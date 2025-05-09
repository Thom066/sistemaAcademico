#base de datos con estudiantes
infoEstudiantes={
        1001:{'Nombre completo': 'thomas noriega zuleta', 'edad': 18, 'nota': 4.0},
        1002:{'Nombre completo': 'stik berrio montaño', 'edad': 16, 'nota': 3.5
    },
        1003:{'Nombre completo': 'alex muñoz mosquera', 'edad': 17, 'nota': 3.0
    },
        1004:{'Nombre completo': 'estiven garcia diez', 'edad': 19, 'nota': 2.5
    },
        1005:{'Nombre completo': 'james salazar marulanda', 'edad': 16, 'nota': 2.0
    },
        1006:{'Nombre completo': 'elena santana jaramillo', 'edad': 18, 'nota': 5.0
    }
}

#aqui estoy agregando estudiantes 
# ##terminado
def agregarEstudiantes():
    print("Vas a agregar un estudiante")

    
    while True:
        idAggEst = int(input("Ingrese numero de documento: "))

        if idAggEst in infoEstudiantes:
            print("Este usuario esta en la plataforma. Ingrese bien su documento")
        else :
            print("Prosiga")
            break
    
    nomAggEst = input("Ingrese su nombre completo: ")

    edadAggEst = int(input("Digite su edad: "))

    notaAggEst= float(input("Digite la nota que saco: "))

    infoEstudiantes[idAggEst]={
        "Nombre completo":nomAggEst,
        "edad": edadAggEst,
        "nota": notaAggEst
    }
    print("Estudiante agregado")

#aqui estoy buscando
#El sistema debe permitir la búsqueda de estudiantes por su número de identificación (ID) (búsqueda exacta).
def buscarEstudiantes():
    while True:
        idBuscarEst = input("Digite el documento por favor: ")

        registroId= infoEstudiantes.get(idBuscarEst)

        if registroId not in infoEstudiantes:
            print("el contacto no existe")
        else :
            if registroId:
                print("---"*10,"Estudiante encontrado","---"*10)
                print("Documento:", idBuscarEst)
                print(f"Nombre completo:", registroId["Nombre completo"],"\nedad:",registroId["edad"],"\nnota:",registroId["nota"])
            
            break
    # print("Vas a buscar estudiantes")
    # print(infoEstudiantes)
    # while True:
    #     idBuscarEst = input("Digite el numero de identificaion: ")

    #     if idBuscarEst in infoEstudiantes:
    #         print("Este usuario esta registrado")
    #         for idBuscarEst in infoEstudiantes.values():
    #             if idBuscarEst in infoEstudiantes:
    #                 print

            
#aqui debo actualizar informacion
def actualizarEstudiantes():
    print("Actualizar datos")

    print("Que deseas actualizar:\n 1) Edad\n 2) nota")

#aqui debo eliminar informacion
### terminado
def eliminarEstudiantes():
    print("Eliminar estudiante")
    print(infoEstudiantes)
    print("---"*13)

    while True:

        estudianteElim = int(input("Digite el id del estudiante que desea eliminar: "))

        if estudianteElim not in infoEstudiantes:
            print("No se encuentra en el sistema. Ingrese el id de nuevo")
            
        else :
            print("Seguro que quieres eliminarlo del sistema?\n 1) SI o 2) No" )
            opcionEliminar = input("Digite una opcion: ")
            if opcionEliminar =="1":
                print("Estudiante eliminado del sistema") 
                infoEstudiantes.pop(estudianteElim)
                break

            elif opcionEliminar =="2":
                print("Saliendo de eliminar")
                break
                
#aqui debo calvular promedios
def calcularPromedios():
    print

###aqui debo listar los estudiantes del umbral por debajo de 3.0
###terminado
def listarEstudiantesUmbral():
    for estudiante in  infoEstudiantes.values():
        if estudiante["nota"]<3.0: 
            print(f"{estudiante['Nombre completo']} va perdiendo con: {estudiante['nota']}\n", "---"*13)

while True: 
    print(infoEstudiantes)
    print("---"*13)
    print ("Que deseas hacer:\n 1) Agregrar estudiantes \n 2) Buscar estudiantes\n 3)Actualizar informacion \n 4) Eliminar estudiantes\n 5) calcular promedio de notas\n 6) Listar estudiantes con notas inferiores a 3.0\n 7) Salir")

    opcionMenu = input("Digita una opcion-->")

    if opcionMenu == "1":
        agregarEstudiantes()
    elif opcionMenu == "2":
        buscarEstudiantes()
    elif opcionMenu == "3":
        actualizarEstudiantes()
    elif opcionMenu== "4":
        eliminarEstudiantes()
    elif opcionMenu == "5":
        calcularPromedios()
    elif opcionMenu == "6":
        listarEstudiantesUmbral()
    elif opcionMenu== "7":
        break
    else: 
        print("Opcion invlaida")



