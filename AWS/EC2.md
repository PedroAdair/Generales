## EC2 de AWS

### Crar una instancia de EC2 en AWS



### Instalar Conda en la EC2/Linux
En el primer paso es abrir la estancia recien creada, para esto haremos uso de la instalacion en una linea de [miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)

1. Crear una carpeta llamada **miniconda3**.
```
mkdir -p ~/miniconda3
```

2. Se clona la informacion del repositorio anaconda para **linux** en la carpeta recien creada.
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
```

3. Se ejecuta el bash  **miniconda.sh** que contiene la información 
```
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
```

4. Finalmente se **remueve** el archivo bash
```
rm -rf ~/miniconda3/miniconda.sh
```


Ahora, se inicializa miniconda. Para esto sera necesario reiniciar la instancia de aws, se ejecutan los siguientes comandos.

```
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

Finalmente, se comprueba que todo funciona de manera exitosa con el siguiente comando:

```
conda --version
```

### Instalar Git en la EC2
0. Actualizar yum en caso de ser necesario.
```
sudo yum update -y
```
1. Instalar git 
```
sudo yum install git -y
```

2. Se comprueba que se haya instalado de manera exitosa Git
```
git --version
```
3. Iniciar las credenciales de GitHub para conectar nuestra cuenta
```
git config — global user.name “Your Name”
git config — global user.email “your_email@example.com”
```

### Instalar Tmux en la EC2

tmux permite tener multiples terminales abierta, dividir la terminal en pestañas y enn general tener un mejor control de las temrinales.

```
sudo yum install tmux
```

A continuacion algunos ejemplos:


| Comando | Descripcion             | Ejemplo   |
|---------|-------------------------|-----------|
| tmux ls | Listar sesiones activas | tmux ls   |
| tmux attach-session -t *name_of sesssion* | acceder a una session conociendo su nombre | tmux attach-session -t API|