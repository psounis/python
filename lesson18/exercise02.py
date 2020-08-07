from random import randrange, seed
from datetime import datetime

class Video:
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.artist} - {self.title} ({self.duration})"

class Playlist:
    def __init__(self, title, descr, duration, videos):
        self.title = title
        self.descr = descr
        self.duration = duration
        self.videos = videos

    def __str__(self):
        st = f"{self.title} ({self.descr}). Duration: {self.duration}"
        st += "\n" + "-" * 20
        for video in self.videos:
            st += "\n" + str(video)
        return st

    def add_video(self, video):
        self.videos += [video]

    def recommendation(self):
        return f"I recommend: {self.videos[randrange(len(self.videos))]}"


class ClassicalPlaylist(Playlist):
    def __init__(self, title, descr, duration, videos, period):
        super().__init__(title, descr, duration, videos)
        self.period = period

    def recommendation(self):
        return f"I recommend: {self.videos[0]} !!"


seed(datetime.now())

p = Playlist("Zouzounia","Paidika tragoudia", "45.18",
             [Video("ZouzTV", "Xarwpa ta dio mou xeria ta xtipw", "03.22"), Video("ZouzTv", "Magia i melissa", "04.17")])


print(p)
print(p.recommendation())

c = ClassicalPlaylist("Beethoven No.9", "", "88.13",
                      [Video("Beethoven", "Track 01", "03.22"),
                       Video("Beethoven", "Track 02", "04.17")], "baroque")

print(c)
print(c.recommendation())