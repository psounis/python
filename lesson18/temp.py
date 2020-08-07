from random import randrange, seed
from datetime import datetime


class Video:
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.artist}-{self.title} ({self.duration})"


class Playlist:
    def __init__(self, title, descr, duration, videos):
        self.title = title
        self.descr = descr
        self.duration = duration
        self.videos = videos

    def __str__(self):
        st = f"{self.title}({self.descr}) - {self.duration}"
        st += "\n" + "-" * 20
        for video in self.videos:
            st += "\n" + str(video)
        return st

    def add_video(self, video):
        self.videos += [video]

    def recommendation(self):
        return self.videos[randrange(len(self.videos))]


class ClassicalPlaylist(Playlist):
    def __init__(self, title, descr, duration, videos, period):
        super().__init__(title, descr, duration, videos)
        self.period = period

    def __str__(self):
        st = f"{self.title}({self.descr}) - {self.duration} [Period: {self.period}]"
        st += "\n" + "-" * 20
        for video in self.videos:
            st += "\n" + str(video)
        return st

    def recommendation(self):
        return self.videos[0]


seed(datetime.now())

p = Playlist("Beethoven Symphony no.9", "Metropolitan Orchestra", "45.18",
             [Video("Beethoven", "Track 1", "12.14"), Video("Beethoven", "Track 2", "07.25")])
print("I recommend: " + str(p.recommendation()))


cp = ClassicalPlaylist("Beethoven Symphony no.9", "Metropolitan Orchestra", "45.18",
             [Video("Beethoven", "Track 1", "12.14"), Video("Beethoven", "Track 2", "07.25")],
              "classical")
print("I recommend: " + str(p.recommendation()))
