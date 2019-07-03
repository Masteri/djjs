from bs4 import BeautifulSoup
import requests
import io, json

url = ("http://www.alsautopa.com/vehiclelist.php?SortOrder=1&SortDirection=DESC&VehicleType=C")
r = requests.get(url)
soup = BeautifulSoup(r.text)
list1 = soup.find("table", id="rsTable")
tdtext = []
tdhref = []
jobject = []
in_text = {}

for tr in list1.select("tr"):
    inx = (list1.index(tr))
    for td in tr.find_all("td"):
        for o in td:

            if td.find('a'):
                if td.img:
                    hr = ({list1.index(tr): 'http://www.alsautopa.com/' + td.img['src']})
                    tdhref.append(hr)
                    in_text.update({'name': td.text, 'img': hr})
            else:
                in_text.update({'name': td.text})



        jobject.append(dict([(inx, in_text)]))

        in_text = {}
        i = ({list1.index(tr): td.text})
        tdtext.append(i)



print('tdtext: ', tdtext[8:]) #delete firts items
print('tdhref: ', tdhref)
print(jobject)
print(json.dumps(jobject, indent=4))


#listword = ['href', 'img', 'stock', 'year', 'model', 'make', 'title', 'description', 'price', '0', '1', '2', '3']
#dictory = dict(zip(listword, list3))
#print(dictory)

with io.open('data.txt', 'w', encoding='utf-8') as f:
  f.write(json.dumps(tdtext[8:], ensure_ascii=False))



