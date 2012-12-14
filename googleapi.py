from urllib.request import urlopen
from urllib.parse import quote_plus 
import json
import downloader

class GoogleImage():
    ''' 
    A simple data representation of a result from Google image
    search. Do not contain the images themselves, only
    information about the search result.
    '''

    def __init__(self, url, size, title=None, imageId=None):
        ''' 
        Keyword arguments:
        url     -- url of image
        size    -- (width, height) of image
        title   -- descriptive text
        imageId -- google API image id
        '''

        self.url = url
        self.size = size
        self.title = title 
        self.imageId = imageId

class GoogleImageSearch():
    '''
    Google Image Search API interface.
    '''

    googleAPI = 'https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s'

    def getContent(self, keyword):
        ''' 
        getContent(string) -> string (json)

        Uses the Google Image API to search for images
        for a given keyword. Returns the meta-data result 
        as a json representation. 

        Keyword arguments:
        keyword -- google image search term

        return json representation of the search result
        '''

        apiRequestURL = self.googleAPI % quote_plus(keyword)
        data = urlopen(apiRequestURL).read().decode('utf-8')
        return data

    def search(self, keyword):
        ''' 
        search(string) -> GoogleImage Array

        Uses google search API to search for images of a given
        keyword, returns object representation result that 
        contains information about url, size, title and imageId.

        Keyword arguments:
        keyword -- google image search term

        return GoogleImage array from search result
        '''
        googleImages = []
        
        jsondata = self.getContent(keyword)
        data = json.loads(self.getContent(keyword))

        for img in data['responseData']['results']:
            url = img['url']
            title = img['contentNoFormatting']
            size =  img['width'], img['height']
            imgId = img['imageId']

            googleImages.append(GoogleImage(url, size, title, imgId))

        return googleImages



