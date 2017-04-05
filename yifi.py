import requests
import shutil,os
import json,sys
import webbrowser

from urlgen import urlgen
import magnet


def displayHelp():
    f = open("help.txt")
    print f.read()
    f.close()
    exit()

if '--help' in sys.argv:
    displayHelp()

url = urlgen()
url = url.genrate(sys.argv)

if "--url" in sys.argv:
    print url

response=requests.get(url)
response = json.loads(response.text)

print "status : ",response["status"],"| ",response["status_message"]

if "-id" in sys.argv:
    movie = response["data"]["movie"]

    if "--trailer" in sys.argv:
        webbrowser.open("http://youtube.com/watch?v="+movie["yt_trailer_code"]);
        exit(0)

    if "--magnet" in sys.argv:
        quality = 0
        if "-q" in sys.argv:
            if len(sys.argv) >= sys.argv.index("-q")+1:
                quality = sys.argv[sys.argv.index("-q")+1]

            if type(quality) is not int:
                displayHelp()

        webbrowser.open(magnet.getMagnet(movie,quality))
        exit(0)

    if "--download" in sys.argv:
        quality = ""
        if "-q" in sys.argv:
            if len(sys.argv) >= sys.argv.index("-q")+1:
                quality = sys.argv[sys.argv.index("-q")+1]
        else:
            quality = len(movie["torrents"])-1

        print movie['torrents'][quality]['url'],"~/Downloads/"+movie['title']+".torrent"
        webbrowser.open(movie["torrents"][quality]['url'])
        exit(0)

    print "title   : "+str(movie["title_long"].encode('utf-8'))
    print "year    : "+str(movie["year"])
    print "rating  : * "+str(movie["rating"])
    print "runtime : "+str(movie["runtime"])+" min"
    print "lang    : "+str(movie["language"])
    print "genres  :",[str(genre) for genre in movie["genres"]]
    print "mpa     : "+movie["mpa_rating"]
    print "descr   : "+movie["description_intro"]

    qualities = ""
    for i in range(len(movie["torrents"])):
        if i < len(movie['torrents'])-1:
            qualities += (movie['torrents'][i]['quality']+" , ")
        else:
            qualities += movie['torrents'][i]['quality']
    print "quality : "+qualities



else:
    for movie in response["data"]["movies"]:
        print str(movie["id"]),str(movie["title"].encode('utf-8'))
