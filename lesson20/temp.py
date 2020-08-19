from queue import Queue


class Node:
    def __init__(self, descr="", neighbors=None):
        self.descr = descr
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors


class Graph:
    def __init__(self):
        self.nodes=[]

    def add_vertex(self, descr="", neighbors=None):
        if neighbors is None:
            neighbors = []
        self.nodes.append(Node(descr, neighbors))

    def index_of(self, descr):
        for i in range(len(self.nodes)):
            if descr == self.nodes[i].descr:
                return i
        return -1

    def add_edge(self, descr1, descr2):
        index1 = self.index_of(descr1)
        index2 = self.index_of(descr2)
        self.nodes[index1].neighbors.append(self.nodes[index2])
        self.nodes[index2].neighbors.append(self.nodes[index1])

    def neighbors(self, descr):
        return self.nodes[self.index_of(descr)].neighbors

    def __str__(self):
        st = ""
        for node in self.nodes:
            st += f"\n{node.descr}: "
            for neighbor in node.neighbors:
                st += f"{neighbor.descr} "
        return st


def breadth_first_search(graph, start, finish):
    q = Queue()
    discovered = [start]
    q.enqueue(start)
    parent = {}
    while len(q)>0:
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

    facebook_users.add_edge("Carl", "Diana")
    facebook_users.add_edge("Carl", "Elisa")
    facebook_users.add_edge("Carl", "Bob")
    facebook_users.add_edge("Diana", "Bob")
    facebook_users.add_edge("Diana", "Anne")
    facebook_users.add_edge("Elisa", "Anne")
    facebook_users.add_edge("Anne", "Bob")
    print(facebook_users)
    breadth_first_search(facebook_users, "Anne", "Diana")


main()
