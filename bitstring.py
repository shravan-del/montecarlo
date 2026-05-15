import numpy as np

class BitString:
    def __init__(self, N):
        self.N = N
        self.spins = np.random.choice([-1, 1], size=N)

    def flip(self, i):
        self.spins[i] *= -1

    def magnetization(self):
        return np.sum(self.spins)

    def copy(self):
        new_copy = BitString(self.N)
        new_copy.spins = self.spins.copy()
        return new_copy

    def __str__(self):
        return str(self.spins)
