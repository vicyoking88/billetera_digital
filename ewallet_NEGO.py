"""NEGOCIOS"""
class OpeCripto():
    def __init__(self,t_r):
        self.idu, self.moneda, self.cantidad, self.tx = t_r
        self.t_n=t_r

#--- METODO OPERACIONES DE SUMA Y RESTA DE LOS FONDOS DE LAS MONEDAS contenidas en nuestra billetera

    def oper_carga(self, dic_sal2, RoT):

        if RoT:
            if self.moneda in dic_sal2:
                print("Cantidad Actual de la CRiptoMoneda")
                print(self.moneda)
                sal_actual=float(dic_sal2.get(self.moneda))
                print(sal_actual)
                tota_saldo=sal_actual+float(self.cantidad)
                dic_sal2[self.moneda]=tota_saldo  
                return dic_sal2
            else:
                dic_sal2[self.moneda]=float(self.cantidad)
                print("INgreso nueva Moneda a tu e-wallet ")
                return dic_sal2
        else:
            if self.moneda in dic_sal2:
                sal_actual=float(dic_sal2.get(self.moneda))
                if float(self.cantidad)<sal_actual:
                    print("Tienes de "+self.moneda+" : ",sal_actual," unidades para transferir")
                    conti_operacion = input("Desea continuar con la transferencia (s/n):")
                    tota_saldo=sal_actual-float(self.cantidad)
                    if conti_operacion=="s":
                        dic_sal2[self.moneda]=str(tota_saldo) 
                        return dic_sal2
                    else:
                        print("Se cancelo operacion ")
                        return dic_sal2
                else:
                    print(" NO te alcanza para transferir ")
                    return dic_sal2
            else:
                print("No TIENES unidades de esta Criptomoneda en tu Billetera ")
                return dic_sal2
                  
    
    #DESPUES DE VALIDAR SI EXISTE EN COIN MARKET Y DESPUES DE SUMAR O RESTAR AL SALDO
    #con esta funcion ejecutamos ingreso y resta o transferencia
    def cx_regis (self, RoT):  
        from ewallet_registro import registro #Hacemos referencia a la capa de registros
        cx_regis1=registro(self.t_n)#enviamos datos al constructor de la capa de registro
        dic_regi=self.oper_carga(cx_regis1.mostrar_saldos(), RoT)#Cargamos los fondos actuales de la billetera para su posterior actualizacion
        if not dic_regi==cx_regis1.mostrar_saldos():#validamos si se hizo un cambio en el diccionario de monedas registradas en la billetera
            cx_regis1.reg_saldos(dic_regi)#registramos actualiacion del diccionario al archivo csv
            return cx_regis1.reg_TX()#retornamos mensaje de registro exitoso

#----FUNCION PARA CARGAR EL BALANCE DE UNA MONEDA EN ESPECIFICO
    def inf_moneda(self):
        from ewallet_registro import registro
        from ewallet_Conex_coinmarket import conexmarket
        cx_regis1=registro(self.t_n)
        con_market=conexmarket()
        if self.moneda in cx_regis1.mostrar_saldos():
            inf_m=cx_regis1.mostrar_saldos().get(self.moneda)
            try:
                cot_m=float(con_market.consul_binance(self.moneda))
                tot_usd_cripto=inf_m*cot_m
                print(
                "Moneda                 : ",self.moneda,"\n"
                "Cantidad               : ",inf_m,"\n"
                "Cotizacion en Binance  : ",cot_m," USDT Por unidad\n"
                "Total USD de la Moneda : ",tot_usd_cripto," USDT")
            except:
                print("Oops no tienes internet")
            
        else:
            print("No tienes unidades de esta Criptomoneda en tu Billetera ")

#----------FUNCION PARA EL BALANCE GENERAL
    def balan_gene(self):
        from ewallet_registro import registro
        from ewallet_Conex_coinmarket import conexmarket
        cx_regis1=registro(self.t_n)
        con_market=conexmarket()
        monedas=[]
        cantidades=[]
        cotizaciones=[]
        total_m=[]
        t_G_usd=0.0
        try:
            print("Moneda  -  Cantidad  -  Cotizaciones  -  Monto USD\n")
            for key in cx_regis1.mostrar_saldos().keys():
                monedas.append(key)
                cantidades.append(cx_regis1.mostrar_saldos().get(key))
                
                cotizaciones.append(float(con_market.consul_binance(key)))
                total_m.append((cx_regis1.mostrar_saldos().get(key))*float(con_market.consul_binance(key)))
            conteo=len(monedas)
            for i in range(conteo):
                print(monedas[i],"    - ",cantidades[i],"     - ",cotizaciones[i],"     - ",total_m[i],"\n")
                t_G_usd=t_G_usd+float(total_m[i])
            print("Total USD de todas las monedas es : ",t_G_usd)   
        except:
            print("Oops no tienes internet")



        
#--------VALIDAMOS SI LA MONEDA EXISTE en COINMARKET
    def vali_coin(self, RoT):
        from ewallet_Conex_coinmarket import conexmarket
        con_market=conexmarket()
        verificacion=con_market.consul_coinm()

   
        if RoT:
            while not (self.moneda in verificacion.keys()):
                mensaje= "Moneda Invalida no esta en CoinMarket, Por favor indique una moneda valida para proceder con el registro"
                return mensaje
            else:
                mensaje= "Moneda con symbol:",self.moneda,"y nombre:",verificacion.get(self.moneda)," se encuentra en el sistema de coimnmarketcap.com"
                #print(mensaje)
                RoT=True
                self.cx_regis(RoT)
                return mensaje

                
        else:

            while not (self.moneda in verificacion.keys()):
                mensaje= "Moneda Invalida no esta en CoinMarket, Por favor indique una moneda valida para proceder con la Transferencia"
                return mensaje
            else:
                mensaje= "Moneda con symbol:",self.moneda,"y nombre:",verificacion.get(self.moneda)," se encuentra en el sistema de coimnmarketcap.com"
                #print(mensaje)
                RoT=False
                self.cx_regis(RoT)
                return mensaje
    
 #--- caRGAMOS Y enviamos historico de transacciones                
    def histo_m (self):
        from ewallet_registro import registro
        cx_regis1=registro(self.t_n)
        return cx_regis1.mostrar_tx()

"""x=OpeCripto("","")
x.vali_coin()
input()"""
