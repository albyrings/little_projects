print('############################################')
print()
print('RISOLUTORE DEI PROBLEMI RICORRENTI DELLE OPS 2017-2018')
print('PROGRAMMA REALIZZATO DA ALBERTO ANELLI')
print('IL RISOLUTORE E\' IN GRADO DI RISOLVERE I SEGUENTI PROBLEMI:')
print()
print('a)Knapsack')
print('b)Crittografia')
print('c)Grafi')
print('d)Sottosequenze')
print('e)Pianificazione')
print('f)Canali')
print('g)Movimento di un robot')
print('h)Regole e deduzioni')
print('i)Fatti e conclusioni')
print('j)Movimento di pezzi degli scacchi')
print()
print('#############################################')
print()
 
            ###PROGRAMMI RISOLUTORI###
 
#MINERALI
def Minerali():
 
  print('Questo programma risolve l\' esercizio dei minerali. Per avviarlo, inserire i dati del problema quando richiesto e premere invio')
  print('Il programma supporta fino a 12 minerali e 2, 3 o 4 minerali alla volta per camion. E\' possibile utilizzare il programma più di una volta con gli stessi minerali senza reinserirli')
  print()
  #DEFINIZIONE DELLA CLASSE MINERALI
 
  class minerali:
      def __init__(self, valore=0, peso=0):
          self.valore = valore
          self.peso = peso
 
  m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12 = minerali(),minerali(),minerali(),minerali(),minerali(),minerali(),minerali(),minerali(),minerali(),minerali(),minerali(),minerali()
 
 
  #INPUT
  mins = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
  f = 0
  for mine in mins:
    f += 1
    mine.valore,mine.peso = eval(input('valore minerale ' + str(f))), eval(input('peso minerale ' + str(f)))
 
  while 1:
      pesomassimo = eval(input('Peso massimo trasportabile dal camion:'))
      mineralitrasportabili = eval(input('Numero massimo di minerali trasportabili(2,3 o 4):'))
 
      minerali = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
 
      #ALGORITMO
      valorerecord = 0
      pesorecord = 0
      mineralirecord = []
 
      if mineralitrasportabili == 2:
          for x in minerali:
              for y in minerali:
                  if not x == y:
                      if x.peso + y.peso <= pesomassimo:
                          if x.valore + y.valore > valorerecord:
                              valorerecord = x.valore + y.valore
                              pesorecord = x.peso + y.peso
                              mineralirecord = [x,y]
                          elif x.valore + y.valore == valorerecord:
                              if x.peso + y.peso < pesorecord:
                                  pesorecord = x.peso + y.peso
                                  mineralirecord = [x,y]
 
      if mineralitrasportabili == 3:
          for x in minerali:
              for y in minerali:
                  for z in minerali:
                      if not x == y and not x == z and not y == z:
                          if x.peso + y.peso + z.peso <= pesomassimo:
                              if x.valore + y.valore + z.valore > valorerecord:
                                  valorerecord = x.valore + y.valore + z.valore
                                  pesorecord = x.peso + y.peso + z.peso
                                  mineralirecord = [x,y,z]
                              elif x.valore + y.valore + z.valore == valorerecord:
                                  if x.peso + y.peso + z.peso < pesorecord:
                                      pesorecord = x.peso + y.peso + z.peso
                                      mineralirecord = [x,y,z]
 
      if mineralitrasportabili == 4:
          for x in minerali:
              for y in minerali:
                  for z in minerali:
                      for a in minerali:
                          if not x == y and not x == z and not x == a and not y == z and not y == a and not z == a:
                              if x.peso + y.peso + z.peso + a.peso <= pesomassimo:
                                  if x.valore + y.valore + z.valore + a.valore > valorerecord:
                                      valorerecord = x.valore + y.valore + z.valore + a.valore
                                      pesorecord = x.peso + y.peso + z.peso + a.peso
                                      mineralirecord = [x,y,z,a]
                                  elif x.valore + y.valore + z.valore + a.valore == valorerecord:
                                      if x.peso + y.peso + z.peso + a.peso < pesorecord:
                                          pesorecord = x.peso + y.peso + z.peso + a.peso
                                          mineralirecord = [x,y,z,a]
 
      #OUTPUT
      for min in mineralirecord:
          print ('valore e peso singolo', min.valore, min.peso)
      print ('')
      print ('peso complessivo', pesorecord)
      print ('valore complessivo ',valorerecord)
      print ('')
      continua = input('Continuare a usare il programma? S/N ')
      if continua == 'N':
          break
      print ('')
      print ('')
  print ('Grazie per aver usato questo programma!')
 
