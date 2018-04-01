from neighbor import neighbor

class item:

    def __init__(self, value, neighbors):
        self.value = value
        self.neighbors = neighbors

    def print_info(self):
        print("Value: " + str(self.value))

        n = self.neighbors
        while n != None:
            n.print_info()
            n = n.next

    def add_neighbor(self, neighbor):
        if self.neighbors == None:
            self.neighbors = neighbor
        else:
            head = self.neighbors
            while (self.neighbors.next != None):
                self.neighbors = self.neighbors.next
            self.neighbors.next = neighbor
            self.neighbors = head
            

        
            
                
