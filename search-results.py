import requests, bs4, webbrowser

search = input("Search with python package installer:").replace(' ','+')

link = "https://pypi.org/search/?q="

link += search

print("Searching...")

res = requests.get(link)

soup = bs4.BeautifulSoup(res.text,'html.parser')
linkElems = soup.select('.package-snippet')

for i in range(min(5,len(linkElems))):
    url = "https://pypi.org/" + linkElems[i].get('href')
    print('Opening',url)
    webbrowser.open(url)

print("\nDone! Enjoy : )")