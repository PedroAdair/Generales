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
