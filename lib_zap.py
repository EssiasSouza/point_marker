import ssl
import certifi
import pywhatkit as kit
import socket
import logging

logging.basicConfig(level=logging.DEBUG)

def is_connected():
    try:
        context = ssl.create_default_context(cafile=certifi.where())
        socket.create_connection(("www.google.com", 443), context=context)
        return True
    except OSError as e:
        logging.error(f"Connection error: {e}")
        return False

def send_whatsapp_message(phone_number, message, hour, minute):
    if is_connected():
        try:
            logging.info("Sending message...")
            kit.sendwhatmsg(phone_number, message, hour, minute)
            logging.info("Message sent successfully")
        except kit.core.exceptions.InternetException as e:
            logging.error(f"InternetException: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
    else:
        logging.error("No internet connection. Please check your connection and try again.")

send_whatsapp_message("+5511983969219", "Hello, this is a test message.", 11, 55)
