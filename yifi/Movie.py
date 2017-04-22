import json
import webbrowser
import textwrap
import urllib
import trackers

class Movie:

    def __init__(self,response):
        self.jsonObject = json.loads(response.text)

        if "movie" in self.jsonObject["data"]:
            self.movie = self.jsonObject["data"]["movie"]
            self.qualities=[]
            for i in range(len(self.movie["torrents"])):
                self.qualities.append(self.movie['torrents'][i]['quality'].encode('utf-8'))

    def downloadMagnet(self,quality):

        base = "magnet:?xt=urn:btih:"+self.movie["torrents"][quality-1]["hash"]+"&dn"+urllib.quote(self.movie["title"])
        for t in trackers.getTrackers():
            base+= '&tr='+t

        webbrowser.open(base)
        exit(0)

    def downloadTorrent(self,quality):
        print self.movie['torrents'][quality-1]['url'],"~/Downloads/"+self.movie['title']+".torrent"
        webbrowser.open(self.movie["torrents"][quality-1]['url'])
        exit(0)


    def getQualities(self):
        return self.qualities

    def displayLatest(self):
        for movie in self.jsonObject["data"]["movies"]:
            print str(movie["id"]),str(movie["title"].encode('utf-8'))


    def displayStatus(self):
        movie = self.movie

        print "title   : "+str(movie["title_long"].encode('utf-8'))
        print "year    : "+str(movie["year"])
        print "rating  : * "+str(movie["rating"])
        print "runtime : "+str(movie["runtime"])+" min"
        print "lang    : "+str(movie["language"])
        print "genres  :",[str(genre) for genre in movie["genres"]]
        print "mpa     : "+movie["mpa_rating"]
        print "quality : " + str(self.getQualities())
        print "descr   :"+"\n\t  ".join(textwrap.wrap(" "+movie["description_intro"]))
        print ""

    def watchTrailer(self):
        webbrowser.open("http://youtube.com/watch?v=" + self.movie["yt_trailer_code"])
        exit(0)
