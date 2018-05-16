class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__
    

doctor_who = [    
Record (episode = "Rose" , season = 1, rating = 10.81, doctor = "Chris Eccleston", writer = "Russel T Davis"),
Record (episode = "The Doctor Falls", season = 10, rating = 5.29, doctor = "Peter Capaldi", writer = "Steven Moffat"),
Record (episode = "Rise of the Cybermen", season = 2, rating = 9.22, doctor = "David Tennant", writer = "Tom MacRae"),
Record (episode = "The Runaway Bride", season = 3, rating = 9.35, doctor = "David Tennat", writer = "Russel T Davis"),
Record (episode = "Silence in the Library", season = 4, rating = 6.27, doctor = "David Tennant", writer = "Steven Moffat"),
Record (episode = "The Eleventh Hour", season = 5, rating = 10.09, doctor = "Matt Smith", writer = "Steven Moffat"),
Record (episode = "The Imposible Astronaut", season = 6, rating = 8.86, doctor = "Matt Smith", writer = "Steven Moffat"),
Record (episode = "Dinosaurs on a Spaceship", season = 7, rating = 7.57, doctor = "Matt Smith", writer = "Chris Chibnall"),
Record (episode = "Deep Breath", season = 8, rating = 9.17, doctor = "Peter Capaldi", writer = "Steven Moffat"),
Record (episode = "The Husbands of River Song", season = 9, rating = 7.69, doctor = "Peter Capaldi", writer = "Steven Moffat")
]

number_of_shows = {}
for author in doctor_who:
    if author.writer not in number_of_shows:
        number_of_shows[author.writer] =author.episode
        number_of_shows[author.writer]=0
    
    number_of_shows[author.writer]+=1
print(number_of_shows)