import urllib.request
from bs4 import BeautifulSoup
import datetime

for i in range(1,50):
   url = "https://www.hepsiburada.com/ara?q=blender&sayfa="+str(i)
   f = urllib.request.urlopen(url)
   page = f.read()
   f.close()
   soup = BeautifulSoup(page)

   data_list = []

   for link in soup.findAll('img'):
      data_list.append(link.get('data-src'))

   data_list = list(filter((None).__ne__, data_list))

   for d in data_list:
      urllib.request.urlretrieve(
         d, 'blender/'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S%f")+'.jpg')
   print(str(i)+'. page completed!')
