import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings
import numpy as np  # Added to fix the undefined 'np' error

# Load the dataset
file_path = "C:/Users/abdol/Documents/project/Python/countries-aggregated.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Q1: Visualize the time series
# Convert 'Date' column to datetime and filter data for France
df["Date"] = pd.to_datetime(df["Date"])
country_df = df[df["Country"] == "France"].copy()

# Plot cumulative confirmed cases
plt.figure()
plt.plot(country_df["Date"], country_df["Confirmed"], label="Confirmed Cases", color="blue")
plt.title("COVID-19 Confirmed Cases in France")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()

# Q2: Identify key patterns
# Compute daily new cases and 7-day rolling average
country_df["Daily_New"] = country_df["Confirmed"].diff().fillna(0)
country_df["Rolling_7"] = country_df["Daily_New"].rolling(window=7).mean()

# Define growth phase boundaries for France
phases = [
    ("2020-01-01", "2020-06-01", "1st Wave\n(Exponential)", "red"),
    ("2020-06-01", "2020-09-01", "Stabilization\n(Summer 2020)", "green"),
    ("2020-09-01", "2021-02-01", "2nd Wave\n(Exponential)", "orange"),
    ("2021-02-01", "2021-07-01", "3rd Wave\n(Linear)", "purple"),
    ("2021-07-01", "2022-01-01", "Delta Wave", "brown"),
    ("2022-01-01", "2022-06-01", "Omicron Wave\n(Rapid Spike)", "blue"),
]

# Create subplots for visualization
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Plot 1: Cumulative Confirmed Cases
axes[0].plot(country_df["Date"], country_df["Confirmed"], color="steelblue", linewidth=2)
axes[0].set_title("COVID-19 Confirmed Cases in France — Overall Trend", fontsize=13)
axes[0].set_ylabel("Cumulative Confirmed Cases")
axes[0].set_xlabel("Date")

# Highlight growth phases
for start, end, label, color in phases:
    axes[0].axvspan(pd.Timestamp(start), pd.Timestamp(end), alpha=0.15, color=color, label=label)

axes[0].legend(loc="upper left", fontsize=8)
axes[0].tick_params(axis='x', rotation=45)

# Plot 2: Daily New Cases with Rolling Average
axes[1].bar(country_df["Date"], country_df["Daily_New"], color="lightcoral", alpha=0.5, label="Daily New Cases")
axes[1].plot(country_df["Date"], country_df["Rolling_7"], color="darkred", linewidth=2, label="7-day Rolling Average")
axes[1].set_title("Daily New Cases — Growth Phase Detection", fontsize=13)
axes[1].set_ylabel("New Cases per Day")
axes[1].set_xlabel("Date")
axes[1].legend()
axes[1].tick_params(axis='x', rotation=45)

# Annotate key phases on daily plot
for start, end, label, color in phases:
    mid = pd.Timestamp(start) + (pd.Timestamp(end) - pd.Timestamp(start)) / 2
    axes[1].axvspan(pd.Timestamp(start), pd.Timestamp(end), alpha=0.1, color=color)
    axes[1].text(mid, axes[1].get_ylim()[1] * 0.85, label.split("\n")[0],ha='center', fontsize=7, color=color, rotation=90)

plt.tight_layout()
plt.show()

# Print a summary of the trend analysis
print("=" * 50)
print("TREND & GROWTH PHASE ANALYSIS — France")
print("=" * 50)

total_cases = country_df["Confirmed"].max()
peak_day = country_df.loc[country_df["Daily_New"].idxmax(), "Date"]
peak_cases = country_df["Daily_New"].max()

print(f"Total confirmed cases  : {total_cases:,.0f}")
print(f"Peak daily new cases   : {peak_cases:,.0f} on {peak_day.date()}")
print()
print("Identified phases:")
for start, end, label, _ in phases:
    phase_data = country_df[
        (country_df["Date"] >= pd.Timestamp(start)) &
        (country_df["Date"] < pd.Timestamp(end))
    ]
    avg_daily = phase_data["Daily_New"].mean()
    print(f"  {label.replace(chr(10), ' '):<30} | Avg daily new cases: {avg_daily:>10,.0f}")

# Q3: Compute a 7-day moving average
country_df["Moving_Avg_7"] = country_df["Confirmed"].rolling(window=7).mean()

plt.figure(figsize=(14, 6))

# Original data
plt.plot(country_df["Date"], country_df["Confirmed"], 
        color="lightblue", linewidth=1, alpha=0.7, label="Confirmed Cases (Raw)")

# 7-day moving average
plt.plot(country_df["Date"], country_df["Moving_Avg_7"], 
        color="darkblue", linewidth=2, label="7-Day Moving Average")

plt.title("COVID-19 Confirmed Cases in France — 7-Day Moving Average", fontsize=13)
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("7-Day Moving Average (last 10 values):")
print(country_df[["Date", "Confirmed", "Moving_Avg_7"]].tail(10).to_string(index=False))

# Handle specific warnings instead of ignoring all
warnings.filterwarnings("ignore", category=FutureWarning)  # Ignore warnings about deprecated features
warnings.filterwarnings("ignore", category=UserWarning)    # Ignore user-specific warnings

# Optionally, log warnings to understand their source during debugging
# warnings.simplefilter("always")  # Uncomment this line to enable all warnings for debugging purposes

# --- Prepare data ---
ts = country_df.set_index("Date")["Confirmed"]

# Split: last 30 days = test, rest = train
train = ts.iloc[:-30]
test  = ts.iloc[-30:]

# --- Build ARIMA model ---
# order=(p,d,q): p=autoregression, d=differencing, q=moving average
model = ARIMA(train, order=(5, 2, 1))
model_fit = model.fit()

print(model_fit.summary())

# --- Forecast next 30 days ---
forecast_steps = 30
forecast = model_fit.forecast(steps=forecast_steps)
forecast_index = pd.date_range(start=ts.index[-1], periods=forecast_steps + 1, freq="D")[1:]

# --- Evaluate on test set ---
pred_on_test = model_fit.forecast(steps=30)
mae  = mean_absolute_error(test, pred_on_test)
rmse = np.sqrt(mean_squared_error(test, pred_on_test))

print(f"\nModel Evaluation on last 30 days:")
print(f"  MAE  : {mae:,.0f}")
print(f"  RMSE : {rmse:,.0f}")

# --- Plot ---
plt.figure(figsize=(14, 6))

plt.plot(train.index, train, 
        color="steelblue", linewidth=1.5, label="Training Data")

plt.plot(test.index, test, 
        color="green", linewidth=1.5, label="Actual (Test)")

plt.plot(forecast_index, forecast, 
        color="red", linewidth=2, linestyle="--", label="ARIMA Forecast")

plt.plot(test.index, pred_on_test, 
        color="orange", linewidth=1.5, linestyle=":", label="Predicted (Test Period)")

# Confidence interval shading
conf_int = model_fit.get_forecast(steps=forecast_steps).conf_int()
plt.fill_between(forecast_index, 
                conf_int.iloc[:, 0], 
                conf_int.iloc[:, 1], 
                color="red", alpha=0.1, label="95% Confidence Interval")

plt.title("COVID-19 Forecast — ARIMA(5,2,1) — France", fontsize=13)
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()