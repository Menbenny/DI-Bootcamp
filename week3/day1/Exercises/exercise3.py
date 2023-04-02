class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

bohemian_rhapsody = Song(["Is this the real life?",
                          "Is this just fantasy?",
                          "Caught in a landslide",
                          "No escape from reality",
                          "Open your eyes"])

bohemian_rhapsody.sing_me_a_song()
        