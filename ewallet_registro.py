class registro:
  
    def __init__(self,t_r):
        self.idu_r, self.moneda_r, self.cantidad_r, self.tx_r = t_r

#--- funcion para registrar las transacciones en el archivo de registros

    def reg_TX (self):
        from datetime import datetime
        from ewallet_Conex_coinmarket import conexmarket
        con_market=conexmarket()
        cot_m=float(con_market.consul_binance(self.moneda_r))
        USD_T=cot_m*float(self.cantidad_r)
        ahora = datetime.now()
        archivo=open("registro_tx.csv","a")

        archivo.write(self.idu_r)
        archivo.write(",")
        archivo.write(self.moneda_r)
        archivo.write(",")
        archivo.write(self.cantidad_r)
        archivo.write(",")
        archivo.write(str(cot_m))
        archivo.write(",")
        archivo.write(str(USD_T))
        archivo.write(",")
        archivo.write(self.tx_r)
        archivo.write(",")
        archivo.write(ahora.strftime("%d/%m/%y %H:%M:%S"))
        archivo.write("\n")
        
        archivo.close()

        print("Transaccion Exitosa, DAtos de la Operacion :\n"+
        "Codigo Remite: "+self.idu_r+"\n"+
        "Simbolo Moneda: "+self.moneda_r+"\n"+ 
        "Cantidad : "+self.cantidad_r+"\n"+
        "Tipo de Operacion: "+self.tx_r)

#Funcion para registrar nuevos saldos o actualizar los existentes en el archivo
    def reg_saldos(self, dic_sal):
        archivo_n="saldos_m.csv"
        csv = open(archivo_n,"w")
        columnas="Moneda,Saldo\n"
        csv.write(columnas)
        for key in dic_sal.keys():
            moneda=str(key)
            saldo=str(dic_sal[key])  
            filas=(moneda+","+saldo+"\n")
            csv.write(filas)
           
#--- CArgamos los registros de los movimientos de nuestra billetera para su visualizacion

    def mostrar_tx(self):
        #print("hola")
        import pandas as pd
        d_transa=pd.read_csv("registro_tx.csv")
        return d_transa

#--- Cargamos los fondos de nuestra billetera para su visualizacion.

    def mostrar_saldos(self):
        import pandas as pd
        d_saldos=pd.read_csv("saldos_m.csv")
        sal_act=dict(d_saldos.values.tolist())
        return sal_act
        


    


