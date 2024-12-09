class Edge:
    def __init__ (self, router1, router2, cost):
        self.router1 = router1
        self.router2 = router2
        self.cost = cost
    
    def __str__ (self):
        return f"{self.router1.name} -- {self.router2.name} : {self.cost}"