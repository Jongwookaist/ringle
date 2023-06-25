import json
import random
import datetime

start_time = datetime.datetime.strptime("2023-06-07T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
end_time = datetime.datetime.strptime("2023-06-09T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
time_delta = datetime.timedelta(minutes=30)

json_data = {"tutors": [], "slots": []}

# Generate tutors
for i in range(1, 8):
    tutor_id = "t" + str(i)
    tutor_name = "Tutor " + str(i)
    json_data["tutors"].append({"id": tutor_id, "name": tutor_name})

# Generate start times and session numbers for each tutor
session_num = 1
for tutor in json_data["tutors"]:
    tutor_id = tutor["id"]
    for j in range(3):
        random_time = start_time + random.randint(0, int((end_time - start_time) / time_delta)) * time_delta
        slot_id = "s" + str(session_num)
        json_data["slots"].append({"id": slot_id, "start_time": random_time.strftime("%Y-%m-%dT%H:%M:%SZ"), "tutor_id": tutor_id})
        session_num += 1

# Output the generated JSON data
output_file = "sample.json"
with open(output_file, "w") as f:
    json.dump(json_data, f, indent=4)

print(f"Sample JSON data with tutors and slots has been generated and saved to '{output_file}'.")