#CRITTOGRAFIA
def Crittografia():
  #le chiavi sono contate verso destra
  def cesare(lettera,chiave):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
    lettera_cifrata = 0
    for letter in alfabeto:
      lettera_cifrata = lettera_cifrata + 1
      if lettera == letter:
        break
    lettera_cifrata = lettera_cifrata + chiave
    while lettera_cifrata > 26:
      lettera_cifrata = lettera_cifrata - 26
    return alfabeto[lettera_cifrata - 1]
 
  #INPUT
  frase = input('Frase da decifrare ')
  differenza_chiavi = eval(input('Differenza tra le due chiavi (se viene usata un unica chiave digitare 0):'))
  frasedecifrata = []
 
  #DIVISIONE FRA LETTERE PARI E DISPARI
  lettere_pari = []
  lettere_dispari = []
  numero_lettera = 0
  for lepter in list(frase):
    numero_lettera = numero_lettera + 1
    if numero_lettera % 2 == 0:
      lettere_pari.append(lepter)
    else:
      lettere_dispari.append(lepter)
 
 
  #per le lettere pari viene usata chiave2 come chiave
  #ALGORITMO
  for chiave in range(26):
    frasedecifrata = []
    frasedecifr = ''
    chiave2 = chiave + differenza_chiavi
    y = 0
    for lettera in lettere_dispari:
      y = y + 1
      frasedecifrata.append(cesare(lettera,chiave))
      x = 0
      for letter in lettere_pari:
        x = x + 1
        if x == y:
          frasedecifrata.append(cesare(letter,chiave2))
    for let in frasedecifrata:
      frasedecifr = frasedecifr + let
    print (frasedecifr)
    print ('Chiave dispari verso destra = ',chiave)
    print ('Chiave pari verso destra = ',chiave2)
    print ('Chiave dispari verso sinistra = ',26 - chiave)
    print ('Chiave pari verso sinistra = ',26 - chiave2)
    print ('')
 
#GRAFI
def Grafi():
  pass
 
#SOTTOSEQUENZE
def Sottosequenze():
  pass
 
#PIANIFICAZIONE
def Pianificazione():
  pass
 
#FLUSSI IN UNA RETE
def Flussi():
  pass
 
#ROBOT
def Robot():
 
  print('QUESTO PROGRAMMA RISOLVE L\' ESERCIZIO DEL ROBOT:')
  print('DATO UN PERCORSO E DELLE COORDINATE DI PARTENZA IN UN PIANO')
  print('CARTESIANO IL PROGRAMMA INDIVIDUA LE COORDINATE DI ARRIVO')
  print('E\' INOLTRE NECESSARIO INSERIRE L\' ORIENTAMENO INIZIALE DEL ROBOT')
  print()
 
  ##############################
 
  #PARAMETRI INIZIALI
 
  orientamento = int(input("Inserisci l' orientamento iniziale del robot (1 per alto, 2 per destra, 3 per basso e 4 per sinistra) :"))
  istruzioni = input("Inserisci le istruzioni corrispondenti al percorso del robot, tutto attaccato e senza alcun carattere diverso da f, o,  a")
  x = int(input('Inserisci l\' ascissa (posizione sull\' asse delle x) del robot nella sua posizione di partenza: '))
  y = int(input('Inserisci l\' ordinata (posizione sull\' asse delle y) del robot nella sua posizione di partenza: '))
 
  #ALGORITMO
 
  for i in list(istruzioni):
    if i == 'f':
      if orientamento == 1:
        y += 1
      elif orientamento == 3:
        y -= 1
      elif orientamento == 2:
        x += 1
      elif orientamento == 4:
        x -= 1
    elif orientamento == 1 and i == 'a':
      orientamento = 4
    elif i == 'a':
      orientamento -= 1
    elif orientamento == 4 and i == 'o':
      orientamento = 1
    elif i == 'o':
      orientamento += 1
 
 
  #OUTPUT
 
  print()
  print ("coordinate di arrivo: (" + str(x) + ',' + str(y) + ')')
  if orientamento ==  1:
    print ("Orientamento verso l' alto")
  elif orientamento ==  3:
    print ("Orientamento verso il basso")
  elif orientamento ==  2:
    print ("Orientamento verso destra")
  elif orientamento ==  4:
    print ("Orientamento verso sinistra")
 
 
#REGOLE
def Regole():
  pass
 
#FATTI E CONCLUSIONI
def Fatti():
  pass
 
#CAVALLO
def Cavallo():
  pass
 
#####################################
 
#SCELTA DEL PROGRAMMA DA UTILIZZARE
 
using = True
 
while using:
 
  programma = input('Digita la lettera corrispondente in elenco al programma che desideri utilizzare, quindi premi invio')
  print()
 
  if programma == 'a':
    #INTRO KNAPSACK
    Minerali()
 
  elif programma == 'b':
    #ISTRUZIONI CRITTOGRAFIA
    Crittografia()
 
  elif programma == 'c':
    #ISTRUZIONI GRAFI
    Grafi()
 
  elif programma == 'd':
    #ISTRUZIONI SOTTOSEQUENZE
    Sottosequenze()
 
  elif programma == 'e':
    #ISTRUZIONI PIANIFICAZIONE
    Pianificazione()
 
  elif programma == 'f':
    #ISTRUZIONI FLUSSI IN UNA RETE
    Canali()
 
  elif programma == 'g':
    #ISTRUZIONI ROBOT
    Robot()
 
  elif programma == 'h':
    #ISTRUZIONI REGOLE E DEDUZIONI
    Regole()
 
  elif programma == 'i':
    #ISTRUZIONI FATTI E CONCLUSIONI
    Fatti()
 
  elif programma == 'j':
    #ISTRUZIONI CAVALLO
    Cavallo()
  else:
    print ('La lettera da te inserita non e\' valida!')
 
  continuare = input('Continuare a usare il proramma?(s/n)')
  if continuare == 'n':
    using = False
    print ('Grazie per aver usato questo programma! ')
