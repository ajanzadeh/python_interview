# write a function to get names and change the age from json_from_file.json and save it back
import json
import os.path
def form(firstName,lastName,age):

    json_file_name = "json_from_file.json"
    dir_name = os.path.dirname(__file__)
    json_path = os.path.join(dir_name,json_file_name)

    def load_json(path):
        with open(path,"r") as file:
            json_data = json.loads(file.read())
        return json_data
    def write_json(path):
        with open(path,"w") as file:
            json.dump(d,file)


    d = load_json(json_path)
    for item in d:
        print(item)
        for i in d[item]:
            if (i["firstName"] == firstName) and (i["lastName"] == lastName):
                i["age"] = age
                print("change age for ", firstName, lastName)
    print(d)
    w = write_json(json_path)
    return w

print(form("John","Doe",22))
