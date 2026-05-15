import numpy as np

class IsingHamiltonian:
    def __init__(self, graph):
        self.graph = graph
        self.mu = None

    def set_mu(self, mu):
        self.mu = mu

    def energy(self, config):
        E = 0

        for i, j in self.graph.edges:
            Jij = self.graph.edges[(i, j)].get('weight', 1.0)
            E += Jij * config.spins[i] * config.spins[j]

        if self.mu is not None:
            for i in range(config.N):
                E += self.mu[i] * config.spins[i]

        return E

    def compute_average_values(self, T, configs=100):
        energies = []
        magnetizations = []

        for _ in range(configs):
            spins = np.random.choice([-1, 1], size=self.graph.number_of_nodes())

            class TempConfig:
                pass

            conf = TempConfig()
            conf.spins = spins
            conf.N = len(spins)

            E = self.energy(conf)
            M = np.sum(spins)

            energies.append(E)
            magnetizations.append(M)

        E_avg = np.mean(energies)
        M_avg = np.mean(magnetizations)

        HC = (np.mean(np.square(energies)) - E_avg**2) / (T**2)
        MS = (np.mean(np.square(magnetizations)) - M_avg**2) / T

        return E_avg, M_avg, HC, MS
