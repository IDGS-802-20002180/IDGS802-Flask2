
#primero especificamos la ruta y en seguida la funcion que queremos, en este caso r para leerlo
#f=open('alumnos.txt','r')
#Llamamos la funcion read. para especificar que queremos que lea el archivo 
##nombres=f.read()
#imprimimos en consola
#print(nombres)
''' 
nombres2=f.readlines()
print(nombres2)
f.close()

for items in nombres2:
    print(items,end='')
'''
alumno={'Matricula':12345,'Nombre':'Mario','Apellidos':'Lopez','Correo':'Daniellizama17@gmail.com'}
f=open('alumnos.txt','a+')
for i in alumno:
    
    f.write(f'\n{i}: {alumno[i]}')
f.close()
