n1 = int(input("Introduce tu primer número: "))
n2 = int(input("Introduce tu segundo número: "))
n3 = int(input("que quiere hacer: "))

print("1) sumar, 2) restar, 3) Dividir")
 
if n3==1:
    print("la suma de: ", n1, "y", n2, "Es", (n1+n2))
elif n3==2:
    print("La ressta de ", n1, "Y", n2,"Es",(n1-n2))
elif n3==3:
    print("La division de ", n1, "Y", n2,"Es",(n1//n2))
else:
    print("Ay no se ")

