import requests
import random
import bs4

category = input("Select a category: \n1. Inspirational\n2. Life\n3. Motivational\n4. Love \n      ").lower()

if category == "inspirational" or category == "life" or category == "motivational" or category == "love":
    web_site = requests.get("https://www.azquotes.com/quotes/topics/"+category+".html")
else:
    print("Invalid category")
    exit()


html = web_site.text
parser = bs4.BeautifulSoup(html, 'html.parser')
quotes = parser.findAll("a",attrs={"class": "title"})
authors = parser.findAll("div",attrs={"class": "author"})

random_quote = random.randrange(0, len(quotes))
print(f'Quote of the day:\n"{quotes[random_quote].text.strip()}" ---- {authors[random_quote].text.strip()}')

