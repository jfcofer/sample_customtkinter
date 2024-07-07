# Prueba de CustomTKinter

Esta prueba tiene de forma, todo lo que se deberá implementar más a detalle
en las siguientes semanas:

## Estructura


***lib:*** la aplicación

***packages:*** las conexiones a la base de datos


#### Lib
Generalmente todas las partes de esta carpeta 
se separan en **view**, y proximamente **bloc (o logic)**

**view:** lo que se ve dentro de la aplicacion,

**bloc:** con la lógica de conexión al repositorio
(eso lo subiré proximamente)

Existen dos carpetas, app y modulos,

la app es la etapa inicial y donde se realizan las configuraciones de la misma,

los modulos se refieren mas a las partes individuales de la aplicacion y que generalmente deben estar lo mas separados el uno del otro

#### Packages

se separan en **repository** y **apis**
los repositorios son para la abstraccion de la logica
de las llamadas a la base de datos, conexiones y otras cosas
usando el polimorfimes de las apis


en las apis siempre debe haber una abstracta, que es la que se usa
en el repositorio, y la implementacion concreta que es la que 
se instancia directamente en la aplicacion


## Que paquetes se usan

sqlalchhemy


## Como instalar

```python
python -m venv .venv
pip install -r requirements
```

