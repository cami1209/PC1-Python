archivo = input("Ingresa el nombre del archivo").lower()
extension = archivo.split(".")[-1]
if extension == "gif":
    print("image/gif")
elif extension == "jpg":
    print ("image/jpeg")
elif extension == "jpeg":
    print ("image/jpeg")
elif extension == "png":
    print ("image/png")
elif extension == "pdf":
    print ("application/pdf")
elif extension == "txt":
    print ("text/plain")
elif extension == "zip":
    print ("application/zip")
else:
    print("application/octet-stream")