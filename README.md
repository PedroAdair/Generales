# Códigos en consola

## Instalar miniconda
https://docs.anaconda.com/free/miniconda/#quick-command-line-install

## Git
```
git config --global user.name <UserName>
git config --global user.email <Email>
```
Para revisar el historial de cambios, para consultar los archivos modificados
```
git status
```
Para agregar los cambios realizados (con . es para todos los cambios, mientras que si uno especifica el nombre del archivos, estas actualizaciones seran unicamente  al archivos seleccionado)
```
git add .
```
Para comprobar que se agregaron los cambios, nuevamente ejecutamos
```
git status
```
Para agregar una descripcion breve de los cambios y realiza
```
git commit -m "Aqui damos una descripcion detallada"
```
Para descargar los cambios realizados en el proyecto, se aplica el siguiente comando
```
git pull origin <Nombre de la rama>
```

Finalmente, 
```
git push
```
Para realizar el merge de dos ramas:
1. Confirmamos el nombre de la rama destino (sobre la cual haremos la fusion, ejemplo **main** o **master**)
```
git checkout <Rama Destino>
```



2. 
## Conda
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
Para saber los nombres de los entornos disponibles en nuestro ordenador
```
conda env list
```
Una vez sabemos el nombre del entorno que queremos activar, realizamos el siguiente comando
```
conda activate <Nombre_Entorno> 
```
Para crear un archivo capaz de crear un entorno para Linux y Windows:
```
conda env export --no-builds > environment.yaml 
```
Para eliminar un entorno
```
conda remove --name  <Env_Name> --all
```
 `rgb(9, 105, 218)`

## pip
Para crear un archivo de requirements
```
pip freeze > requierements.txt
```
Para creat un entorno a partir de un archivo de requisitos en formato *txt*
```
pip install -r /path/to/requirements.txt
```

https://docs.github.com/es/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme
