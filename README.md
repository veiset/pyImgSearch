pyImgSearch
===========
A python Interface for the Google Image Search API

Example usage 
-------------
```python
from googleapi import GoogleImageSearch
from downloader import download

googleImage = GoogleImageSearch()
images = googleImage.search("super mario snes")

for image in images: 
    download(image.url, 'img/' + image.imageId)
```

The code-snippet will search for images matching 'super mario snes' using
the Google Image Search API and download the images to a local folder 'img'.
