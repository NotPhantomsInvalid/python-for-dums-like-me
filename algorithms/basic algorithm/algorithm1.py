# Algoritmo 1 find the 3 names in the list
a='fernando','mario','luis'
print ('Ingrese un nombre')
entrada = input()
while entrada not in a:
    print ('Ingrese un nombre')
    entrada = input()
    if entrada == a[0]:
        print ('El nombre es', a[0])