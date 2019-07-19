import urllib3
from bs4 import BeautifulSoup


year = "2019"

url = "http://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"
dataUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(dataUrl, "html.parser")


i = 1
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

for divItem in movieList:
    div = divItem.find('div', attrs={'class': 'lister-item-content'})

    header = div.findChildren('h3', attrs={'class':'lister-item-header'})

    print(str(i) + '.', 'Movie: ' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))

    i += 1
