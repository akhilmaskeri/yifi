import urllib

class urlgen:
    def __init__(self):
        self.url = "https://yts.ag/api/v2/list_movies.json?"
        self.parm = dict()

    def add(self,key,value):
        self.parm[key] = str(value)

    def genrate(self,arg):

        if "-s" in arg:
            sort = ""

            if len(arg) >= arg.index("-s")+1:
                sort = arg[arg.index("-s")+1]

            if sort == "r" or sort == "s" or sort == "rating" or sort == "seeds":
                if sort == "r" or sort == "rating":
                    sort = "rating"
                else:
                    sort = "seeds"

                self.add("sort_by", sort)
            else:
                pass

        if "-o" in arg:
            order = ""

            if len(arg) >= arg.index("-o")+1:
                order = arg[arg.index("-o")+1]

            if order == "a" or order == "d":
                if order == "a":
                    order = "asc"
                else:
                    order = "desc"
                self.add("order_by", order)
            else:
                pass

        if "-l" in arg:
            length = ""
            if len(arg) >= arg.index("-l")+1:
                length = arg[arg.index("-l")+1]
            try:
                val = int(length)
                self.add("limit",length)
            except ValueError:
                print "value error with parsing the limit "
                print '-'*40

        if "-p" in arg:
            page = ""
            if len(arg) >= arg.index("-p")+1:
                page = arg[arg.index("-p")+1]
            try:
                val = int(page)
                self.add("page",page)
            except ValueError:
                print "value error with parsing the page"
                print '-'*40

        if "-f" in arg:
            q = ""
            if len(arg) >= arg.index("-f")+1:
                q = arg[arg.index("-f")+1]

            if "-" not in q:
                self.add("query_term",q)

        if "-g" in arg:
            geners = ""
            if len(arg) >= arg.index("-g")+1:
                g = arg[arg.index("-g")+1].split(",")
                self.add("gener",g)

        return self.url+urllib.urlencode(self.parm)

