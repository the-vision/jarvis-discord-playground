import imdb


def main(argv=None):
    if not argv:
        argv = sys.argv
    s = Store()
    if argv[1] in ("help", "--help", "h", "-h"):
        help()
    elif argv[1] == "whoami":
        if os.path.exists(storefn):
            print(list(s.who())[0])
        else:
            s.who(argv[2])
    elif argv[1].startswith("http://www.imdb.com/title/tt"):
        if s.movie_is_in(argv[1]):
            raise
        else:
            i = imdb.IMDb()
            movie = i.get_movie(argv[1][len("http://www.imdb.com/title/tt") : -1])
            print("%s (%s)" % (movie["title"].encode("utf-8"), movie["year"]))
            for director in movie["director"]:
                print("directed by: %s" % director["name"].encode("utf-8"))
            for writer in movie["writer"]:
                print("written by: %s" % writer["name"].encode("utf-8"))
            s.new_movie(movie)
            rating = None
            while not rating or (rating > 5 or rating <= 0):
                try:
                    rating = int(raw_input("Rating (on five): "))
                except ValueError:
                    rating = None
            date = None
            while not date:
                try:
                    i = raw_input("Review date (YYYY-MM-DD): ")
                    date = datetime.datetime(*time.strptime(i, "%Y-%m-%d")[:6])
                except:
                    date = None
            comment = raw_input("Comment: ")
            s.new_review(movie, date, rating, comment)
    else:
        help()
