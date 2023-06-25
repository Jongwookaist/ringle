import json
import sys
import datetime
import csv

if len(sys.argv) != 5:                           #인자 개수를 잘못준 경우 quit
    print("Please write length of class time, available class starting and ending time.")
    quit()

with open(sys.argv[1], 'r') as data:

    json_data = json.load(data)                      #json data 가져오기

    id_to_name = dict()                              #tutor id 랑 이름을 미리 dictionary로 저장해두기  id:name
    for i in range(len(json_data["tutors"])):
        id_to_name[json_data["tutors"][i]["id"]] = json_data["tutors"][i]["name"]
    
    time_length = int(sys.argv[2])//30               #학생이 원하는 수업 시간 길이(30분 단위)             
    start_time = datetime.datetime.fromisoformat(sys.argv[3]) #학생이 수업 시작 할 수 있는 시간
    end_time = datetime.datetime.fromisoformat(sys.argv[4])   #학생이 수업 끝내야 되는 시간

    tutor_dict = dict()                                  #선생님 id마다 start_time과 end_time 사이에 가능한 수업 시간이 start_time과 얼마나 떨어져있는지 저장
    for i in range (len(json_data["tutors"])):
        tutor_dict[(json_data["tutors"][i]['id'])] = []
    for k in range(len(json_data["slots"])):
        start_diff = (datetime.datetime.fromisoformat(json_data["slots"][k]["start_time"]) -start_time)
        end_diff = (datetime.datetime.fromisoformat(json_data["slots"][k]["start_time"]) -end_time)
        if start_diff == abs(start_diff) and end_diff != abs(end_diff):    #선생님의 수업 시간이 학생의 start time과 end time 사이인 경우
            tutor_dict[json_data["slots"][k]["tutor_id"]].append([json_data["slots"][k]["id"],json_data["slots"][k]["start_time"],start_diff.seconds//1800])
    answer_list = []
    #tutor_dict에 저장된 값 {'t1': [['s1', '2023-06-07T12:00:00Z', 24], ['s3', '2023-06-07T12:30:00Z', 25]], 't2': [['s2', '2023-06-07T12:00:00Z', 24]]}

    for i in range(len(json_data["tutors"])):                #선생님의 수업 가능한 시간이 unordered일 수 있으니 시간으로 sort 해주기
        tutor_id = json_data["tutors"][i]["id"]  #t1  t2
        tutor_dict[tutor_id].sort(key=lambda x: x[2])



    for i in range(len(json_data["tutors"])):
        tutor_id = json_data["tutors"][i]["id"]  #t1  t2
        consecutive_count = 0
        previous_slot = None
        first_time = None
        for k in range (len(tutor_dict[tutor_id])):
            if previous_slot is None: #tutor id 마다 처음
                first_time = [tutor_dict[tutor_id][k][0],tutor_dict[tutor_id][k][1],tutor_id, id_to_name[tutor_id]]
                consecutive_count = 1
            elif (previous_slot == tutor_dict[tutor_id][k][2]-1):  #수업 시간이 이어져 있는 경우

                consecutive_count += 1
            else:  #수업 시간이 끊어져 있고 학생이 원하는 만큼 길지 않은 경우
                first_time = [tutor_dict[tutor_id][k][0],tutor_dict[tutor_id][k][1],tutor_id, id_to_name[tutor_id]]
                consecutive_count = 1 
            previous_slot = tutor_dict[tutor_id][k][2]

            if consecutive_count >= time_length:  #수업 가능한 시간이 학생이 원하는 만큼 이상일 때
                answer_list.append(first_time)
                break

f = open('tutor.csv','w',newline='')
wr = csv.writer(f)
for a in range(len(answer_list)):
    wr.writerow(answer_list[a])
f.close()
data.close()