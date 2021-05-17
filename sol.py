

# testing of input data
# testing of data arrangement


# function to define nodes
def path_finder():
    # node_req = input('A B C D E are available')
    graph_dict = {}
    input_data = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
    
    # creating path in dict
    # picking up the 1st letter for each array element
    for i in input_data:
        node_letter = i[0]
        # temp_str = i.split()
        temp_str = i[1]+i[2]
        print(temp_str)

        if node_letter in graph_dict.keys():
            graph_dict[node_letter].add(temp_str)
        else:
            graph_dict[node_letter] = temp_str

    print(graph_dict)
        # https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/



path_finder()