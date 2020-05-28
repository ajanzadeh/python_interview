#1*2*3*4*5*6 = 720

def factoriel(n):
    if n == 0:
        return 1
    else:
        if n == 1:
            return n
        else:
            return n * factoriel(n-1)

print(factoriel(6))
