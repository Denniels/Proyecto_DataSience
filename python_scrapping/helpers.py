import re

#urlScrapping = 'https://vincheckpro.com'
urlScrapping = 'https://driving-tests.org/vin-decoder'
#urlScrapping = 'https://vincheck.info'


#https://api.carmd.com/
#http://api.carmd.com/v3.0/decode?vin=1GNALDEK9FZ108495
AuthorizationKey = 'Basic OTEzNjczMmMtMTFhNi00NDBhLTllMTEtY2E1Mzk1MGIxZjZj'
PartnerToken = '0e033e73987845d895a4aa866734bc64'


def returnNumber(text):
    number = re.findall(r'\d+', text)
    #number = [float(s) for s in text.split() if s.isdigit()]
    return number[0]

def lastWord(text):
    # string to list and
    lis = list(text.split(" "))
     
    # length of list
    length = len(lis)
     
    # returning last element in list
    return lis[length-1]

def lastTwoWord(text):
    # string to list and
    text = text.replace('\n', " ")
    lis = list(text.split(" "))
     
    # length of list
    length = len(lis)
     
    # returning last element in list
    return lis[length-2] +' '+ lis[length-1]


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
