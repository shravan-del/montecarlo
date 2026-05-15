# Monte Carlo Package

This project implements Monte Carlo simulations for arbitrary Ising Hamiltonians.

## Features

- Ising Hamiltonian simulations
- Thermodynamic averages
- Magnetization calculations
- Metropolis Monte Carlo sampling

## Installation

```bash
pip install .
```

## Usage

```python
import networkx as nx
from montecarlo import BitString, IsingHamiltonian

G = nx.Graph()
G.add_edge(0, 1, weight=1.0)

conf = BitString(2)
ham = IsingHamiltonian(G)

E, M, HC, MS = ham.compute_average_values(T=1)

print(E, M, HC, MS)
```
