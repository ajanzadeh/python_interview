#! /bin/env python
# generates a dict of users and how many groups they have

#Cracking the Coding Interview: 189 Programming Questions and Solutions

passwd_file = "/etc/passwd"
group_file = "/etc/group"

def readfile(filename):
    with open(filename,'r') as f:
        data = f.readlines()
    return(data)

users_membership = {}
groups = []

for line in readfile(passwd_file):
    users_membership[line.split(":")[0]] = 0 #O(n)  #ex: root:x:0:0:root:/root:/bin/bash

for line in readfile(group_file):
    if line.split(":")[3] != "\n":
      groups.append(line.split(":")[3].strip("\n").split(",")) #O(n)  # example adm:x:4:aj,arash

for user in users_membership: # O(n^2)
    for memberes in groups:
        for member in memberes: # example if you have few member adm:x:4:aj,arash
          if user == member:
             users_membership[user] += 1
print(users_membership)
