
while True:  
    num1 = int(input('inserire il primo numero:   '))
    num2 = int(input('inserire il secondo numero:  '))
    if(num1>0 and num2>0):
        break 
   

def MCD(n1,n2):
#Calcola il Massimo Comune Divisore tra due numeri#
    while n1!=n2:
        if n1>n2:
            n1=n1-n2

        else:
            n2=n2-n1
            
    return n1
print(MCD(num1,num2))