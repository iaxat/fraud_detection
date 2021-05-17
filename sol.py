# testing of input data
# testing of data arrangement

def data_collector():
    input_data = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
    graph_dict = {'A':[],'B':[],'C':[],'D':[],'E':[]}
    temp_cal = 0

    for i in input_data:
        temp_str = i[1]+i[2]
        if i[0] in graph_dict:
            graph_dict[i[0]].append(temp_str)

    print(graph_dict)
    # soltiuon for question
    # 1 to 5
    find_results = ['ABC']
    



data_collector()