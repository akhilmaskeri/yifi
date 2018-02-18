import requests

try:
    from yifi import Movie
except ImportError:
    import Movie

try:
    from urllib.parse import urlencode      # python 3.X
except ImportError:
    from urllib import urlencode            # python 2.X

# class to handle responses 
class browser:

    def __init__(self):
        self.query ="https://yts.ag/api/v2/list_movies.json?"
        self.details = "https://yts.ag/api/v2/movie_details.json?"

    # fetches the movies that are sorted by number of seeds
    def bySeeds(self,limit=20,page=1,min_rating=0):
        param = dict({"limit":limit})
        param["page"]=page
        param["minimum_rating"]=min_rating

        response=requests.get(self.query+urlencode(param))

        movie = Movie.Movie(response)
        return movie.getRecents()

    # fetch the movies sorted by rating
    def byRating(self,limit=20,page=1,min_rating=0):
        param = dict({"limit":limit})
        param["page"]=page
        param["minimum_rating"]=min_rating
        param["sort_by"]="rating"
        response=requests.get(self.query+urlencode(param))

        movie = Movie.Movie(response)
        return movie.getRecents()

    # fetch the details of movie < using the id >
    def detail(self,Id):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)

        return movie.details()

    # send the string with the query term
    def find(self,query):
        param = dict({"query_term":str(query)})
        url = self.query+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)

        return movie.getRecents()

    # fetch the youtube trailer url
    def getTrailerUrl(self,Id):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)
        return str(movie.getTrailerUrl())

    # fetch the qualities
    def getQualities(self,Id):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)

        response=requests.get(url)
        movie = Movie.Movie(response)

        return movie.getQualities()

    # fetch magnet url
    def getMagnetUrl(self,Id,quality):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)
        return movie.Magnet(quality)

    # fetch torrent url
    def getTorrentUrl(self,Id,quality):
        param = dict({"movie_id":str(Id)})

        url = self.details+urlencode(param)
        response=requests.get(url)
        movie = Movie.Movie(response)
        return movie.Torrent(quality)
