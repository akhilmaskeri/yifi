from __future__ import print_function
import webbrowser
import textwrap
import sys

try:
    import yifi
    yifi.browser()
except (ImportError, AttributeError):
    from yifi import yifi

def displayMovies(movies):
    for movie in movies:
        print(movie[0]+" "+movie[1])

def displayQualities(y,Id):
    print ("please select the quality :")
    qualities = y.getQualities(Id)

    for i in range(len(qualities)):
        print (i+1," -> ",str(qualities[i]))

    quality = int(input())
    return quality

def displayDetails(movie):
    print("title   : "+str(movie["title"]))
    print("year    : "+str(movie["year"]))
    print("rating  : * "+str(movie["rating"]))
    print("runtime : "+str(movie["runtime"])+" min")
    print("lang    : "+str(movie["language"]))
    print("genres  :",[str(genre) for genre in movie["genres"]])
    print("mpa     : "+movie["mpa_rating"])
    print("quality : " + movie["quality"])
    print("descr   :"+"\n\t  ".join(textwrap.wrap(" "+movie["description_intro"])))
    print("")


def help():
    print("usage")
    print()
    print("\t\t-id     <number>      get the details of movie")
    print("\t\t-s      <r or s>      sort by rating")
    print("\t\t-l      <number>      list length (max of 50)")
    print("\t\t-p      <number>      page number")
    print("\t\t-f      <string>      find query term")
    print("\t\t-m      <number>      minimum rating (max 10)")
    print()
    print("\t\t--download            downloads the torrent file")
    print("\t\t--magnet              downloads the movie using the magnet")
    print()

def main():
    arg = sys.argv

    if '--help' in arg:
        help()
        exit()

    y = yifi.browser()

    if "-id" in arg:
        Id = ""
        if len(arg) >= arg.index("-id")+1:
            Id = arg[arg.index("-id")+1]

        if "--trailer" in arg:
            url = y.getTrailerUrl(Id)
            webbrowser.open(url)
            exit()

        if "--magnet" in arg:
            quality = ''
            if "-q" in arg:
                if len(arg) >= arg.index("-q")+1:
                    quality = arg[arg.index("-q")+1]

                if quality not in y.getQualities():
                    quality=displayQualities(y,Id)
            else:
                quality = displayQualities(y,Id)

            url = y.getMagnetUrl(Id,quality)
            webbrowser.open(url)
            exit()

        if "--download" in arg:

            quality = ""

            if "-q" in arg:

                if len(sys.arg) >= arg.index("-q")+1:
                    quality = sys.argv[sys.argv.index("-q")+1]

                if quality not in y.getQualities():
                    quality=displayQualities(y,Id);
            else:
                quality = displayQualities(y,Id)

            url = y.getTorrentUrl(Id,quality)
            webbrowser.open(url)
            exit()

        displayDetails(y.detail(Id))

    else:
        if "-f" in arg:
            q=""
            if len(arg) >= arg.index("-f")+1:
                q = arg[arg.index("-f")+1]

            if "-" not in q:
                lis = y.find(q)
                if(len(lis)==0):
                    print("sorry, no results found :(")
                else:
                    displayMovies(y.find(q))

        else:
            limit = 20
            page = 1
            min_rating = 0

            if "-l" in arg:
                if len(arg) >= arg.index("-l")+1:
                    limit = arg[arg.index("-l")+1]
                try:
                    val = int(limit)
                except ValueError:
                    print ("value error with parsing the limit ")
                    print ('-'*40)

            if "-p" in arg:
                if len(arg) >= arg.index("-p")+1:
                    page = arg[arg.index("-p")+1]
                try:
                    val = int(page)
                except ValueError:
                    print ("value error with parsing the page")
                    print ('-'*40)

            if "-m" in arg:
                if len(arg) >= arg.index("-m")+1:
                    min_rating = arg[arg.index("-m")+1]

            if "-s" in arg:
                if len(arg) >= arg.index("-s")+1:
                    sort = arg[arg.index("-s")+1]
                if sort == "r" or sort == "s" or sort == "rating" or sort == "seeds":
                    if sort == "r" or sort == "rating":
                        displayMovies(y.byRating(limit,page,min_rating))
                    else:
                        displayMovies(y.bySeeds(limit,page,min_rating))
                exit()

            displayMovies(y.bySeeds(limit,page,min_rating))
