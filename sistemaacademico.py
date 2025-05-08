#base de datos con estudiantes
infoEstudiantes={
    '001':{'Nombre completo': 'thomas noriega zuleta', 'edad': '18', 'nota': 4.0},
    '002':{'Nombre completo': 'stik berrio montaño', 'edad': '16', 'nota': 3.5
    },
    '003':{'Nombre completo': 'alex muñoz mosquera', 'edad': '17', 'nota': 3.0
    },
    '004':{'Nombre completo': 'estiven garcia diez', 'edad': '19', 'nota': 2.5
    },
    '005':{'Nombre completo': 'james salazar marulanda', 'edad': '16', 'nota': 2.0
    },
    '006':{'Nombre completo': 'elena santana jaramillo', 'edad': '18', 'nota': 5.0
    }
}

#aqui estoy agregando estudiantes
def agregarEstudiantes():
    print("Vas a agregar un estudiante")

    
    while True:
        idAggEst = input("Ingrese numero de documento: ")

        if idAggEst in infoEstudiantes:
            print("Este usuario esta en la plataforma. Ingrese bien su documento")
        else :
            print("Prosiga")
            break
    
    nomAggEst = input("Ingrese su nombre completo: ")

    edadAggEst = input("Digite su edad: ")

    notaAggEst= float(input("Digite la nota que saco: "))

    infoEstudiantes[idAggEst]={
        "Nombre completo":nomAggEst,
        "edad": edadAggEst,
        "nota": notaAggEst
    }
    print("Estudiante agregado")

#aqui estoy buscando
def buscarEstudiantes():
    print("Vas a buscar estudiantes")
    print(infoEstudiantes)
    while True:
        idBuscarEst = input("Digite el numero de identificaion: ")

        if idBuscarEst in infoEstudiantes:
            print("Este usuario esta registrado")
            
#aqui debo actualizar informacion
def actualizarEstudiantes():
    print("Actualizar datos")

    print("Que deseas actualizar:\n 1) Edad\n 2) nota")
    opcionInfo = 






while True: 
    print ("Que deseas hacer:\n 1) Agregrar estudiantes \n 2) Buscar estudiantes\n 3)Actualizar informacion \n 4) Eliminar estudiantes\n 5) calcular promedio de notas\n 6) Listar estudiantes con notas inferiores a 3.0")

    opcionMenu = input("Digita una opcion-->")

    if opcionMenu == "1":
        agregarEstudiantes()
    elif opcionMenu == "2":
        buscarEstudiantes()
    elif opcionMenu == "3":
        actualizarEstudiantes()
    

