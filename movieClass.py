"""
Movie Database
~~~~~~~~~~
*fullstack_moviedb* is a simple tool that grabs movie information from "The Movie Databse" located themoviedb.org.
This tool then creates an array of the information, spits it into a file that creates a visual web experience of the information.
"""

__title__ = 'fullstack_moviedb'
__version__ = '1.0.0'
__author__ = 'Daniel Britt'

import webbrowser

class Movie():
    def __init__(self, movieName, movieStoryline, posterImage, trailerLink, rating):
        self.title = movieName
        self.storyline = movieStoryline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerLink
        self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
