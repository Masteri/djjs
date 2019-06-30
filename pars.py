from bs4 import BeautifulSoup
import requests
import io, json

url = ("http://www.alsautopa.com/vehiclelist.php?SortOrder=1&SortDirection=DESC&VehicleType=C")
r = requests.get(url)
soup = BeautifulSoup(r.text)
list1 = soup.find("table", id="rsTable")


#for item in soup.select("td.style14"):
#    print(item.get_text())

list3 = []

for tr in list1.select("tr"):
    print('tr---') #print(list1.index(tr))
    for td in tr.find_all("td"):#class_="style14"):
        if td.find('a'):
            if td.img:
                print(td.img['src'])
            print(td.text, td.a.get('href'))#, td.img.get('srd'))
        print(td.text)
        #print(list1.index(tr))
        print('td--')




#for td in list1.parent.find_all_next('td'):
#    list3.append(td.text)

#for el in list2[6:]:
    #list3.append(el.a.get('href'))


#listword = ['href', 'img', 'stock', 'year', 'model', 'make', 'title', 'description', 'price', '0', '1', '2', '3']
#dictory = dict(zip(listword, list3))
#print(dictory)

#with io.open('data.txt', 'w', encoding='utf-8') as f:
#  f.write(json.dumps(list3, ensure_ascii=False))


#import json
#with open('no.txt', 'w') as txtfile:
#    json.dump(list3, txtfile)




