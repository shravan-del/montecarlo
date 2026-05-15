import numpy as np

def metropolis_step(hamiltonian, config, T):
    N = config.N

    for i in range(N):
        current_energy = hamiltonian.energy(config)

        config.flip(i)

        new_energy = hamiltonian.energy(config)

        delta_E = new_energy - current_energy

        if delta_E > 0:
            probability = np.exp(-delta_E / T)

            if np.random.rand() > probability:
                config.flip(i)

    return config


def run_simulation(hamiltonian, config, T, steps=1000):
    energies = []
    magnetizations = []

    for _ in range(steps):
        metropolis_step(hamiltonian, config, T)

        energies.append(hamiltonian.energy(config))
        magnetizations.append(config.magnetization())

    return energies, magnetizations
