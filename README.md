# SOCIALTENNIS
------
<div style="text-align:center">
    <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Texto alternativo 1" width="200" style="display:inline">
    <img src="https://www.djangoproject.com/s/img/logos/django-logo-positive.png" alt="Texto alternativo 2" width="200" style="display:inline">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/1200px-SQLite370.svg.png" alt="Texto alternativo 3" width="200" style="display:inline">
</div>

------

SocialTennis es una plataforma de red social dedicada exclusivamente a los amantes del tenis. Conecta con jugadores, encuentra eventos y organiza partidos en un solo lugar.

## Screenshots de las Vistas
<div>
    <img src="https://github.com/elvis-codev/SocialTennis/blob/main/Screenshots/Screenshot%201%20-%20Pagina%20Inicio.png" width="200" />
    <img src="https://github.com/elvis-codev/SocialTennis/blob/main/Screenshots/Screenshot%202%20-%20Inicio%20Sesi%C3%B3n.png" width="200" />
    <img src="https://github.com/elvis-codev/SocialTennis/blob/main/Screenshots/Screenshot%205%20-%20Partidos.png" width="200" />
    <img src="https://github.com/elvis-codev/SocialTennis/blob/main/Screenshots/Screenshot_9%20-%20Crear%20Post%20.png" width="200" />
</div>

## 🌤️ Información de API para el Clima 🌤️

[WeatherAPI.com](https://www.weatherapi.com/) es un servicio que proporciona datos meteorológicos y pronósticos a través de una API (Interfaz de Programación de Aplicaciones). Esta API ofrece información detallada sobre el clima actual, pronósticos a corto y largo plazo, así como datos históricos.

## Características clave

Algunas características clave de WeatherAPI.com incluyen:

### 1. Datos precisos
Utiliza una combinación de fuentes de datos para proporcionar información meteorológica precisa y confiable.

### 2. API fácil de usar
Ofrece una API bien documentada y fácil de integrar en aplicaciones y sitios web.

### 3. Compatibilidad
La API es compatible con varios lenguajes de programación y plataformas, lo que la hace accesible para una amplia gama de desarrolladores.


<div>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJx089v3cq_xyJc0U0vPeDXkQ6vzO0TXAtqUQWf5oIqA&s?raw=true" alt="alt text" width="190"/>
<img src="https://github.com/elvis-codev/SocialTennis_Clima/blob/main/Screenshots/Screenshot_Codigo_API_view.png" alt="alt text" width="300"/>
<img src="https://github.com/elvis-codev/SocialTennis_Clima/blob/main/Screenshots/Screenshot_Codigo_API_home.png?raw=true" alt="alt text" width="300"/>
</div>

https://www.weatherapi.com/


## 🌧️ Screenshot API Clima 🌧️
<div>
<img src="https://github.com/elvis-codev/SocialTennis_Clima/blob/main/Screenshots/Screenshot%2010%20-%20Clima.png?raw=true" alt="alt text" width="400"/>
<img src="https://github.com/elvis-codev/SocialTennis_Clima/blob/main/Screenshots/Screenshot_Codigo_API_json.png" alt="alt text" width="300"/>
</div>

## Diagrama de Base de Datos
![alt text](https://github.com/elvis-codev/SocialTennis/blob/main/Diagrama%20Base%20de%20Datos/BasedeDatos_SocialTennis.png?raw=true)


## Requisitos de Instalación

Antes de comenzar con el desarrollo en este proyecto, asegúrate de tener los siguientes requisitos instalados en tu sistema:

- [Python](https://www.python.org/downloads/) (versión X.X o superior)
- [pip](https://pip.pypa.io/en/stable/installation/) (herramienta de gestión de paquetes de Python)

## Configuración del Entorno de Desarrollo

Sigue estos pasos para configurar el entorno de desarrollo:

1. Clona el repositorio desde GitHub:

```bash
git clone https://github.com/elvis-codev/SocialTennis
```

2. Instala las dependencias del proyecto desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

4. Abre tu navegador y accede a [http://localhost:8000/](http://localhost:8000/) para ver la aplicación en funcionamiento.

5. puedes ir a la url de [http://localhost:8000/data](http://localhost:8000/data) para cargar informacion por defecto

## Usuarios

| TIPO  | username  | password  |
|---|---|---|
| Admin  | renato12  | 1234  |
| Usuario  | renatoac  | renato12345 |



--- 


### Requirements.txt
```bash
Django==5.0.4
Pillow==10.3.0

asgiref==3.8.1
bitarray==2.9.2
bitstring==4.1.4
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
click==7.1.2
click-didyoumean==0.3.0
cryptography==42.0.5
Django==5.0.4
ecdsa==0.18.0
esptool==4.7.0
idna==3.6
intelhex==2.3.0
Jinja2==3.1.3
jmespath==1.0.1
MarkupSafe==2.1.5
p==1.4.0
pycparser==2.21
pyserial==3.5
PyYAML==6.0.1
reedsolo==1.7.0
requests==2.31.0
setuptools==69.1.1
six==1.16.0
sqlparse==0.4.4
template==0.7.6
toml==0.10.2
tzdata==2024.1
urllib3==2.2.1
```
