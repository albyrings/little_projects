

print('stai risolvendo ATTIVITA RAGAZZI by ALBERTO ANELLI. Per un utilizzo piu fluido correggere tutti i range dei cicli for ricordandosi la regola del +1 ')
a=[0,0,0,0,0,0,0,0,0,0,0,0,0,]
n=0

t=int(input('numeri di attivita:'))
print('inserire i numeri di giorni per le attivita superflue come numero di giorni:0')
for i in range(1,t+1):
  a[i]=int(input('numero di giorni='))


sinfoli=int(input('numeri di singoli:'))

for j in range(1,sinfoli+1):

 singoli=int(input('singoli='))
 n=n+a[singoli]
quantitadicoppie= int(input('quantitadicoppie='))
for j in range(1,quantitadicoppie+1):
  allineati1a=int(input('allineati1a=')) 
  
  allineati1b=int(input('allineati1b=')) 
  allineati1c=int(input('allineati1c=')) 
  allineati2a=int(input('allineati2a=')) 
  allineati2b=int(input('allineati2b=')) 
  allineati2c=int(input('allineati2c=')) 

  if a[allineati1a]+a[allineati1b]+a[allineati1c]>a[allineati2a]+a[allineati2b]+a[allineati2c]:
    n=n+a[allineati1a]+a[allineati1b]+a[allineati1c]
  else:
    n=n+a[allineati2a]+a[allineati2b]+a[allineati2c]
  
v=str(n)
print('numero di giorni:'+v)
print('ben fatto')
