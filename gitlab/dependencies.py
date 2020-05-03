# Problem: Package dependencies
#
# There are a lot of different ways to install packages on different operating systems.
# One thing that most of them have in common is a way to handle dependencies.
# When one package depends on another package the dependency must be installed first.
#
# The following text file lists packages (A,B,C,..etc) followed by their corresponding package dependencies.
#
# example: deps.txt
#
# A:D,B
# B:C,E
# C:D,E
#
# First task is we read in the file, populating a data structure where
# keys are the package names and the values are an array of dependencies
#
# deps = {
# "A" : ["D","B"],
# "B" : ["C", "E"],
# "C" : ["D", "E"]
# }
#
#
# Next is to build the dependency management part of a package manager.
# For example, to install package C you must also install package D and E.
# Write a function get_deps() that given a package name returns a list of package dependencies.
#
# def b:
# b


def read_file():
  data = dict()
  with open("deps.txt", "r") as deps:
    for line in deps:
      line = line.strip()
      (key, val) = line.split(':')
      dependencies = val.split(',')
      for dep in dependencies:
          data.setdefault(key,[]).append(dep)
  return data ;
#read_file()
def dependency_management(package, dependency_list=None, seen_packages=None ):
  data = read_file()
  if dependency_list is None:
     dependency_list = []
  if seen_packages is None:
      seen_packages = []
  if (package in data) and (package not in seen_packages):
    seen_packages.append(package)
    for i in data[package]:
      dependency_list.append(i)
      if i in data:
        for x in data[package]:
           dependency_management(x, dependency_list, seen_packages)
  dependency_list = list(set(dependency_list))
  return dependency_list



def find_dependencies():

  check_packages = "A"
  print (dependency_management(check_packages))


find_dependencies()
