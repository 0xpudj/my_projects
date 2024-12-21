print("          Calender forme like this: (day /month /year)")
day,months,year=int(input("Enter the date: ")),int(input("/ ")),int(input("/ "))

Y=year%100
Z=year//100
week_days=int((day+ ( (13*(months+1)) /5) + Y + (Y/4) + (Z/4) + 5*Z) %7)

match months:
    case 1:
        month="January"
    case 2:
        month="February"
    case 3:
        month="March"
    case 4:
        month="April"
    case 5:
        month="May"
    case 6:
        month="June"
    case 7:
        month="July"
    case 8:
        month="August"
    case 9:
        month="September"
    case 10:
        month="October"
    case 11:
        month="November "
    case 12:
        month="December"
    case other:
        print("\n    Invalid month: (1-12)")

match week_days:
    case 0:
        week_days= "Saturday"
    case 1:
        week_days= "Sunday" 
    case 2:
        week_days= "Monday"
    case 3:
        week_days= "Tuesday"    
    case 4:
        week_days= "Wednesday"
    case 5:
        week_days= "Thursday"
    case 6:
        week_days= "Friday"

if week_days and day<32 and months<13 and year<2030:
    print(f"\nThe date is :  {week_days} {day} {month} {year}")
else:
    print("\n    Invallid date check our information")