print('tka co jak je u tebe dneska??/ napis stupne CISLEM ZADNE CELSIA NEDAAVEJ')
teplota=int(input(''))
if teplota < 10 :
    print('celkem ziminka')
    print('oblec si plavky')
elif teplota <=25 :
    print('prijemne celkem mnam')
    print('oblec se jak panda, anebo jako tucnak Kowalski')
else :
    print('fuj vedro jak v sahare')
    print('oblec se jako bys slo lyzovat :33')
    
import time
print('a ted se jdeme ozvedet jestli si tynager nebo ne')
time.sleep(2)
print('kolko ti je???????????????????????????????????')
vek=int(input(''))
if vek >= 12 and vek <=19:
    print("zatim jsi tynager........ zatim.")
elif vek >19 and vek <25 :
    print('niesi tynager :( )')
elif vek>=25 and vek<50 :
    print('omg dospelak')
elif vek<12 and vek>=5 :
    print('jezuuss co tu delas u pc mamka te vola spratku')
elif vek<5 :
    print('no dpc mlade jdi pryc od pc odkdy ses naucilo psat vubec, di si vymenit plenky uz zasmradly')
else:
    print('dedo starej')

print('no tak ted kdyz jsme se dozedeli tvuj vek.......')
time.sleep(1)
print('chces se libat s bananem??')
odpoved=input('')
if odpoved=="ano" or odpoved=="a" or odpoved=="ANO" :
    print('tak do toho libej se')
    banana_ascii="\U0001F34C"
    print(banana_ascii)
elif odpoved=="ne" or odpoved=="nn" or odpoved=="n" or odpoved=='NE':
    print('tak se libej s jablkem')
    jablko='\U0001F34E'
    print(jablko)
else:
    print('cotokurva pises didopice')
    time.sleep(3)
    exit()
