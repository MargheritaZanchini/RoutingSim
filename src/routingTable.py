class RoutingTable:
    def __init__(self):
        self.table = {}

    def addRoute(self, destination, cost, next_hop):
        self.table[destination] = (cost, next_hop)