print("ESTA ES UNA CALCULADORA")
print("ingrese un valor")
a = int(input())
print("ingrese b")
b = int(input())
c = a+b
e = a-b
m = a*b
d = a/b if b != 0 else 'Indefinido (división por cero)'
print ("El resultado de la suma es igual a:",c)
print ("El resultado de la resta es igual a:",e)
print ("El resultado de la multiplicacion es igual a:",m)
print ("El resultado de la division es igual a:",d)