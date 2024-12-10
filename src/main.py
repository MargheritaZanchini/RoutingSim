from router import Router
from network import Network
from GUI import GUI

#routers = [] # array of all routers

def main():
    global routers  # dichiarazione della variabile globale
    network = Network()

    # comment the second line and uncomment the first line to create a random network
    #routers = network.create_random_network()
    routers = network.create_network()


if __name__ == "__main__":
    main()
    app = GUI(routers)