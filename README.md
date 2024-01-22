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

3. Sigue el [tutorial](https://github.com/Toimil/WhatsApp-Google-Forms-Bot#tutorial-para-habilitar-la-api-de-google) facilitado en este documento para habilitar la API de Google. 

4. Crea un formulario de google y selecciona que **se cree un google sheets de ese formulario**.

5. **Comparte ese google sheets con el correo** que se creó en el tutorial que será de la forma aaaaaa@aaaaaa.iam.gserviceaccount.com.

6. Modifica la primera parte del código [whatsapp_google_forms_bot.py](https://github.com/Toimil/WhatsApp-Google-Forms-Bot/blob/main/whatsapp_google_forms_bot.py) para adaptarlo a tus necesidades:

    * Deberás indicar el mensaje con el cual se notificará a las personas cuando cubran el formulario de Google, por ello, **modifica la variable *mensaje*** (puedes usar caracteres comodines para luego sustituirlos por lo que se introduzca en diversos campos del formulario).
    * Si realizaste el paso anterior utilizando algun caracter comodín, deberás indicar el campo del formulario que quieres que se sustituya en el lugar que se indica con comentarios en el código.
    
7. Tal como está diseñado el script, será necesario añadir dos nuevas columnas denominadas "Enviado" y "Entradas Disponibles", además, justo en la celda que se encuentra debajo de "Entradas Disponibles" deberás indicar con números las entradas que querrás repartir.
    
8. Antes de ejecutar el script accede al enlace [https://api.whatsapp.com/send?phone=34666666666&text=aaa](https://api.whatsapp.com/send?phone=34666666666&text=aaa) y **habilita siempre las redirecciones a la aplicación de escritorio de WhatsApp** 
    
9. Ejecuta el script mediante el comando **```python whatsapp_google_forms_bot.py```**, antes de ejecutarlo asegúrate que tienes la **aplicacion de WhatsApp abierta**.

10. Cuando desees **finalizar la ejecución** del bot tendrás que hacer ***ctrl + c*** en la ventana de la terminal.



## Tutorial para habilitar la API de Google

1. En primer lugar, accede a la web [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. A continuación, tendrás que seguir una serie de pasos que se detallan en los siguientes apartados y que se pueden visualizar en este gif
   <p align="center">
        <img src="https://github.com/Toimil/WhatsApp-Google-Forms-Bot/blob/main/tutorial.gif" alt="animated" />
    </p>

3. Primeramente deberás hacer click en "*selecciona un proyecto*" y, posteriormente, pulsar en "*proyecto nuevo*". A continuación, escribes el nombre con el que vas a identificar al proyecto y le das a "*crear*".
4. Ahora en la pestaña que se abre tras pulsar "*selecciona un proyecto*" te aparecerá el proyecto que acabas de crear, ahora tendrás que hacer click en él y en la pestaña que se te abre seleccionar el apartado denominado "*panel*".
5. En la barra de búsqueda que puedes encontrar en la parte superior de tu pantalla escribirás "*google drive api*" y clickar el primer resultado que te aparece de la búsqueda, tras esto, le das a "*habilitar*".
6. Una vez realizado el paso anterior, deberás repetirlo pero escribiendo en este caso "*google sheets api*".
7. Tras habilitar "*google sheets api*" tendrás que hacer click en el apartado de credenciales que se encuentra en la parte izquierda de la pantalla. Después de realizar lo descrito anteriormente, deberás pulsar en "*administrar cuentas de servicio*" y, en la pestaña que se te abrirá, seleccionar "*crear cuenta de servicio*".
8. A continuación, observarás que debes introducir unos datos de los cuales basta con cubrir el "*nombre de la cuenta de servicio*" escribiendo el nombre que desees y pulsar "*crear y continuar*".
9. Posteriormente, observarás un correo electrónico que deberás copiar ya que será de utilidad más tarde, además, deberás de clickar en los tres puntos y entre las opciones que te saldrán disponibles selecciona "*administrar claves*".
10. Para finalizar, presiona "*agregar clave*" y, en la pestaña emergente, selecciona el tipo de clave en formato "*JSON*". Por último, pulsa el botón de "*crear*". Se te descargará automáticamente un archivo que deberás **ubicarlo en la misma carpeta que en la que hayas clonado el repositorio**.

## Hecho con

* [Python 3](https://www.python.org/)
* [PyAutoGUI](https://github.com/asweigart/pyautogui)
* [gspread](https://github.com/burnash/gspread)
* [Oauth2client](https://github.com/googleapis/oauth2client)
* [Webbrowser](https://docs.python.org/es/3/library/webbrowser.html)

## Autor

* **Óscar Toimil**. - [Toimil](https://github.com/Toimil)


