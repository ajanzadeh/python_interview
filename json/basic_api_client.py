import json
import requests
users = {}

def get_http(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            return json.loads(response.text)
        except ValueError as err:
            print(err)

todolist = get_http("https://jsonplaceholder.typicode.com/todos")

if todolist:
   for todo in todolist:
       if todo["completed"]:
         try:
           print(todo["userId"])
           users[todo["userId"]] += 1
         except:
              users[todo["userId"]] = 1
print(users)
