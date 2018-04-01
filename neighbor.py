class neighbor:


    def __init__(self, weight, objectTo):
        self.next = None
        self.weight = weight
        self.objectTo = objectTo

    def print_info(self):
        print("-----Next object is:")
        print("-----" + str(self.objectTo.value))
        print("-----Weight: " + str(self.weight))


        
