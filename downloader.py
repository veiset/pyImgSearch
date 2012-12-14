from urllib.request import Request, build_opener
from os import path
import sys

def download(url, target):
    ''' 
    download(string, string) -> boolean

    Downloads content from a given URL and saves it to the 
    given target location. Return True if the content
    was successfully downloaded, or False if the download
    fails (no content, target already exists).

    Keyword arguments:
    url    -- url of content (e.g: http://../hello.png)
    target -- filesystem location to save the content to

    return True if success, False if otherwise
    '''

    if path.exists(target):
        print("Error retrieving image: file target '%s' already exists." % target)
        return False

    opener = build_opener()  
    req = Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')

    try: 
        fp = opener.open(req)
        with open(target, "wb") as fo:
            fo.write(fp.read())
        return True
    except: 
        print("Error fetching content: ", sys.exc_info()[0])
        return False
