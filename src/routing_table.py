import sys
class RoutingTable:
    def __init__(self):
        self.table = {}

    #add a route to the routing table
    def add_route(self, destination, cost, next_hop):
        self.table[destination] = (cost, next_hop)
