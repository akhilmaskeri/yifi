import json
import webbrowser
import urllib

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class Movie:

    def __init__(self,response):
        self.jsonObject = json.loads(response.text)
        self.trackers = [
            'udp://open.demonii.com:1337/announcejj',
            'udp://tracker.istole.it:80',
            'http://tracker.yify-torrents.com/announce',
            'udp://tracker.publicbt.com:80',
            'udp://tracker.openbittorrent.com:80',
            'udp://tracker.coppersurfer.tk:6969',
            'udp://glotorrents.pw:6969/announce',
            'udp://tracker.opentrackr.org:1337/announce',
            'udp://torrent.gresille.org:80/announce',
            'udp://p4p.arenabg.com:1337',
            'udp://tracker.leechers-paradise.org:6969',
            'http://exodus.desync.com:6969/announce'
        ]

        if "movie" in self.jsonObject["data"]:
            self.movie = self.jsonObject["data"]["movie"]
            self.qualities=[]
            for i in range(len(self.movie["torrents"])):
                self.qualities.append(self.movie['torrents'][i]['quality'])

    def Magnet(self,quality):

        base = "magnet:?xt=urn:btih:"+self.movie["torrents"][quality-1]["hash"]+"&dn"+quote(self.movie["title"])
        for t in self.trackers:
            base+= '&tr='+t

        return base

    def Torrent(self,quality):
        #print (self.movie['torrents'][quality-1]['url'],"~/Downloads/"+self.movie['title']+".torrent")

        return self.movie["torrents"][quality-1]['url']

    def getQualities(self):
        return self.qualities

    def getRecents(self):
        movie_list = []

        if self.jsonObject["data"]["movie_count"] > 0:
            for movie in self.jsonObject["data"]["movies"]:
                try:
                    movie_list.append((str(movie["id"]).decode('unicode-escape'),str(movie["title"]).decode('unicode-escape')))
                except AttributeError:
                    movie_list.append((str(movie["id"]),str(movie["title"])))
                except UnicodeEncodeError:
                    pass

        return movie_list


    def details(self):
        movie = self.movie
        details = dict();

        details["title"] = str(movie["title_long"])
        details["year"] = str(movie["year"])
        details["rating"] = str(movie["rating"])
        details["runtime"] = str(movie["runtime"])
        details["language"]=str(movie["language"])
        details["genres"]=[str(genre) for genre in movie["genres"]]
        details["mpa_rating"]=movie["mpa_rating"]
        details["quality"]=str(self.getQualities())
        details["description_intro"]=movie["description_intro"]

        return details

    def getTrailerUrl(self):
        return "http://youtube.com/watch?v=" + self.movie["yt_trailer_code"]

