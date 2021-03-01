"""CONEXION COINMARKET"""
class conexmarket(object):

    def __init__(self):
        self

#--Consulta En Coin Market Existencia de la moneda
    def consul_coinm(self): 
        monedas=()
        monedas_dict={}
        import requests
        COINMARKET_API_KEY = "2448e9c9-b938-4f0e-85f1-9878a7b41c87"
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
        }
        data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
        for cripto in data["data"]:
            monedas_dict[cripto["symbol"]]=cripto["name"]

        monedas = monedas_dict
        return monedas

#-- Consulta del valor de la moneda en el momento para su registro y visualizacion   
    def consul_binance(self,cripto):
        import requests
        data=requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+cripto+"USDT").json()
        cotiza=float(data["price"])
        return cotiza



