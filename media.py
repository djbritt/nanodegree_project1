import movieClass
import fresh_tomatoes
#used for getting movie ratings
import requests
#used for formatting response into json
import json
import unicodedata



key = 'themoviedb api key'
def movieInfo(id):
    #Step one, get movie info
    r = requests.get("https://api.themoviedb.org/3/movie/"+str(id)+"?api_key="+key+"&append_to_response=release_dates")
    #Step two, format info to JSON
    responseFormatted = r.json()
    #Step three, get information for movie
    poster = responseFormatted['poster_path']
    title = responseFormatted['title']
    storyline = unicodedata.normalize('NFKD', responseFormatted['overview']).encode('ascii','ignore')
    rating = unicodedata.normalize('NFKD', responseFormatted['release_dates']['results'][0]['release_dates'][0]['certification']).encode('ascii','ignore')
    return [title, storyline, poster, rating]

data = movieInfo(603)
theMatrix = movieClass.Movie(data[0], data[1], "https://image.tmdb.org/t/p/w500" + data[2], "https://www.youtube.com/watch?v=m8e-FF8MsqU", data[3])

data = movieInfo(11360)
dumbo = movieClass.Movie(data[0], data[1], "https://image.tmdb.org/t/p/w500" + data[2], "https://www.youtube.com/watch?v=22v-1eMIl40", data[3])

data = movieInfo(9078)
swordStone = movieClass.Movie(data[0], data[1], "https://image.tmdb.org/t/p/w500" + data[2], "https://www.youtube.com/watch?v=KnL0rYFKuL4", data[3])

data = movieInfo(218)
terminator = movieClass.Movie(data[0], data[1], "https://image.tmdb.org/t/p/w500" + data[2], "https://www.youtube.com/watch?v=k64P4l2Wmeg", data[3])

data = movieInfo(1635)
theIsland = movieClass.Movie(data[0], data[1], "https://image.tmdb.org/t/p/w500" + data[2], "https://www.youtube.com/watch?v=_ZyNJ3cKfEg", data[3])

data = movieInfo(8467)
dumber = movieClass.Movie(data[0], data[1], "https://image.tmdb.org/t/p/w500" + data[2], "https://www.youtube.com/watch?v=MSu25pQ4iFw", data[3])

movies = [theMatrix, dumbo, swordStone, terminator, theIsland, dumber]
# print str(theMatrix.storyline)

#Send array of movies to fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
