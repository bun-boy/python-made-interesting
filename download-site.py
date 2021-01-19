import requests

link = input("Enter link:")
res = requests.get(link)

site = open("site-code.html","wb")

for ch in res:
    site.write(ch)
site.close()