# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.
# EXAMPLE
# Input: "Mr 3ohn Smit h 13
# Output: "Mr%203ohn%20Smith"

def URLify(string):

    if str(string):
        return string.replace(" ","%20")
    else:
        print("not a string")

def URLify_nomodule(string):
    string2 = []
    if str(string):
        for i in range(0,len(string)):
            if string[i] == " ":
                string2.append("%20")
            else:
                string2.append(string[i])
        string2 = "".join(map(str,string2))
        return string2
print(URLify("test this"))
print(URLify_nomodule("this number 2"))
