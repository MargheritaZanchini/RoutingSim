from routing_table import RoutingTable
class Router:
    def __init__(self, name):
        self.name = name
        self.neighbors = {} #dictionary of neighbors with the cost of the connection
        self.my_table = RoutingTable() #routing table of the router
        self.my_table.add_route(self.name, 0, self.name) #add the router to its own routing table
        self.position = (0, 0) #position of the router in the GUI

    #addition of a neighbor to the router
    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost 
        self.my_table.add_route(neighbor.name, cost, neighbor.name)

    #update the distance vector of the router with the Dv of the neighbors
    def update_distance_vector(self) -> bool:
        update = False
        for router in self.neighbors:
            neighbor_distance_vector = router.get_distance_vector() #takes the DV of the neighbor
            for destination, cost in neighbor_distance_vector.items():
                if destination in self.my_table.table: #chek if the destination is already in the routing table
                    if self.my_table.table[destination][0] > cost[0] + self.neighbors[router]: #if it is in the table check if the new cost is lower
                        self.my_table.add_route(destination, cost[0] + self.neighbors[router], router.name) #updates the routing table if the new cost is lower
                        update = True
                else: #if the destination is not in the table add it
                    self.my_table.add_route(destination, cost[0] + self.neighbors[router], router.name)    
                    update = True    
        return update

    #return the distance vector of the router, so the neighbors can see it
    def get_distance_vector(self):
        return self.my_table.table
    
    #set the position of the router in the GUI
    def set_position(self, x, y):
        self.position = (x, y)

    def __str__(self):
        str = ""
        for router in self.neighbors:
            str = ""+ str + " { " + router.name + f" -> {self.neighbors[router]} " + " } "

        return f"Router {self.name}: neighbors: {str} \nrouting table: {self.my_table.table}\n"



