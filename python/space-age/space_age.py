class SpaceAge(object):
    earth_year = 31557600
    corr = {
        'earth': 1,
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def repr(self, planet=None):
        return round(self.seconds / (self.earth_year * (self.corr[planet] if planet else 1)), 2)

    def __getattr__(self, name):
        planet = name[3:]
        