#Comandos en conda 

Crear un entorno con una version especial de python 
```
conda create -n myenv python=3.9
```
Crear un entorno desde un archivo yml o yaml 
```
conda env create -f <Nombre_archivo.yaml> 
```
Exportar el archivo de entorno para crear nuevos:
```
conda env export > environment.yml  
```
Para crear un archivo capaz de crear un entorno para Linux y Windows:
```
conda env export --no-builds > environment.yaml 
```
Para eliminar un entorno
```
conda remove --name  <Env_Name> --all
```