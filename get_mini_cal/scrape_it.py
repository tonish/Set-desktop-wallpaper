import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()

if now.month < 10:
    month = '0' + str(now.month)
else:
    month = now.month

if now.day < 10:
    day = '0' + str(now.day)
else:
    day = now.day
year = now.year
date =(str(now.year)[-2:]) + str(month) + str(day)
url = 'http://miniature-calendar.com/' + str(date)


def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata =BeautifulSoup(thepage,"html.parser")
    return soupdata

days = ["mon","tue","wed","thu","fri","sat","sun"]
weekDay = now.weekday()
dayName = days[weekDay]
# i =1
# soup = make_soup(url)
# for img in soup.findAll('img'):
#     temp = img.get('src')
#     if temp[:1]=="/":
#         image = url + temp
#     else:
#         image = temp
#
# nametemp = img.get('alt')
#     if len(nametemp)==0:
#        filename = str(i)
#        i=i+1
#     else:
#       filename = nametemp
#
#     imagefile = open(filename + ".jpeg", 'wb')
#     imagefile.write(urllib.request.urlopen(image).read())
#     imagefile.close()

urllib.request.urlretrieve("http://miniature-calendar.com/wp-content/uploads/" + str(year) + '/' + str(month) +'/' + str(date) + dayName + '.jpg', ("d:\\" + 'wallpaper' + ".jpg"))