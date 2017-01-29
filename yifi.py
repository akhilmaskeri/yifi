import requests
from urlgen import urlgen
import json,sys
import webbrowser

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

    print "title   : "+str(movie["title_long"])
    print "year    : "+str(movie["year"])
    print "rating  : * "+str(movie["rating"])
    print "runtime : "+str(movie["runtime"])+" min"
    print "lang    : "+str(movie["language"])
    print "genres  :",[str(genre) for genre in movie["genres"]]
    print "mpa     : "+movie["mpa_rating"]
    print "descr   : "+movie["description_intro"]

else:
    for movie in response["data"]["movies"]:
        print str(movie["id"]),str(movie["title"])

