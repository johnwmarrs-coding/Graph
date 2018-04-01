from item import item
from neighbor import neighbor

class graph:


    def __init__(self, nodes, name):
        self.nodes = nodes
        self.name = name


    def get_nodes_in_range(self, from_node, target_depth, current_depth, reached_nodes):
        if current_depth > 0:
            reached_nodes.append(from_node)

        #print("Iterated over " + str(from_node.value))
        #print(reached_nodes)
        neigh = from_node.neighbors
        print(neigh)
        while (neigh != None and current_depth < target_depth):
            next_node = neigh.objectTo
            reached_nodes.extend( self.get_nodes_in_range(next_node, target_depth, current_depth+1, reached_nodes))
            neigh = neigh.next

        reached_nodes = set(reached_nodes)
        reached_nodes = list(reached_nodes)
        return reached_nodes

    def get_nodes_in_weight_range(self, from_node, target_depth, current_depth, reached_nodes):
        if (current_depth > 0):
            reached_nodes.append(from_node)

        neigh = from_node.neighbors
        while (neigh != None and current_depth < target_depth):
            next_node = neigh.objectTo
            reached_nodes.extend(self.get_nodes_in_weight_range(next_node, target_depth, current_depth + neigh.weight, reached_nodes))
            neigh = neigh.next

        reached_nodes = set(reached_nodes)
        reached_nodes = list(reached_nodes)
        return reached_nodes





#to generalize the process of graph creation
#-------------------------------------------
#Make n nodes
#Make n neighbors in the form -> n_item = neighbor(1, item[n], None)
#Append neighbors to desired items (From user info)

# FILE TYPE FOR GRAPH DESIGN
# LineNum  Purpose     Format
# 0        Graph Name  String
# 1        Type        unidirectional/bidirectional
# 2        Node Name   String
# 3        .
# 4        .
# 5        .
# 6        Edges       String, String   $Names from and to
# 7        .
# 8        .
# n        .

def generate_graph_from_txt(file_path):
    nodes = []
    f = open(file_path)
    print(f)
    content = list(f)
    for i in range(0, len(content)):
        content[i] = content[i].strip()

    name = content[0]
    if (content[1].lower() == 'unidirectional'):
        i = 2
        indexDictionary = {}
        while ',' not in content[i]:
            nodes.append(item(content[i], None))
            indexDictionary[content[i]] = i-2
            i = i+1

        while(',' in content[i]):

            from_node = content[i][0: content[i].index(',')]
            to_node = content[i][content[i].index(',')+1:len(content[i])]

            nodes[indexDictionary[from_node]].add_neighbor(neighbor(1,nodes[indexDictionary[to_node]]))

            i = i + 1
            if i == len(content):
                break
                ### NEED TO FINISH THE NEIGHBOR PART OF THIS
        #print("Finished Theoretically")
        #print(nodes)
                           
    elif (content[1].lower() == 'bidirectional'):

        i = 2
        indexDictionary = {}
        while ',' not in content[i]:
            nodes.append(item(content[i], None))
            indexDictionary[content[i]] = i - 2
            i = i + 1

        while (',' in content[i]):

            from_node = content[i][0: content[i].index(',')]
            to_node = content[i][content[i].index(',') + 1:len(content[i])]

            nodes[indexDictionary[from_node]].add_neighbor(neighbor(1, nodes[indexDictionary[to_node]]))
            nodes[indexDictionary[to_node]].add_neighbor(neighbor(1, nodes[indexDictionary[from_node]]))

            i = i + 1
            if i == len(content):
                break
                ### NEED TO FINISH THE NEIGHBOR PART OF THIS
        # print("Finished Theoretically")
        # print(nodes)

    f.close()
    print(nodes)
    return graph(nodes, name)
        
    

def main():
    g = generate_graph_from_txt('graphs/test0.txt')

    n = g.nodes[0]

    ns = g.get_nodes_in_range(n,2,0, [])

    for item in ns:
        print(item.value)

    
#If this function is run standalone, the __name__ variable will be set to __main__ and run the main function
#If this functino is called by another program, the function will not run
if __name__ == "__main__":
    main()
