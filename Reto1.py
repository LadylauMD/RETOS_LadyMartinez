day= int(input("Seleccione dia de la semana\n 1.Lunes\n 2.Martes\n 3.Miercoles\n 4.Jueves\n 5.Viernes\n 6.Sabado\n 7.Domingo\n"))

if(day==1 or day==2 or day==3):
    p=2.00
if(day==4 or day==5):
    p=2.50
if(day==6 or day==7):
    p=3.00

time= int(input("Tiempo estacionado(minutos)\n"))

if(time>5):
    vp=(p/60)*time
else:
    vp=0.00

print("Total a pagar",vp)