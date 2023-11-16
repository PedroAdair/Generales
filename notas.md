
Se creo un entorno compatible a Copnstanza con Python 3.11.4
```
conda create -n TrialsDiego python=3.11.4
```
Posteriormente se activo dicho entorno

```
conda activate TrialsDiego
```
ahora se instalo una libreria para un modelo TextToSpeech [![Prototipo - v1.1](https://img.shields.io/static/v1?label=Pip&message=gTTS&color=#2986cc&logo=Google)](https://pypi.org/project/gTTS/)

```
pip install gTTS==2.4.0
```
Revisar si ya la tienes instaklada

```
pip show gTTS
```