from duration import duration
from datetime import datetime
from process_data import preprocess_time,preprocess_name


def preprocess_data(filepath):
    log_data=dict()
    total_list=list()
    with open(filepath,"r") as file:
        for each_data in file:
            each_row = each_data.strip().split()
            each_row[0] = preprocess_time(each_row[0])
            total_list.append(each_row)
        start_time = total_list[0][0]
        end_time = total_list[-1][0]
        for each_data in total_list:
            if 3 >= len(each_data) > 2 and preprocess_name(each_data[1]):
                if each_data[1] in log_data:
                        if each_data[2] == "End" or each_data[2] == "Start":
                            log_data[each_data[1]].append({each_data[2]:each_data[0]})
                else:
                    if each_data[2] == "End":
                        log_data[each_data[1]]=[{"Start":start_time}]
                        log_data[each_data[1]].append({each_data[2]:each_data[0]})
                    else:
                        if each_data[2] == "Start":
                            log_data[each_data[1]]=[{each_data[2]:each_data[0]}]
            
    return log_data,start_time,end_time






def refactor_data(user_dict,start_time,end_time):
    for each_user in user_dict:
        data = user_dict[each_user]
        start_list=list()
        end_list=list()
        sorted_data = sorted(data, key=lambda x: 'Start' not in x)
        for each_key in sorted_data:
            if "Start" in each_key:
                start_list.append(each_key)
            else:
                end_list.append(each_key)

        if len(start_list) < len(end_list):
            while len(start_list) < len(end_list):
                start_list.append({"Start":start_time})
        elif len(end_list) < len(start_list):
            while len(end_list) < len(start_list):
                end_list.append({"End":end_time})

        duration(each_user,start_list,end_list)


file_path = input("Enter file path :")
response,start_time,end_time = preprocess_data(file_path)
refactor_data(response,start_time,end_time)
