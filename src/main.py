from router import Router
from network import Network
from GUI import GUI

def main():
    global routers  #array of all routers
    network = Network()

    # comment the second line and uncomment the first line to create a random network
    #routers = network.create_random_network()
    routers = network.create_network()


if __name__ == "__main__":
    main()
    app = GUI(routers)