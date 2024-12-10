from router import Router
from GUI import GUI
import random

routers = [] #array of all routers
#n_routers = random.randint(3, 8) #random number of routers between 3 and 10

#function to create a random network
def create_random_network():
    n_routers = random.randint(3, 8) #random number of routers between 3 and 10
    print(f"Random number of routers: {n_routers}")

    for i in range(n_routers):
        routers.append(Router(chr(65+i))) #creation of the routers

    # Create edges
    n_edge = random.randint(n_routers-1, (n_routers*(n_routers-1))/2)  #random number of edges

    #matrix that indicates where I already have an edge
    mat_edges = [[0 for _ in range(n_routers)] for _ in range(n_routers)] 
    print(f"number of edge: {n_edge}")

    #routers that are not connected to any other router
    routers_not_connected = routers.copy()

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
        routers[r1].add_neighbor(routers[r2], cost)
        routers[r2].add_neighbor(routers[r1], cost)
        if(routers[r1] in routers_not_connected):
            routers_not_connected.remove(routers[r1]) 
        
        if(routers[r2] in routers_not_connected):
            routers_not_connected.remove(routers[r2]) 


    #checking if there are routers without connection
    if (routers_not_connected.count != 0):
        #if there are routers without connection, I will connect them to a random router
        for router in routers_not_connected:
            r2 = random.choice(routers)
            while router == r2:
                r2 = random.choice(routers)
            cost = random.randint(1, 10)
            router.add_neighbor(r2, cost)
            r2.add_neighbor(router, cost)
            


#function to create a network that I know the result
def create_network():
    routers.append(Router('A'))
    routers.append(Router('B'))
    routers.append(Router('C'))
    routers.append(Router('D'))
    routers.append(Router('E'))
    routers.append(Router('F'))

    routers[0].add_neighbor(routers[1], 1) 
    routers[0].add_neighbor(routers[2], 10) 
    routers[1].add_neighbor(routers[0], 1)
    routers[1].add_neighbor(routers[2], 8)
    routers[1].add_neighbor(routers[3], 3)
    routers[2].add_neighbor(routers[0], 10)
    routers[2].add_neighbor(routers[1], 8)
    routers[2].add_neighbor(routers[4], 1)
    routers[2].add_neighbor(routers[5], 9)
    routers[3].add_neighbor(routers[1], 3)
    routers[3].add_neighbor(routers[4], 2)
    routers[4].add_neighbor(routers[2], 1)
    routers[4].add_neighbor(routers[3], 2)
    routers[5].add_neighbor(routers[2], 9)

    #I created this network to test the algorithm:
    #Router A: {} neighbors: {'B': 1, 'C': 10}
    #Router B: {} neighbors: {'A': 1, 'C': 8, 'D': 3}
    #Router C: {} neighbors: {'A': 10, 'B': 8, 'E': 1, 'F' : 9}
    #Router D: {} neighbors: {'B': 3, 'E': 2}
    #Router E: {} neighbors: {'C': 1, 'D': 2}
    #Router F: {} neighbors: {'C': 9}


def distance_vector_routing() -> bool:
    #every roueter updates his DV
    update = False
    for router in routers:
        if(router.update_distance_vector()): 
            update = True #update is true if at least one DV changed
    return update
    

def main():
    create_random_network()
    #create_network()
    update = True #if it's false the DV of the routers are not changing
    print ("The routers only know the neighbors\n")
    for router in routers:
        print(router)
    
    while(update): #update the DV of every router until tehre is no changing
        #print(" sto ciclando")
        update = distance_vector_routing()
    
    print("optimal routing table: \n")
    for router in routers:
        print(router)


if __name__ == "__main__":
    main()
    app = GUI(routers)