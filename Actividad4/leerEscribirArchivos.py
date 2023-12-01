#escribir sobre un archivo, primero abriendolo
archivo=open("archivoNuevo.txt", 'a')
archivo.write("Ejemplo de escritura sobre un archivo \n")

#leer archivo 
archivo=open("archivoNuevo.txt",'r')
print(archivo.read())

archivo.close()