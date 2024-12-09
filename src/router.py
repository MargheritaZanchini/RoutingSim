class Router:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.distance_vector = {}

    def addNeighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost
        #self.distance_vector[neighbor] = cost

    #def update_distance_vector(self, neighbor, neighbor_distance_vector):
    #    updated = False
    #    for dest, cost in neighbor_distance_vector.items():
    #        if dest not in self.distance_vector or self.distance_vector[dest] > self.neighbors[neighbor] + cost:
    #            self.distance_vector[dest] = self.neighbors[neighbor] + cost
    #            updated = True
    #    return updated

    def __str__(self):
        return f"Router {self.name}: {self.distance_vector} neighbors: {self.neighbors}"



