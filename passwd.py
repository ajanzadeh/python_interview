import time
import random
import glob
import os
import shutil
import re

users_file = open('/etc/passwd', "r")
group_file = open('/etc/group', "r")

users_membership = {}
groups = []


for line in users_file:
    users_membership[line.split(":")[0]] = 0

for line in group_file:
    if line.split(":")[3] != "\n":
      groups.append(line.split(":")[3].strip("\n").split(","))

for user in users_membership:
    cnt = 0
    for memberes in groups:
        for member in memberes:
          if user == member:
             users_membership[user] += 1
print(users_membership)
