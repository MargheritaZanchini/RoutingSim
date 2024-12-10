import random
from router import Router

class Network:
    def __init__ (self):
        self.routers = []
    
    #function to create a random network
    def create_random_network(self) -> list:
        n_routers = random.randint(3, 8) #random number of routers between 3 and 10
        print(f"Random number of routers: {n_routers}")

        for i in range(n_routers):
            self.routers.append(Router(chr(65+i))) #creation of the routers

        # Create edges
        n_edge = random.randint(n_routers-1, (n_routers*(n_routers-1))/2)  #random number of edges

        #matrix that indicates where I already have an edge
        mat_edges = [[0 for _ in range(n_routers)] for _ in range(n_routers)] 
        print(f"number of edge: {n_edge}")

        #routers that are not connected to any other router
        routers_not_connected = self.routers.copy()

        for i in range(n_edge):
            #selecting two random routers
            r1 = random.randint(0, n_routers-1)
            r2 = random.randint(0, n_routers-1)
            #checking if the routers are the same or the enge already exists
            while r1 == r2 or mat_edges[r1][r2] == 1 or mat_edges[r2][r1] == 1:
                r1 = random.randint(0, n_routers-1)
                r2 = random.randint(0, n_routers-1)
            mat_edges[r1][r2] = 1
            mat_edges[r2][r1] = 1
            cost = random.randint(1, 10)

            #creating the edge between the routers
            self.routers[r1].add_neighbor(self.routers[r2], cost)
            self.routers[r2].add_neighbor(self.routers[r1], cost)
            if(self.routers[r1] in routers_not_connected):
                routers_not_connected.remove(self.routers[r1]) 

            if(self.routers[r2] in routers_not_connected):
                routers_not_connected.remove(self.routers[r2]) 


    #checking if there are routers without connection
        if (routers_not_connected.count != 0):
            #if there are routers without connection, I will connect them to a random router
            for router in routers_not_connected:
                r2 = random.choice(self.routers)
                while router == r2:
                    r2 = random.choice(self.routers)
                cost = random.randint(1, 10)
                router.add_neighbor(r2, cost)
                r2.add_neighbor(router, cost)

        return self.routers
            

#function to create a network that I know the result
    def create_network(self) -> list:
        self.routers.append(Router('A'))
        self.routers.append(Router('B'))
        self.routers.append(Router('C'))
        self.routers.append(Router('D'))
        self.routers.append(Router('E'))
        self.routers.append(Router('F'))

        self.routers[0].add_neighbor(self.routers[1], 1) 
        self.routers[0].add_neighbor(self.routers[2], 10) 
        self.routers[1].add_neighbor(self.routers[0], 1)
        self.routers[1].add_neighbor(self.routers[2], 8)
        self.routers[1].add_neighbor(self.routers[3], 3)
        self.routers[2].add_neighbor(self.routers[0], 10)
        self.routers[2].add_neighbor(self.routers[1], 8)
        self.routers[2].add_neighbor(self.routers[4], 1)
        self.routers[2].add_neighbor(self.routers[5], 9)
        self.routers[3].add_neighbor(self.routers[1], 3)
        self.routers[3].add_neighbor(self.routers[4], 2)
        self.routers[4].add_neighbor(self.routers[2], 1)
        self.routers[4].add_neighbor(self.routers[3], 2)
        self.routers[5].add_neighbor(self.routers[2], 9)

        #I created this network to test the algorithm:
        #Router A: {} neighbors: {'B': 1, 'C': 10}
        #Router B: {} neighbors: {'A': 1, 'C': 8, 'D': 3}
        #Router C: {} neighbors: {'A': 10, 'B': 8, 'E': 1, 'F' : 9}
        #Router D: {} neighbors: {'B': 3, 'E': 2}
        #Router E: {} neighbors: {'C': 1, 'D': 2}
        #Router F: {} neighbors: {'C': 9}

        return self.routers

        