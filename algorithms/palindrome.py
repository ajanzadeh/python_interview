# get a string and decide if it's palindrome or not.

def palindrome(word):

    middle_index = len(word)//2
    print(middle_index)

    for i in range(0,middle_index):
        if word[i] != word[len(word)-1-i] :
            print(word,": no it's not palindrome")
            break
        elif i == middle_index-1:
            print(word,": it's palindrome")




palindrome("step on no pets")
palindrome("rotator")
palindrome("arash")
