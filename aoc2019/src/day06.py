import networkx as nx
import matplotlib.pyplot as plt

from common.util import read_input


def generate_graph(orbit_map):
    graph = nx.Graph()
    edges = [orbit.split(')') for orbit in orbit_map]
    graph.add_edges_from(edges)
    return graph


def calculate_min_transfers(orbit_map, source, target):
    return nx.shortest_path_length(generate_graph(orbit_map), source, target) - 2


def calculate_orbits(orbit_map):
    return sum(dict.values(nx.shortest_path_length(generate_graph(orbit_map), 'COM')))


def main():
    orbit_map = read_input('input', separator='\n')
    print('Answer for Day6 - Part 1: {}'.format(calculate_orbits(orbit_map)))
    print('Answer for Day6 - Part 2: {}'.format(calculate_min_transfers(orbit_map, 'YOU', 'SAN')))


if __name__ == "__main__":
    main()
