# Sincronizacion: Exclusión Mutua y Seccion Crítica

## Video Clase 3 - Codigo Fuente
```
raceConditionBank.py
raceConditionBankLock.py
```

## Ejercicio:

```
globalContador.py
```
El siguente programa lanza un conjunto de threads cuyo código es un contador que incrementa una variable glogal una determinada cantidad. El resultado del programa es la impresión del contenido final de la variable global  **contador**

Leer y analizar el código y tratar de deducir que hace cada bloque.

## Preguntas (responder en el campus):

1. Cual es el valor esperado de la variable ***contador***. En que condiciones se obtendría este valor esperado.
2. Ejecute el programa varias veces y explicar a que se deben los resultados que observa.
3. Identifique las Secciones Críticas (escribir las lineas en la respuesta).
4. Modifique el programa, utilizando Locks de modo que se asegure la exclusión mutua en las secciones críticas.
5. Que es una "condición de carrera"?
6. Que es una Sección Crítica
7. Que es la Exclusión Mútua?


<sub>[Daniel Buaon - unahur-progra-concu-1-2021](https://github.com/unahur-progra-concu-1-2021)</sub>
