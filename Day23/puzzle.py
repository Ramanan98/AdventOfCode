import networkx as nx

def build_graph():
    G = nx.Graph()
    with open('input.txt', 'r') as file:
        for line in file:
            node1, node2 = line.strip().split('-')
            G.add_edge(node1, node2)
    return G

def find_three_sets(graph):
    three_sets = [list(three_set) for three_set in nx.enumerate_all_cliques(graph) if len(three_set) == 3]
    return three_sets

def maximal_clique(graph):
    maximal_clique = max(nx.find_cliques(graph), key=len)
    return maximal_clique

def main():
    graph = build_graph()
    three_sets = find_three_sets(graph)
    largest_clique = maximal_clique(graph)

    count = 0
    for three_set in three_sets:
        if any(element.startswith('t') for element in three_set):
            count += 1
    print(count) # Part 1

    print(','.join(sorted(largest_clique))) # Part 2

if __name__ == "__main__":
    main()