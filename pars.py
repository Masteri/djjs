from bs4 import BeautifulSoup
import requests
import io, json

url = ("http://www.alsautopa.com/vehiclelist.php?SortOrder=1&SortDirection=DESC&VehicleType=C")
r = requests.get(url)
soup = BeautifulSoup(r.text)
list1 = soup.find("table", id="rsTable")
tdtext = []
tdhref = []

for tr in list1.select("tr"):
    for td in tr.find_all("td"):
        i = ({list1.index(tr): td.text})
        tdtext.append(i)
        if td.find('a'):
            if td.img:
                hr = ({list1.index(tr): 'http://www.alsautopa.com/' + td.img['src']})
                tdhref.append(hr)


print('tdtext: ', tdtext)
print('tdhref: ', tdhref)

#listword = ['href', 'img', 'stock', 'year', 'model', 'make', 'title', 'description', 'price', '0', '1', '2', '3']
#dictory = dict(zip(listword, list3))
#print(dictory)

with io.open('data.txt', 'w', encoding='utf-8') as f:
  f.write(json.dumps(tdtext, ensure_ascii=False))


#import json
#with open('no.txt', 'w') as txtfile:
#    json.dump(list3, txtfile)




