from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        a, b = numer, denom
        while b:
            a, b = b, a%b
        self.numer = numer // a
        self.denom = denom // a

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return self + Rational(-1,1) * other

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
        if power < 0:
            self.numer, self.denom = self.denom, self.numer
        return Rational(self.numer ** abs(power), self.denom ** abs(power))

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
