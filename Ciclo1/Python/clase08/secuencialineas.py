lineas = []
while True:
    s = input("Escriba algunas lineas. Deje en blanco para finalizar: ")
    if s:
        lineas.append(s.upper())
    else:
        break;
 
for refran in lineas:
    print (refran)
print (lineas)