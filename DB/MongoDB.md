# Mongo DB
Crear una coneccion local en MongoDb apoyandonos de Docker
```
docker run -p 27023:27017 --name local-mongo3 -d mongo
```
```
mongodb://localhost:27023/
```
## PyMongo
MongoDb es un sistema de base de datos no estructurada (NoSQL), en el caso de Python se tiene uso de la libreria  [PyMongo](https://github.com/mongodb/mongo-python-driver). la cual contiene su instalacion mediante pip.
```
pip install pymongo
```
Mientras que la manera de consumirla dentro de nuestros archivos.py es mediante el cientede Mongo. a continuacion un ejemplo
```
from pymongo import MongoClient
```
Uno de los primero pasos consiste en acceder a una coleccion dentro de una base de datos, se recomienda usar la siguiente función:
```
def coneccionDB(mongo_uri:str,database_name:str,collection_name:str):
    '''Permite realizar una coneccion a una colecccion en base de datos'''
    try:
        client = MongoClient(mongo_uri)
        db = client[database_name]
        collection = db[collection_name]
        print(f'coneccion exitosa a la coleccion: {database_name}.{collection_name}')
    except Exception as e:
        print(e)

    return collection 
```

## a