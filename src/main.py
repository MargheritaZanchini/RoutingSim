from router import Router
from edge import Edge
import random

routers = [] #array of all routers

#function to create a random network
def createRandomNetwork():
    nRouters = random.randint(3, 4) #random number of routers
    print(f"Random number of routers: {nRouters}")

    for i in range(nRouters):
        routers.append(Router(chr(65+i))) #creation of the routers

    # Create edges
    nEdge = random.randint(nRouters-1, (nRouters*(nRouters-1))/2)  #random number of edges

    #matrix that indicates where I already have an edge
    matEdges = [[0 for _ in range(nRouters)] for _ in range(nRouters)] 
    print(f"number of edge: {nEdge}")

    #routers that are not connected to any other router
    routersNotConnected = routers.copy()

    for i in range(nEdge):
        #selecting two random routers
        r1 = random.randint(0, nRouters-1)
        r2 = random.randint(0, nRouters-1)
        #checking if the routers are the same or the enge already exists
        while r1 == r2 or matEdges[r1][r2] == 1 or matEdges[r2][r1] == 1:
            r1 = random.randint(0, nRouters-1)
            r2 = random.randint(0, nRouters-1)
        matEdges[r1][r2] = 1
        matEdges[r2][r1] = 1
        cost = random.randint(1, 10)
        
        #creating the edge between the routers
        routers[r1].addNeighbor(routers[r2].name, cost)
        routers[r2].addNeighbor(routers[r1].name, cost)
        if(routers[r1] in routersNotConnected):
            routersNotConnected.remove(routers[r1]) 
        
        if(routers[r2] in routersNotConnected):
            routersNotConnected.remove(routers[r2]) 


    #checking if there are routers without connection
    if (routersNotConnected.count != 0):
        #if there are routers without connection, I will connect them to a random router
        for router in routersNotConnected:
            r2 = random.choice(routers)
            while router == r2:
                r2 = random.choice(routers)
            cost = random.randint(1, 10)
            router.addNeighbor(r2, cost)
            r2.addNeighbor(router, cost)
            

#function to create a network that I know the result
def createNetwork():
    routers.append(Router('A'))
    routers.append(Router('B'))
    routers.append(Router('C'))
    routers.append(Router('D'))
    routers.append(Router('E'))

    routers[0].addNeighbor('B', 1)
    routers[0].addNeighbor('C', 2)
    routers[1].addNeighbor('A', 1)
    routers[1].addNeighbor('C', 8)
    routers[1].addNeighbor('D', 5)
    routers[2].addNeighbor('A', 2)
    routers[2].addNeighbor('B', 8)
    routers[2].addNeighbor('E', 7)
    routers[3].addNeighbor('B', 5)
    routers[3].addNeighbor('E', 2)
    routers[4].addNeighbor('C', 7)
    routers[4].addNeighbor('D', 2)

    #I created this network to test the algorithm:
    #Router A: {} neighbors: {'B': 1, 'C': 2}
    #Router B: {} neighbors: {'A': 1, 'C': 8, 'D': 5}
    #Router C: {} neighbors: {'A': 2, 'B': 8, 'E': 7}
    #Router D: {} neighbors: {'B': 5, 'E': 2}
    #Router E: {} neighbors: {'C': 7, 'D': 2}

def main():
    createRandomNetwork()
    #createNetwork()
    for router in routers:
        print(router)


    # Simulate distance vector updates
    #routers = [router_a, router_b, router_c]
    #updated = True
    #while updated:
    #    updated = False
    #    for router in routers:
    #        for neighbor_name in router.neighbors:
    #            neighbor_router = next(r for r in routers if r.name == neighbor_name)
    #            if router.update_distance_vector(neighbor_name, neighbor_router.distance_vector):
    #                updated = True


if __name__ == "__main__":
    main()