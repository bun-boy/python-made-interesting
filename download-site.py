import requests

link = input("Enter link:")
res = requests.get(link)

hard_copy = open("hard_copy.html","wb")

for ch in res:
    hard_copy.write(ch)
hard_copy.close()