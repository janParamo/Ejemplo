Proceso HorasEnMinutosYSegundos
	Definir horas1 Como Entero;
	Definir horas2 Como Entero;
	Definir minutos Como Entero;
	Definir segundos Como Entero;
	// Proceso 
	Escribir 'escriba la cantidad de horas: ';
	Leer horas1, horas2;
	minutos <- horas1*60;
	segundos <- horas2*3600;
	Escribir ' la conversion a minutos es: ', minutos;
	Escribir ' la coversion a segundos es: ', segundos;
FinProceso
