## JFINDEX

Es un proyecto "UNIX" para calcular las Energías de los archivos generados por los experimentos Químicos.
## Requerimientos

Requiere python 3.

## Installation

Descarga el proyecto desde Github usando la opción zip o git clone. Mueve el proyecto JFINDEX a una carpeta en tu computador. 

Descomprime el archivo zip mediante consola o usando las herramientas del sistema operativo (click derecho descomprimir)
```
$unzip jfindex.zip
```
También puedes crear un alias en $ .bashrc. (en MAC OS se llama "bash_profile") Utiliza un editor de texto (vi, vim, nano u otro)
```
$ nano ~.bashrc
```
Y agrega esta ultima linea: 
```
alias jfindex='python /home/user/jfindex/jfindex.py'
```
la ruta es donde esta guardado el proyecto en tu computadora

## Ejecución
Debes tener los 3 archivos .log (proyecto JFINDEX), luego ejecutar el programa mediante el comando python

Versión Gráfica:
```
$ python /home/user/jfindex/jfindex.py'
```
Version Linea de Comandos:
```
$ python /home/user/jfindex/jfindex.py' more
```
o simplemente usado el alias jfindex:

Versión Gráfica:
```
$ jfindex
```
![](https://webdesign.s3-us-west-2.amazonaws.com/jfindex/jfindex.png)

Version Linea de Comandos:
```
$ jfindex more
```
![](https://webdesign.s3-us-west-2.amazonaws.com/jfindex/jfindex_more.png)
