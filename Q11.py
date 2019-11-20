import urllib.request , urllib.error , urllib.parse

    url = 'enter url here'

    response = urllib.request.urlopen(url)
    webcontent = response.read()

    print(re.sub('<[^<]+?>','',str(webcontent)))

