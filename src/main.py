from router import Router
from edge import Edge
import random

def main():
    # Create routers
    routers = []
    nRouters = random.randint(3, 8)
    print(f"Random number between 3 and 8: {nRouters}")

    for i in range(nRouters):
        routers.append(Router(chr(65+i)))

    # Create edges
    edges = []
    nEdge = random.randint(nRouters-1, (nRouters*(nRouters-1))/2)

    matEdges = [[0 for _ in range(nRouters)] for _ in range(nRouters)]
    print(f"number of edge: {nEdge}")

    routersNotConnected = routers.copy()

    for i in range(nEdge):
        r1 = random.randint(0, nRouters-1)
        r2 = random.randint(0, nRouters-1)
        while r1 == r2 or matEdges[r1][r2] == 1 or matEdges[r2][r1] == 1:
            r1 = random.randint(0, nRouters-1)
            r2 = random.randint(0, nRouters-1)
        matEdges[r1][r2] = 1
        matEdges[r2][r1] = 1
        edges.append(Edge(routers[r1], routers[r2], random.randint(1, 10)))
        if(routers[r1] in routersNotConnected):
            routersNotConnected.remove(routers[r1]) 
        
        if(routers[r2] in routersNotConnected):
            routersNotConnected.remove(routers[r2]) 


    if (routersNotConnected.count != 0):
        for router in routersNotConnected:
            r2 = random.choice(routers)
            while router == r2:
                r2 = random.choice(routers)
            edges.append(Edge(router, r2, random.randint(1, 10)))
            


    for router in routers:
        print(router)

    for edge in edges:
        print(edge)


    # Add neighbors
    #router_a.add_neighbor('B', 1)
    #router_a.add_neighbor('C', 4)
    #router_b.add_neighbor('A', 1)
    #router_b.add_neighbor('C', 2)
    #router_c.add_neighbor('A', 4)
    #router_c.add_neighbor('B', 2)

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