### Digitos_iguales

n = int(input("INGRESE UN NUMERO: \n"))
X = (n%10)
Y = (n//10)%10 

if(X==Y):
    print(" SI SON IGUALES")
else:
    print("NO SON IGUALES") 