import requests
import shutil,os
import sys
import Movie

from urlgen import urlgen

url = urlgen().genrate(sys.argv)

def helpThePoorSoul():
    f = open("../help.txt")
    print f.read()
    f.close()

    exit()

if '--help' in sys.argv:
    helpThePoorSoul()

if "--url" in sys.argv:
    print url

response=requests.get(url)
movie = Movie.Movie(response)

if "-id" in sys.argv:

    if "--trailer" in sys.argv:
        movie.watchTrailer()

    if "--magnet" in sys.argv:

        if "-q" in sys.argv:

            if len(sys.argv) >= sys.argv.index("-q")+1:
                quality = sys.argv[sys.argv.index("-q")+1]

            if quality not in movie.getQualities():
                helpThePoorSoul()

        else:
            print "please select the quality :"
            qualities = movie.getQualities()

            for i in range(len(qualities)):
                print i+1," -> ",qualities[i]

            quality = int(raw_input())

        movie.downloadMagnet(quality)

    if "--download" in sys.argv:

        quality = ""

        if "-q" in sys.argv:

            if len(sys.argv) >= sys.argv.index("-q")+1:
                quality = sys.argv[sys.argv.index("-q")+1]

            if quality not in movie.getQualities():
                helpThePoorSoul()

        else:
            print "please select the quality :"
            qualities = movie.getQualities()

            for i in range(len(qualities)):
                print i+1," -> ",qualities[i]

            quality = int(raw_input())

        movie.downloadTorrent(quality)

    movie.displayStatus()


else:
    try:
        movie.displayLatest()
    except KeyError:
        print "sorry! couldn't find the movie"
        print "please check the movie name again"
