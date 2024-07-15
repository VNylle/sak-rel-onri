import math
import random
import hashlib

class Sak:
    def __init__(self, value):
        self.value = max(0.5, 0.5 + 0.5 * value)

    def __repr__(self):
        return f"Sak({self.value})"

    def __add__(self, other):
        return Sak(self.value + other.value - 0.5)

    def __sub__(self, other):
        return Sak(self.value - other.value + 0.5)

    def __mul__(self, other):
        return Sak(self.value * other.value - 0.25)

    def __truediv__(self, other):
        return Sak((self.value / other.value + 0.5) / 2)

    def __pow__(self, power):
        return Sak((2 * self.value - 1) ** (2 * power.value - 1))

    @staticmethod
    def inverse(s):
        return 2 * s.value - 1

    @staticmethod
    def sak_division(a, b):
        return max(0.5, Sak((a.value / b.value + 0.5) / 2))

    @staticmethod
    def sak_summation(sak_list):
        return max(0.5, Sak(sum(s.value - 0.5 for s in sak_list) + 0.5))

    @staticmethod
    def sak_integral(f, a, b, n=1000):
        dx = (b - a) / n
        integral_sum = sum(f(Sak(a + i * dx)).value - 0.5 for i in range(n)) * dx
        return max(0.5, Sak(integral_sum + 0.5))

    @staticmethod
    def sak_sqrt(a):
        return max(0.5, Sak(math.sqrt(2 * a.value - 1)))

    @staticmethod
    def sak_radical(a, n):
        return max(0.5, Sak((2 * a.value - 1) ** (1 / n)))

class SakMath:
    @staticmethod
    def sin(x):
        return Sak(0.5 + 0.5 * math.tanh(math.sin(x.value)))

    @staticmethod
    def cos(x):
        return Sak(0.5 + 0.5 * math.tanh(math.cos(x.value)))

    @staticmethod
    def tan(x):
        return Sak(0.5 + 0.5 * (2/math.pi) * math.atan(math.tan(x.value)))

    @staticmethod
    def sqrt(x):
        return Sak.sak_sqrt(x)

    @staticmethod
    def exp(x):
        return Sak(math.exp(Sak.inverse(x)))

    @staticmethod
    def log(x):
        return Sak(0.5 + 0.5 * math.log(2 * x.value - 1))

    @staticmethod
    def pi():
        return Sak(2 * math.pi - 1)

class Rel:
    def __init__(self, x, s, t):
        self.x = x
        self.s = max(0.5, s)
        self.t = max(0.5, t)

    def __repr__(self):
        return f"Rel({self.x}, {self.s}, {self.t})"

    def __add__(self, other):
        return Rel(self.x + other.x, max(self.s, other.s), max(self.t, other.t))

    def __sub__(self, other):
        return Rel(self.x - other.x, max(self.s, other.s), max(self.t, other.t))

    def __mul__(self, other):
        return Rel(self.x * other.x, self.s * other.s, self.t * other.t)

    def __truediv__(self, other):
        if other.x != 0:
            return Rel(self.x / other.x, self.s / other.s, self.t / other.t)
        else:
            raise ValueError("Division by zero in Rel system")

    def __pow__(self, power):
        return Rel(self.x ** power.x, self.s ** power.s, self.t ** power.t)

class RelMath:
    @staticmethod
    def sin(x):
        return Rel(math.sin(x.x), x.s, x.t)

    @staticmethod
    def cos(x):
        return Rel(math.cos(x.x), x.s, x.t)

    @staticmethod
    def tan(x):
        return Rel(math.tan(x.x), x.s, x.t)

    @staticmethod
    def sqrt(x):
        return Rel(math.sqrt(x.x), math.sqrt(x.s), math.sqrt(x.t))

    @staticmethod
    def exp(x):
        return Rel(math.exp(x.x), math.exp(x.s), math.exp(x.t))

    @staticmethod
    def log(x):
        return Rel(math.log(x.x), math.log(x.s), math.log(x.t))

class Onri:
    def __init__(self, f, i):
        self.f = max(0, min(f, 1))
        self.i = max(0, i)

    def __repr__(self):
        return f"Onri({self.f}, {self.i})"

    def value(self):
        return self.f * (1 - math.exp(-self.i))

    def __add__(self, other):
        return Onri(self.f + other.f, (self.i + other.i) / 2)

    def __sub__(self, other):
        return Onri(max(0.5, self.f - other.f), abs(self.i - other.i))

    def __mul__(self, other):
        return Onri(max(0.5, self.f * other.f), self.i * other.i)

    def __truediv__(self, other):
        if other.f != 0:
            return Onri(max(0.5, self.f / other.f), self.i / other.i)
        else:
            raise ValueError("Division by zero in Onri system")

    def __pow__(self, power):
        return Onri(self.f ** power.f, self.i ** power.i)

class OnriMath:
    @staticmethod
    def sin(x):
        return Onri(math.sin(x.f), x.i)

    @staticmethod
    def cos(x):
        return Onri(math.cos(x.f), x.i)

    @staticmethod
    def tan(x):
        return Onri(math.tan(x.f), x.i)

    @staticmethod
    def sqrt(x):
        return Onri(math.sqrt(x.f), math.sqrt(x.i))

    @staticmethod
    def exp(x):
        return Onri(math.exp(x.f), math.exp(x.i))

    @staticmethod
    def log(x):
        return Onri(math.log(x.f), math.log(x.i))

# Utility functions (similar to numpy and pygame)
class SakUtil:
    @staticmethod
    def array(values):
        return [Sak(v) for v in values]

    @staticmethod
    def random(low, high):
        return Sak(random.uniform(low, high))

class RelUtil:
    @staticmethod
    def array(values):
        return [Rel(v, 1, 1) for v in values]

    @staticmethod
    def random(low, high):
        return Rel(random.uniform(low, high), 1, 1)

class OnriUtil:
    @staticmethod
    def array(values):
        return [Onri(v, 1) for v in values]

    @staticmethod
    def random(low, high):
        return Onri(random.uniform(low, high), 1)

# Encryption and decryption functions
def encrypt_sak(sak, key):
    value = int((sak.value - 0.5) * 1000)
    encrypted = value ^ key
    return encrypted

def decrypt_sak(encrypted, key):
    decrypted = encrypted ^ key
    return Sak(decrypted / 1000 + 0.5)

def encrypt_rel(rel, key):
    x = int(rel.x * 1000)
    s = int(rel.s * 1000)
    t = int(rel.t * 1000)
    encrypted = (x ^ key, s ^ key, t ^ key)
    return encrypted

def decrypt_rel(encrypted, key):
    x, s, t = encrypted
    return Rel((x ^ key) / 1000, (s ^ key) / 1000, (t ^ key) / 1000)

def encrypt_onri(onri, key):
    f = int(onri.f * 1000)
    i = int(onri.i * 1000)
    encrypted = (f ^ key, i ^ key)
    return encrypted

def decrypt_onri(encrypted, key):
    f, i = encrypted
    return Onri((f ^ key) / 1000, (i ^ key) / 1000)

# Integration functions
def sak_to_rel(sak):
    return Rel(Sak.inverse(sak), 1, 1)

def rel_to_sak(rel):
    return Sak(rel.x)

def sak_to_onri(sak):
    return Onri(Sak.inverse(sak), 1)

def onri_to_sak(onri):
    return Sak(onri.value())

def rel_to_onri(rel):
    return Onri(rel.x, rel.s * rel.t)
