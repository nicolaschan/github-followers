import networkx as nx
import matplotlib.pyplot as plt
import requests
from time import sleep

G = nx.Graph()
options = {
        'node_color': 'cyan',
        'node_size': 100,
        'width': 1,
        'with_labels': True,
        'edge_color': 'gray'
}

auth = ('', '')

def github_api(path):
    return requests.get('https://api.github.com{}'.format(path), auth=auth).json()

def add_connections(user, graph, seen=set(), depth=0):
    if depth == 0:
        return
    if user in seen:
        return

    print('Looking up', user)
    seen.add(user)
    followers = github_api('/users/{}/followers'.format(user))
    following = github_api('/users/{}/following'.format(user))

    connections = set()
    for follower in followers:
        connections.add(follower['login'])
    for follow in following:
        connections.add(follow['login'])

    graph.add_node(user)
    for connection in connections:
        graph.add_node(connection)
        graph.add_edge(user, connection)
        add_connections(connection, graph, seen=seen, depth=depth - 1)

add_connections('username', G, depth=2)
print('Drawing')

nx.draw(G, **options)
plt.show()
