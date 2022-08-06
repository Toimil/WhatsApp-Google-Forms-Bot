#!/usr/bin/env python3

'''
Bot que envía un WhatsApp a las personas que cubren un google forms notificándoles de su reserva en una actividad

Desarrollado para el Paso de Informatica de la USC (Universidad de Santiago de Compostela) 2022-23

© 2022 Toi1000, Santiago de Compostela, España ©
https://github.com/Toimil
'''


# Mensaje que queremos enviar (podemos usar caracteres comodines para luego sustituirlos por el nombre por ejemplo)
mensaje = """Hola ##### &&&&&!
Desde el Paso de Informática confirmamos tu interés en asistir a la *cena de inicio de curso*.
El plazo de pago es hasta el  martes 21, después se liberarán las reservas.
Puedes pagar en efectivo en la mesa del paso indicando tu *DNI*.

Te esperamos!"""


# Añadir dos columnas a la hoja de calculo que sean en este orden: Notificado y Entradas disponibles
# En contador escribir debajo el numero de entradas que queremos repartir

credenciales = "credentials.json"  # archivo en el que se encuentran nuestras credenciales de la API de Google (debe estar en el mismo directorio)
spreadsheet = "Respuestas"  # hoja de calculo que queremos actualizar (previamente compartida con la cuenta de gserviceaccount que aparece en las credenciales)
nombre_columna_num_tfno = "Número de teléfono"   # como se llama la columna en la que se encuentra el número de teléfono




# Realizamos los imports necesarios
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time
import webbrowser as web
import pyautogui as pg
from urllib.parse import quote
from platform import system
import os



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(credenciales, scope)
client = gspread.authorize(credentials)



# -----------------------------------------------------------------------------
# ------------------------------- FUNCIONES -----------------------------------

def cerrar_ventana(tiempo_espera):
    """Cerramos la pestaña del navegador abierta actualmente
    tiempo_espera: tiempo de espera para que se cierre la ventana en segundos
    """
    time.sleep(tiempo_espera)
    if system().lower() in ("windows", "linux"):
        pg.hotkey("ctrl", "w")
    elif system().lower() == "darwin":
        pg.hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} no soportado!")
    pg.press("enter")


def registrar_mensaje(_time: time.struct_time, receptor: str, mensaje: str) -> None:
    """Registra la información del mensaje enviado en un archivo de texto
    _time: objeto time.struct_time con la hora de envío del mensaje
    receptor: número de teléfono del receptor del mensaje
    mensaje: mensaje enviado"""

    if not os.path.exists("Mensajes_Enviados.txt"):
        file = open("Mensajes_Enviados.txt", "w+")
        file.close()

    with open("Mensajes_Enviados.txt", "a", encoding="utf-8") as file:
        file.write(
            f"Fecha: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nHora: {_time.tm_hour}:{_time.tm_min}\n"
            f"Número de Telefono: {receptor}\nMensaje: {mensaje}"
        )
        
        file.write("\n--------------------\n")
        file.close()


def enviar_whatsapp(num_tfno, mensaje, tiempo_espera, close_time):
    """Envía un mensaje de WhatsApp a un número de teléfono
    num_tfno: número de teléfono al que se quiere enviar el mensaje
    mensaje: mensaje que se quiere enviar
    tiempo_espera: tiempo de espera antes de que se envíe el mensaje al numero de telefono
    close_time: tiempo de espera para que se cierre la ventana del navegador despues de enviar el mensaje   
    """

    web.open(f"https://api.whatsapp.com/send?phone={num_tfno}&text={quote(mensaje)}")
    time.sleep(tiempo_espera)
    pg.press("enter")
    registrar_mensaje(_time=time.localtime(), receptor=num_tfno, mensaje=mensaje)
    web.open("https://google.com")
    cerrar_ventana(tiempo_espera=close_time)
    cerrar_ventana(tiempo_espera=close_time)


def main():
    """Función principal del programa
    """
    while(1):
        sheet = client.open(spreadsheet).sheet1  # Abrimos la hoja de calculo

        data = sheet.get_all_records()  # Obtenemos los datos en una lista de diccionarios
        #pprint(data)

        for index in range(len(data)): # Recorremos todas las filas (sin contar encabezados)
            for key in data[index]: # Recorremos todas las columnas
                
                # Si la columna es el número de teléfono y el valor de esta no está vacío y el valor de la columna Notificado para ese numero es distinto de "Si"
                if (key == nombre_columna_num_tfno and str(data[index][key]) != "" and sheet.cell(index+2,len(data[index])-1).value != "Si"):
                    
                    # Comprobamos que el número de teléfono sea válido, es decir, tenga 9 numeros
                    if(len(str(data[index][key])) != 9 or not str(data[index][key]).isdigit()):
                        print("Número de teléfono inválido --> " + str(data[index][key]))
                        continue # Termina esta iteración del for y continua con la siguiente

                    
                    # Sustituimos en el mensaje los caracteres comodines por el nombre y apellidos de la persona
                    x = mensaje.replace("#####", data[index]["Nombre"])
                    y = x.replace("&&&&&", data[index]["Apellidos"])

                    
                    
                    # Obtenemos el valor del numero de entradas disponibles
                    val = int(sheet.cell(2, len(data[index])).value)
                    if val <= 0: # Si no quedan entradas disponibles mostramos un mensaje por pantalla
                        print("Entradas agotadas")
                        exit()
                    
                    try:
                        enviar_whatsapp("34" + str(data[index][key]), y, 2, 1)            

                        # Actualizamos la columna Notificado para ese numero y ponemos el valor "Si"
                        sheet.update_cell(index+2,len(data[index])-1, "Si")

                        # Decrementamos el contador de entradas disponibles
                        val = val - 1
                        sheet.update_cell(2,len(data[index]), str(val))
                    except:
                        print("Error al enviar whatsapp al numero ", str(data[index][key]))

        time.sleep(5)

# -----------------------------------------------------------------------------




if __name__ == "__main__":
   print("Iniciando el bot...")
   main()
   