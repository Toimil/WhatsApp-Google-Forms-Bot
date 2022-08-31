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

* Tener instalada la **aplicación de escritorio de WhatsApp**.


### Ejecución del bot

1. Clona este repositorio en tu sistema mediante ```git clone https://github.com/Toimil/WhatsApp-Google-Forms-Bot``` o descárgalo colocando todos los archivos en el mismo directorio.

2. Instala todas las librerias mencionadas en [requirements.txt](https://github.com/Toimil/WhatsApp-Google-Forms-Bot/blob/main/requirements.txt) y así asegurar un correcto funcionamiento del bot, para ello, ejecuta el siguiente comando ```pip install -r requirements.txt```.

3. Sigue el tutorial facilitado en este documento para habilitar la API de Google. 

4. Con el correo que se creo, compartelo con el excel de tu forms.

5. Modifica la primera parte del código [whatsapp_google_forms_bot.py](https://github.com/Toimil/WhatsApp-Google-Forms-Bot/blob/main/whatsapp_google_forms_bot.py) para adaptarlo a tus necesidades:

    * Deberás indicar el mensaje con el cual se notificará a las personas cuando cubran el formulario de Google, por ello, **modifica la variable *mensaje*** (puedes usar caracteres comodines para luego sustituirlos por lo que se introduzca en diversos campos del formulario).
    * Si realizaste el paso anterior utilizando algun caracter comodín, deberás indicar el campo del formulario que quieres que se sustituya en el lugar que se indica con comentarios en el código.
    
6. Ejecuta el script mediante el comando **```python whatsapp_google_forms_bot.py```**

7. Cuando desees **finalizar la ejecución** del bot tendrás que hacer ***ctrl + c*** en la ventana de la terminal.



## Tutorial para habilitar la API de Google

1. En primer lugar, accede a la web [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. A continuación, tendrás que seguir una serie de pasos que se detallan en los siguientes apartados y que se pueden visualizar en este gif
   <p align="center">
        <img src="https://github.com/Toimil/WhatsApp-Google-Forms-Bot/blob/main/tutorial.gif" alt="animated" />
    </p>

4. Explicar los pasos...


## Hecho con

* [Python 3](https://www.python.org/)

## Autor

* **Óscar Toimil** - [Toimil](https://github.com/Toimil)


