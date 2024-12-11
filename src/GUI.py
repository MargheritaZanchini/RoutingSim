import tkinter as tk
import math
class GUI:
    def __init__(self, routers):
        self.routers = routers
        self.number_of_steps = 0
        self.update = True
        window = tk.Tk() #creates the window
        window.title("Routing Table Viewer")

        # Canvas for the network
        canvas = tk.Canvas(window, width=500, height=500, bg="lightgray")
        canvas.grid(row=0, column=0, padx=10, pady=10)
        
        # draw the routers with circles in a circular layout
        center_x, center_y = 250, 250
        radius = 150
        num_routers = len(routers)
        angle_step = 2 * math.pi / num_routers

        for i, router in enumerate(routers):
            angle = i * angle_step
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            canvas.create_oval(x-20, y-20, x+20, y+20, fill="white", outline="black", tags="router")
            canvas.create_text(x, y, text=router.name, font=('Helvetica', 12), tags="routerText")
            router.set_position(x, y)

        # draw the connections between the routers
        drawn_edges = set()
        for router in routers:
            for neighbor in router.neighbors:
                edge = tuple(sorted((router.name, neighbor.name)))
                if edge not in drawn_edges:
                    x1, y1 = router.position
                    x2, y2 = neighbor.position
                    canvas.create_line(x1, y1, x2, y2, tags="line")
                    offsetx = 10 if x1 < x2 else -10
                    offsety = 10 if y1 < y2 else -10
                    canvas.create_text((x1+x2)/2 + offsetx, (y1+y2)/2 + offsety, text=router.neighbors[neighbor], font=('Helvetica', 12), fill="red", tags="cost")
                    drawn_edges.add(edge)

        # Raise the routers above the lines
        canvas.tag_raise("router")
        canvas.tag_raise("routerText")


        # Text Area for the routing tables
        self.textArea = tk.Text(window, height=20, width=50)
        self.textArea.grid(row=0, column=1, padx=10, pady=10)
        self.print_routing_tables()

        # Button to go to the next step
        self.button_next = tk.Button(window, text="Next Step (Click Here)", command=self.distance_vector_routing)
        self.button_next.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        

        # starts the GUI
        window.mainloop()

    #function called when the button is clicked, it updates the distance vector of all routers
    def distance_vector_routing(self):
        self.number_of_steps += 1
        #every roueter updates his DV
        self.update = False
        for router in self.routers:
            if(router.update_distance_vector()): 
                self.update = True #update is true if at least one DV changed
        self.print_routing_tables()
        if(not self.update):
           self.button_next.config(state=tk.DISABLED)

    #function to print the routing tables of all routers
    def print_routing_tables(self):
        self.textArea.config(state=tk.NORMAL)
        self.textArea.delete('1.0', tk.END)
        self.textArea.insert(tk.END, f"Routing Table at step {self.number_of_steps} \n\n")
        if(not self.update):
            self.textArea.insert(tk.END, "These are the optimal routing tables\nfor this network: \n\n")
        # write the routing table of each router
        for router in self.routers:
            self.textArea.insert(tk.END, f"Router {router.name}\n")
            self.textArea.insert(tk.END, "Destination\t\tCost\t\tNext Hop\n")
            for dest, cost in router.my_table.table.items():
                self.textArea.insert(tk.END, f"{dest}\t\t{cost[0]}\t\t{cost[1]}\n")
            self.textArea.insert(tk.END, "\n")
        self.textArea.config(state=tk.DISABLED)