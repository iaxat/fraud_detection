# testing of input data
# testing of data arrangement

def data_collector():
    input_data = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
    graph_dict = {'A':[],'B':[],'C':[],'D':[],'E':[]}
    temp_cal = 0
    stops = 0

    for i in input_data:
        temp_str = i[1]+i[2]
        if i[0] in graph_dict:
            graph_dict[i[0]].append(temp_str)

    print(graph_dict)
    # soltiuon for question
    # 1 ABC
    if 'A' in graph_dict.keys():
        for k in graph_dict['A']:
            
            if 'B' in k:
                list(k)
                temp_cal += int(k[1])

                if 'B' in graph_dict.keys():
                    for k in graph_dict['B']:
                        
                        if 'C' in k:
                            list(k)
                            temp_cal += int(k[1])

    print('Output 1. A-B-C',temp_cal)

    
            


data_collector()