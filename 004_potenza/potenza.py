from ast import Raise
from logging import exception


import math

def potenza(x,n):
    if n<0:
        raise Exception("Errore")
        result=0
    if n==0:
        result=1

    elif n%2==0:
        result=potenza(x,n/2)
        result=result*result
    else:
        result=potenza(x,(n-1)/2)
        result=result*result
        
    print(result)  


if __name__ == "__main__":
    potenza(5,3)