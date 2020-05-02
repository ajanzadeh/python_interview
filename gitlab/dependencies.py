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
