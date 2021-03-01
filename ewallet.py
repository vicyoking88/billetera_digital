""" PRESENTACION"""
# Importamos librerias y clases necesarias
import platform # para validar sistema operativo donde se ejecute la aplicacion
import os#para llamar la funcion del sistema operativo a usar 
import sys#para llamar funciones de ventana
from ewallet_NEGO import OpeCripto#conexion a la capa logica de negocios

#--Funcion para limpiar pantallas
def limpiar_pantalla():
    if platform.system()=='windows':
        os.system('cls')
    else:
        os.system('cls')

        
        
#----MENU PRINCIPAL-----
def MenuPrincipal():

#--Titulo y opciones del menu

    cadenaTitulo="Bienvenido a mi e-wallet".title()
    print (cadenaTitulo.center(50, "="))
    print("\nPor favor escoje una de las siguientes opciones : ")

    print(
    "\n1. - Ingresa La cantidad de Criptomonedas", 
    "\n2. - Transferrir mis Criptomonedas"
    "\n3. - Balance por Moneda"
    "\n4. - Balance General"
    "\n5. - Historico de Transacciones"
    "\n6. - Close APP" )

#--Bucle para cargar las opciones del menu rango entre 1 y 6
    opc = "0"
    while opc<"6":
        opc = input("\nEscoge una opcion de 1 a 6: \n")
#--Condicional con 6 opciones cada una ejecuta su respectivo codigo
        if opc=="1":
            #TOMA DE DATOS PARA CONSIGNAR MONEDAS
            idu = input("ingrese Codigo Remite de 6 caracteres Numericos : ")
            #---control validacion codigo
            while not (6==len(idu) and idu.isdigit()):
                idu = input("ingrese Codigo Remite de 6 caracteres Numericos : ")
            else:#-- control validacion del simbolo de la criptomoneda
                moneda=input("ingrese Simbolo de Criptomoneda  : ") 
                while not (5>=len(moneda) and moneda.isalpha()):
                    moneda = input("ingrese Simbolo de Criptomoneda  : ")
                else:#--control validacion de la cantidad, validamos si es un numero
                    cantidad=input("ingrese Cantidad a REcibir : ")
                    while not cantidad.replace('.','',1).isdigit():
                        cantidad=input("Debes ser numerico, Por favor ingrese Cantidad a REcibir : ")
                        
                    else:
                        limpiar_pantalla()#limpiamos las opciones del menu principal
                        print("----Ingreso Criptomonedas----")#titulo operacion de registro
                        tx="Deposito"#tipo de transaccion
                        #CARGAMOS A UNA TUPLA
                        t_p=idu,moneda,cantidad,tx
                        #ENVIAMOS TUPLA AL CONSTRUCTOR
                        cx_reg=OpeCripto(t_p)
                        #tipo de tx
                        RoT=True
                        #validamos error de conexion a internet
                        try:#validamos si existe moneda en COINMARKET
                            print(cx_reg.vali_coin(RoT))
                        except:#si arroja error no tenemos conexion a internet
                            print("Oops no tienes internet, Conecta para validar moneda en CoinMarket")
#--- Despues de mostrar la informacion damos la opcion e regreso al menu principal
            input("\nPresiona Enter para regresar")  
#--- limpiamos pantalla
            limpiar_pantalla()
#----- ejecutamos funcion principal mostrar el menu
            MenuPrincipal() 
        elif opc=="2":
            #TOMA DE DATOS PARA TRANSFERIR MONEDAS
            idu = input("ingrese Codigo Remite de 6 caracteres Numericos : ")
            while not (6==len(idu) and idu.isdigit()):
                idu = input("ingrese Codigo Remite de 6 caracteres Numericos : ")
            else:
                moneda=input("ingrese Simbolo de Criptomoneda  : ") 
                while not (5>=len(moneda) and moneda.isalpha()):
                    moneda = input("ingrese Simbolo de Criptomoneda  : ")
                else:
                    cantidad=input("ingrese Cantidad a Transferir : ")
                    while not cantidad.replace('.','',1).isdigit():
                        cantidad=input("Debes ser numerico, Por favor ingrese Cantidad a Transferir : ")
                    else:
                        tx="Transferencia"
                        limpiar_pantalla()
                        print("----Transferencia De Criptomonedas----")
                        #CARGAMOS A UNA TUPLA
                        t_p=idu,moneda,cantidad,tx
                        #ENVIAMOS TUPLA AL CONSTRUCTOR
                        cx_reg=OpeCripto(t_p)
                        RoT=False
                        try:
                            print(cx_reg.vali_coin(RoT))
                        except:
                            print("Oops no tienes internet, conectate para validar Moneda en CoinMarket")                   
            input("\nPresiona Enter para regresar")  
            limpiar_pantalla()
            MenuPrincipal()   
#--- Opcion para mostrar el balance de una moneda de nuestra billetera
        elif opc=="3":
            moneda=input("Ingrese Moneda : ")
            while not (3==len(moneda) and moneda.isalpha()):
                moneda = input("ingrese Simbolo de Criptomoneda  : ")
            else:
                #CARGAMOS A UNA TUPLA
                limpiar_pantalla()
                print("----Balance Monedas de mi e-wallet Segun Binance----\n")
                t_p=("",moneda,"","")
                #ENVIAMOS TUPLA AL CONSTRUCTOR
                cx_reg=OpeCripto(t_p)
                cx_reg.inf_moneda()
            input("\nPresiona Enter para regresar")  
            limpiar_pantalla()
            MenuPrincipal()  
#--- Opcion para mostrar balance general de nuestra biletera            
        elif opc=="4":  
            limpiar_pantalla()
            print("----Balance General de mi e-wallet Segun Binance----\n")
            t_p=("","","","")
            cx_reg=OpeCripto(t_p)
            cx_reg.balan_gene()
            input("\nPresiona Enter para regresar")  
            limpiar_pantalla()
            MenuPrincipal() 
#--  Opcion para mostrar el historico de transacciones de nuestra billetera
        elif opc=="5":
            limpiar_pantalla()
            print("---- Historico tx de mi e-wallet ----\n")
            #CARGAMOS A UNA TUPLA
            t_p=("","","","")
            #ENVIAMOS TUPLA AL CONSTRUCTOR
            cx_reg=OpeCripto(t_p)
            print(cx_reg.histo_m())
            input("\nPresiona Enter para regresar")  
            limpiar_pantalla()
            MenuPrincipal()
#--- Opcion para salir de la aplicacion            
        elif opc=="6":
            print("escogio la opcion 6")
            sys.exit()
        else:
            print("opcion invalidad")
        opc="0"
#--- Arranca programa
if __name__ == "__main__":
    MenuPrincipal()
    

#input()

