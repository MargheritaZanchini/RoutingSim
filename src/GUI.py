import tkinter as tk
import math

class GUI:
    # Funzione per creare la finestra
    def __init__(self, routers):
        self.router = routers
        window = tk.Tk()
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


        textArea = tk.Text(window, height=20, width=50)
        textArea.grid(row=0, column=1, padx=10, pady=10)
        textArea.insert(tk.END, "Routing Table\n")
        
        # write the routing table of each router
        for router in routers:
            textArea.insert(tk.END, f"Router {router.name}\n")
            textArea.insert(tk.END, "Destination\t\tCost\t\tNext Hop\n")
            for dest, cost in router.my_table.table.items():
                textArea.insert(tk.END, f"{dest}\t\t{cost[0]}\t\t{cost[1]}\n")
            textArea.insert(tk.END, "\n")
        textArea.config(state=tk.DISABLED)
        

        # starts the GUI
        window.mainloop()