import json
import random
import datetime
import sys

start  = sys.argv[1]
end = sys.argv[2]
tutor_num = int(sys.argv[3])
class_num = int(sys.argv[4])

start_time = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ")
end_time = datetime.datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ")
time_delta = datetime.timedelta(minutes=30)

json_data = {"tutors": [], "slots": []}

# 강사
for i in range(1, tutor_num+1):
    tutor_id = "t" + str(i)
    tutor_name = "Tutor " + str(i)
    json_data["tutors"].append({"id": tutor_id, "name": tutor_name})

#강사 수업 시작 시간 및 slot id 만들기
session_num = 1
for tutor in json_data["tutors"]:
    tutor_id = tutor["id"]
    for j in range(class_num):
        random_time = start_time + random.randint(0, int((end_time - start_time) / time_delta)) * time_delta
        slot_id = "s" + str(session_num)
        json_data["slots"].append({"id": slot_id, "start_time": random_time.strftime("%Y-%m-%dT%H:%M:%SZ"), "tutor_id": tutor_id})
        session_num += 1


output_file = "sample.json"
with open(output_file, "w") as f:
    json.dump(json_data, f, indent=4)