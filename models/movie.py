import webbrowser

from media import Media


class Movie(Media):
    """"Movie extends Media with their storyline and trailer"""

    def __init__(self, title, story_line, trailer_youtube_url, poster_image_url):
        """Initializes the variables  """

        Media.__init__(self, title, poster_image_url)
        self.story_line = story_line
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
