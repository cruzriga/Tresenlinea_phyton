#CODING UTF-8
import os
import math
#SEL INIALIZA DOS MATRICES DE 3X3

#se crean la matrices 
numero_columnas = 3
numero_filas = 3
#matriz 1
#esta matriz es la que lleva los valores nuemericos de cada jugada para poder calcular quien es el ganador
Tab1 = [None] * numero_filas
for i in range(numero_filas):
    Tab1[i] = [None] * numero_columnas
# matriz 2
#esta matriz lleva las X o O y es la que se muestra en pantalla
Tab2 = [None] * numero_filas
for i in range(numero_filas):
    Tab2[i] = [None] * numero_columnas

# se inicializa la matriz 1 en 0 y la matriz 2 en " "
for i in range(numero_filas):
	for j in range(numero_columnas):
		Tab1[i][j] = 0
		Tab2[i][j] = " "

# variables
TurnoJugador1 = True
Terminado = False
Ganador = False
CantTurnos = 0

#dibuajar el tablero
while Terminado == False:
	#borrar pantalla
	os.system('clear')  # on linux / os x

	#pantalla del juego
	print(" ")
	print("      ||     ||  ")
	print("   "+Tab2[0][0]+"  ||  "+Tab2[0][1]+"  ||  "+Tab2[0][2])
	print("   1  ||  2  || 3")
	print(" =====++=====++======")
	print("      ||     || ")
	print("   "+Tab2[1][0]+"  ||  "+Tab2[1][1]+"  ||  "+Tab2[1][2])
	print("   4  ||  5  || 6")
	print(" =====++=====++======")
	print("      ||     || ")
	print("   "+Tab2[2][0]+"  ||  "+Tab2[2][1]+"  ||  "+Tab2[2][2])
	print("   7  ||  8  || 9")
	print(" ")

	#si no hay ganador y si aún hay turnos por jugar (max turnos son 9)
	if Ganador == False and CantTurnos < 9:
		#verifica de quien es el turno
		if  TurnoJugador1 == True:
			#ficha del jugador 1 y los valores para agregar en la matriz 1 
			Ficha ='O'
			Valor = 1
			# el objetivo es la multiplicacion de las lineas y digonales como la matriz esta llena de 1 debe ser igual a 1 (1x1x1)
			Objetivo = 1
			print("Turno del jugador 1 (X)")
		else:
			Ficha = 'X'
			Valor = 2
			# el objetivo es la multiplicacion de las lineas y digonales como la matriz esta llena de 2 debe ser igual a 8 (2x2x2)
			Objetivo = 8
			print("Turno del jugador 2 (O)")

		#pide la posición para colocar la ficha y la valida
		print("Ingrese la Posición (1-9):")
		# alternativa del do while en phyton
		# repite el bucle hasta que inserte un dato enterio y valido para la jugada
		while True:
			Pos = input()
			if (Pos != ""):
				Pos = int(Pos)
			
			if Pos <1 or Pos >9 :
				print("Posición incorrecta, ingrese nuevamente: ")
				Pos = 99
			else:
				#calculo la posicion del la jugada 
				i = math.trunc((Pos-1)/3)
				j =((Pos-1) % 3)
				if Tab1[i][j] != 0:
					Pos = 99
					print("Posición incorrecta, ingrese nuevamente: ")
			if Pos != 99:
				break
		#una vez jugado aumento la Cantidad de Turnos en 1 
		CantTurnos= CantTurnos+1
		#le asigno el valor a la matriz 1 y a la 2 le asigno la Ficha (X o O) para mostrar en pantalla
		Tab1[i][j]=Valor
		Tab2[i][j]=Ficha

		#se verifica que se gano buscando el producto
		aux_d1=1
		aux_d2=1

		for i in range(3):
			aux_i=1
			aux_j=1
			aux_d1=aux_d1*Tab1[i][i]
			aux_d2=aux_d2*Tab1[i][3-(i+1)]

			for j in range(3):
				aux_i=aux_i*Tab1[i][j]
				aux_j=aux_j*Tab1[j][i]

			if aux_i==Objetivo or aux_j==Objetivo:
				Ganador = True

		if aux_d1==Objetivo or aux_d2==Objetivo:
			Ganador = True
		else:
			#cambia de turno de jugardor 1 al jugador 2
			TurnoJugador1 = ~TurnoJugador1
	else:
		# ya realizado el proceso determina si quien es el ganador o si hubo empate
		# si hay ganador es el que quedo en turno 
		if Ganador == True:
			print("Ganador: ") 
			if TurnoJugador1 == True:
				print("Jugador 1!")
			else:
				print("Jugador 2!")
		else:
			print("Empate!")
		Terminado = True
