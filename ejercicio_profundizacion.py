import json
import requests
import matplotlib.pyplot as plt

def fetch():
    response = requests.get('https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50')
    data = response.json()
    json_response = data['results']
    

    list_filtrada = []
    diccionario = {}

    
    lista_en_pesos = [x for x in json_response if x['currency_id'] == 'ARS'] 
    
    
   
    for x in lista_en_pesos:
        diccionario['precio'] = x['price']    
        diccionario['condicion'] = x['condition']
        list_filtrada.append(diccionario.copy())
    
    return list_filtrada

def transform(dataset, min, max):
    precio_min = [valor for valor in dataset if valor['precio'] < min]
    precio_medio = [valor for valor in dataset if valor['precio'] > min and valor['precio'] < max]
    precio_max = [valor for valor in dataset if valor['precio'] > max]

    count_min = len(precio_min)
    count_medio = len(precio_medio)
    count_max = len(precio_max)

    return [count_min, count_medio, count_max]

def report(data):
    fig = plt.figure()
    fig.suptitle('Precios de Alquileres', fontsize = 16)
    ax = fig.add_subplot()

    ax.pie(data, labels = ['$0 - $10000', '$10000 - $250000', 'Mayor a $25000'], autopct = '%1.1f%%', startangle = 90)

    plt.show(block = True)



if __name__ == '__main__':
    
    min = 10000
    max = 25000

    dataset = fetch()
    data = transform(dataset, min, max)
    report(data)