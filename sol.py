# testing of input data
# testing of data arrangement

def data_collector():
    input_data = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
    graph_dict = {'A':[],'B':[],'C':[],'D':[],'E':[]}

    stops = 0

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
                else:
                    print("NA")            
            else:
                print("NA")
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
                else:
                    print("NA")            
            else:
                print("NA")
    else:
        print("NA")

    print('Output 1. A-D-C ->',temp_cal)


    # 4. AEBCD
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

                        else:
                            print("NA")
                else:
                    print("NA")            
            else:
                print("NA")
    else:
        print("NA")

    print('Output 1. A-E-D ->',temp_cal)


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

                        else:
                            print("NA")
                else:
                    print("NA")            
            else:
                print("NA")
    else:
        print("NA")

    print('Output 1. A-E-D ->',temp_cal)

data_collector()