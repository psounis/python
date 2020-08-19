from graph import Graph
from queue import Queue


def breadth_first_search(graph, start, finish):
    q = Queue()
    discovered = [start]
    q.enqueue(start)
    parent = {}
    while len(q) > 0:
        v = q.dequeue()
        if v == finish:
            break
        for neighbor in graph.neighbors(v):
            if neighbor.descr not in discovered:
                discovered += [neighbor.descr]
                parent[neighbor.descr] = v
                q.enqueue(neighbor.descr)

    path = [finish]
    while path[0] != start:
        path = [parent[path[0]]] + path

    print(path)


def main():
    facebook_users = Graph()
    for user in ["Bob", "Anne", "Elisa", "Diana", "Carl"]:
        facebook_users.add_vertex(user)

    facebook_users.add_edge("Carl", "Bob")
    facebook_users.add_edge("Carl", "Elisa")
    facebook_users.add_edge("Carl", "Diana")
    facebook_users.add_edge("Diana", "Bob")
    facebook_users.add_edge("Diana", "Anne")
    facebook_users.add_edge("Elisa", "Anne")
    facebook_users.add_edge("Anne", "Bob")
    print(facebook_users)
    print("\n")
    breadth_first_search(facebook_users, "Carl", "Anne")


main()