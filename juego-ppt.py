Nombre1= input("Como te llamas jugador 1?")
print('Bienvenido', Nombre1)
Nombre2= input("Como te llamas jugador 2?") 
print('Bienvenido', Nombre2)

jugador1= input('Comencemos ' + Nombre1 + ' cuentame que eliges para tu partida? Pieda? Papel? Tijera?: ' )
jugador2= input('Comencemos ' + Nombre2 + ' cuentame que eliges para tu partida? Piedra? Papel? Tijera?: ')


condicion1= jugador1== "piedra" and jugador2=="tijera"
condicion2= jugador1== "papel" and jugador2=="piedra" 
condicion3= jugador1=="tijera" and jugador2=="papel"

if jugador1== jugador2:
    print("Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("Felicitaciones " + Nombre1+ " eres el ganador!") 
else:
    print("Felicitaciones "+ Nombre2 +" eres el ganador!") 


