# WhatsApp-Google-Forms-Bot

WhatsApp-Google-Forms-Bot es un bot que envía un WhatsApp a las personas que cubren un formulario de google (Google Forms) con la idea de notificarlas de su reserva en una actividad.

Fue desarrollado para el Paso de Informática de la USC (Universidad de Santiago de Compostela) en el curso 2022-23.


## Por qué fue creado este bot?

Este bot fue creado para facilitar la tarea de enviar un mensaje de confirmación a las personas que han reservado una actividad con el paso. De esta forma, no es necesario tener que enviarles un correo electrónico o un md por Instagram.


## Compilación y ejecución

### Prerrequisitos

Necesitarás disponer de:

* Un espacio de trabajo con **Python**.

* Un **número de teléfono**.

* Tener una **cuenta de WhatsApp** con ese número de teléfono.


### Ejecución del bot

1. Clona este repositorio en tu sistema mediante ```git clone https://github.com/Toimil/CV-USC-Notifier-Bot``` o descárgalo colocando todos los archivos en el mismo directorio.

2. Instala todas las librerias mencionadas en [requirements.txt](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/requirements.txt) y así asegurar un correcto funcionamiento del bot, para ello, ejecuta el siguiente comando ```pip install -r requirements.txt```

3. Modifica la primera parte del código [notificaciones_cv.py](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/notificaciones_cv.py) para adaptarlo a tus necesidades:

    * Deberás indicar las URLs de las asignaturas de las cuales quieres ser notificado cuando se realice un cambio en estas, por ello, **modifica la lista *URLs***.
    * A su vez, debes **modificar la lista *subjectNames*** y poner el nombre de las asignaturas en el mismo orden en el que fueron introducidas las URLs.
    * Además, podrás modificar el icono con el que se ejecutará el bot e indicar la imagen que quieras.
    * Por último, **debes indicar tu correo electrónico y tu contraseña del campus virtual así como tu *execution***. Para obtener lo mencionado anteriormente, se ha facilitado un [*tutorial*](#tutorial-para-obtener-tu-execution).

4. Ejecuta el script mediante el comando **```python3 notificaciones_cv.py```**

5. Cuando desees finalizar la ejecución del bot tendrás que hacer ***click derecho*** en el icono y pulsar la opción ***Salir***.



## Tutorial para crear una cuenta en Google Developers

1. En primer lugar, accede a la web [de Google Developers](https://developers.google.com/profile/u/me?authuser=3) y crea un perfil.
2. Entrar en https://console.cloud.google.com/ 
3. Compartir el excel con el correo que nos ha aparecido

2. Antes de pulsar *Identificarse* haz click derecho y selecciona ***Inspeccionar*** o si lo prefieres puedes hacer la combinacion de teclas ***```Ctrl + Shift + I```***.


## Tutorial para obtener tu *"execution"*

1. En primer lugar, accede a la web [cv.usc.es](https://login.usc.es/cas/login?service=https%3A%2F%2Fcv.usc.es%2Flogin%2Findex.php) y escribe tus credenciales como si estuvieras realizando un login normal.

2. Antes de pulsar *Identificarse* haz click derecho y selecciona ***Inspeccionar*** o si lo prefieres puedes hacer la combinacion de teclas ***```Ctrl + Shift + I```***.

3. Ahora la secuencia de pasos variará dependiendo del navegador que estés utilizando. A continuación, se muestra como se realizaría para Google Chrome y Mozilla Firefox.

   * Google Chrome:
      <p align="center">
        <img src="https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Explicaciones/explicacion_chrome.gif" alt="animated" />
      </p>
    * Mozilla Firefox:
      <p align="center">
        <img src="https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Explicaciones/explicacion_firefox.gif" alt="animated" />
      </p>

## Capturas de pantalla de la ejecución
   
![](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Screenshots/2817.jpg)        ![](https://github.com/Toimil/CV-USC-Notifier-Bot/blob/main/Screenshots/2818.jpg)

## Aviso

**Si el bot deja de funcionar o las notificaciones salen sin motivo alguno es porque es necesario volver a introducir otro nuevo valor para *execution* en el código, para ello volver a repetir el proceso descrito anteriormente**.

## Posibles mejoras

En un futuro sería de gran interés modificar el bot para que sea multiplataforma, es decir, que se pueda usar además de en Windows en otros sistemas como diversas distribuciones de Linux.

Además, otra posible mejora a realizar, es alojar el bot en un servidor para que no haya que tener el ordenador encendido todo el tiempo ejecutando continuamente el script.

## Hecho con

* [Python 3](https://www.python.org/)
* [Win10Toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
* [Pystray](https://github.com/moses-palmer/pystray)

## Autor

* **Óscar Toimil** - [Toimil](https://github.com/Toimil)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
