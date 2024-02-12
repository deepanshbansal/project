from datetime import datetime

def duration(each_user,start_list,end_list):
    total_time = 0
    total_iter = 0
    for i in range(len(start_list)):
        start_time = datetime.strptime(start_list[i]['Start'], "%H:%M:%S")
        end_time = datetime.strptime(end_list[i]['End'], "%H:%M:%S")
        total_iter += 1
        total_time += (end_time- start_time).seconds

    print(each_user, total_iter, total_time)
    
