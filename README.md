# Códigos en consola
##Powersell
```
git config --global user.email <Agregrar correo>
git config --global user.name <Agregar UserName >
```
## Conda
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
conda remove --name  "Env_Name" -all
```
 `rgb(9, 105, 218)`

## pip
Para un archivo de requirements
```
pip freeze > requierements.txt
```

https://docs.github.com/es/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme
