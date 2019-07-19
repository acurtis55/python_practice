import urllib3
from bs4 import BeautifulSoup



class IMDBClient:

    def __init__(self):
        self.url = "http://www.imdb.com/search/title?"


    def searchByReleaseYear(self, releaseYear):

        print("Searching by release year: ", releaseYear)
        searchUrl = self.url + "release_date=" + releaseYear

        dataUrl = urllib3.PoolManager().request('GET', searchUrl).data
        soup = BeautifulSoup(dataUrl, "html.parser")

        i = 1
        movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

        for divItem in movieList:
            div = divItem.find('div', attrs={'class': 'lister-item-content'})

            header = div.findChildren('h3', attrs={'class': 'lister-item-header'})

            print(str(i) + '.', 'Movie: ' + str(
                (header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))

            i += 1
        print('\n')

    def searchByTitle(self, title):

        print("Searching by title: ", title)
        searchUrl = self.url + "title=" + title

        dataUrl = urllib3.PoolManager().request('GET', searchUrl).data
        soup = BeautifulSoup(dataUrl, "html.parser")

        i = 1
        movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

        for divItem in movieList:
            div = divItem.find('div', attrs={'class': 'lister-item-content'})

            header = div.findChildren('h3', attrs={'class': 'lister-item-header'})

            print(str(i) + '.', 'Movie: ' + str(
                (header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))

            i += 1
        print('\n')



client = IMDBClient()
client.searchByReleaseYear("2015")
client.searchByTitle("Fear")
