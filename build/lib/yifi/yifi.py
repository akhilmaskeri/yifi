import requests
try:
    from yifi import Movie
except ImportError:
    import Movie

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

class browser:
    def __init__(self):
        self.query ="https://yts.ag/api/v2/list_movies.json?"
        self.details = "https://yts.ag/api/v2/movie_details.json?"

    def bySeeds(self,limit=20,page=1,min_rating=0):
        param = dict({"limit":limit})
        param["page"]=page
        param["minimum_rating"]=min_rating

        response=requests.get(self.query+urlencode(param))

        movie = Movie.Movie(response)
        return movie.getRecents()

    def byRating(self,limit=20,page=1,min_rating=0):
        param = dict({"limit":limit})
        param["page"]=page
        param["minimum_rating"]=min_rating
        param["sort_by"]="rating"
        response=requests.get(self.query+urlencode(param))

        movie = Movie.Movie(response)
        return movie.getRecents()

    def detail(self,Id):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)

        return movie.details()

    def find(self,query):
        param = dict({"query_term":str(query)})
        url = self.query+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)

        return movie.getRecents()

    def getTrailerUrl(self,Id):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)
        return str(movie.getTrailerUrl())

    def getQualities(self,Id):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)

        response=requests.get(url)
        movie = Movie.Movie(response)

        return movie.getQualities()

    def getMagnetUrl(self,Id,quality):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)
        return movie.Magnet(quality)

    def getTorrentUrl(self,Id,quality):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)
        return movie.Torrent(quality)
