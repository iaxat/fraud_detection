# testing of input data
# testing of data arrangement

from typing import SupportsRound


def data_collector():
    input_data = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
    graph_dict = {'A':[],'B':[],'C':[],'D':[],'E':[]}

    for i in input_data:
        temp_str = i[1]+i[2]
        if i[0] in graph_dict:
            graph_dict[i[0]].append(temp_str)

    print(graph_dict)


    # solution for question
    # 1 ABC
    temp_cal = 0
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
    else:
        print("NA")
    print('Output 1. A-B-C ->',temp_cal)


    # 2. AD
    temp_cal = 0
    if 'A' in graph_dict.keys():
        for k in graph_dict['A']:
            
            if 'D' in k:
                list(k)
                temp_cal += int(k[1])
    else:
        print("NA")
    print('Output 2. A-D ->',temp_cal)


    # 3. ADC
    temp_cal = 0
    if 'A' in graph_dict.keys():
        for k in graph_dict['A']:
            if 'D' in k:
                list(k)
                temp_cal += int(k[1])

                if 'D' in graph_dict.keys():
                    for k in graph_dict['D']:    
                        if 'C' in k:
                            list(k)
                            temp_cal += int(k[1])
    else:
        print("NA")
    print('Output 3. A-D-C ->',temp_cal)


    # 4. AEBCD
    temp_cal = 0
    if 'A' in graph_dict.keys():
        for k in graph_dict['A']:
            if 'E' in k:
                list(k)
                temp_cal += int(k[1])
                if 'E' in graph_dict.keys():
                    for k in graph_dict['E']:    
                        if 'B' in k:
                            list(k)
                            temp_cal += int(k[1])
                            if 'B' in graph_dict.keys():
                                for k in graph_dict['B']:    
                                    if 'C' in k:
                                        list(k)
                                        temp_cal += int(k[1])
                                        if 'C' in graph_dict.keys():
                                            for k in graph_dict['C']:    
                                                if 'D' in k:
                                                    list(k)
                                                    temp_cal += int(k[1])
                                                    print('Output 4. A-E-B-C-D ->',temp_cal)
                                                else:
                                                    print('Output 4. A-E-B-C-D -> no solution')
    

    # 5. AED
    temp_cal = 0
    if 'A' in graph_dict.keys():
        for k in graph_dict['A']:
            if 'E' in k:
                list(k)
                temp_cal += int(k[1])

                if 'E' in graph_dict.keys():
                    for k in graph_dict['E']:    
                        if 'D' in k:
                            list(k)
                            temp_cal += int(k[1])
                            print('Output 5. A-E-D ->',temp_cal)
                        else:
                            print('Output 5. A-E-D -> not a solution')


    # 6. Starting at C and ending at C
    graph_d = {'A': ['B', 'D', 'E'], 'B': ['C'], 'C': ['D', 'E'], 'D': ['C', 'E'], 'E': ['B']}
    source = 'A'
    if source is None or source not in graph_d:
        return "Invalid input"
    path = []
    stack = [source]
    while(len(stack) != 0):
        s = stack.pop()
        if s not in path:
            path.append(s)
        if s not in graph_d:
            #leaf node
            continue
        for neighbor in graph_d[s]:
            stack.append(neighbor)
    print(path)
    return " ".join(path)







    # 7. Trips from A to C








    # 8. A to C shortest route






    # 9. B to B 





    # 10. C to C trips with distance less than 30

data_collector()