def solution(S, K):
    # write your code in Python 3.6
     days = ["Mon","Tue", "Wed","Thu","Fri","Sat","Sun"]
     if (K > 0) and ( K < 500):
         
         rk =( K % 7 )- 7
         rindex = days.index(S)+rk
         r = days[rindex]
     else:
       print("invalid input")
     return r


print(solution("Tue",1))
