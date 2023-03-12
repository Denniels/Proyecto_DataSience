import re

#urlScrapping = 'https://vincheckpro.com'
urlScrapping = 'https://driving-tests.org/vin-decoder'
#urlScrapping = 'https://vincheck.info'

#https://api.carmd.com/
#http://api.carmd.com/v3.0/decode?vin=1GNALDEK9FZ108495
AuthorizationKey = 'Basic OTEzNjczMmMtMTFhNi00NDBhLTllMTEtY2E1Mzk1MGIxZjZj'
PartnerToken = '0e033e73987845d895a4aa866734bc64'


def returnNumber(text):
    '''
    definición: funcion que extrae numero de un texto
     
    text: dato al cual se aplicara la busqueda de numeros
          
    retorno: el primer numero de la lista
    '''
    number = re.findall(r'\d+', text)
    return number[0]

def lastWord(text):
    '''
    definición: funcion que retorna la ultima palabra de una lista
     
    text: dato al cual se aplicara el split de espacios
          
    retorno: la ultima palabra de la lista.
    '''
    
    lis = list(text.split(" "))
     
    length = len(lis)
     
    return lis[length-1]

def lastTwoWord(text):
    '''
    definición: funcion que concatena las ultimas dos palabras de una lista
     
    text: dato al cual se aplicara el split de espacios
          
    retorno: string concatenado con las dos ultimas palabras.
    '''    
    text = text.replace('\n', " ")
    lis = list(text.split(" "))
     
    length = len(lis)
     
    return lis[length-2] +' '+ lis[length-1]


def isfloat(num):
    '''
    definición: funcion que convierte un numero a tipo float
     
    num: dato a evaluar
          
    retorno: numero convertido a float.
    '''
    try:
        float(num)
        return True
    except ValueError:
        return False
