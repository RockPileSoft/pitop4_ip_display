from pitop.miniscreen import OLED, DownButton, UpButton
from time import sleep
import socket
import os

def get_Host_name_IP(): 
    try: 
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       s.connect(("8.8.8.8", 80))
       ip = s.getsockname()[0]
       print(s.getsockname()[0])
       
       text = "IP : " + ip

       s.close()

       oled.draw_multiline_text(text, font_size=14)

       return 


    except: 
        print("Unable to get Hostname and IP")

def get_cpu_temp():
    
    result = 0.0
    
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
        # Test if the string is an integer as expected.
        if line.isdigit():
            # Convert the string with the CPU temperature to a float in degrees Celsius.
            result = round((float(line) / 1000),2)
    # Give the result back to the caller.
    result_to_f = round((result * 1.8 + 32),2)
    tempF = "Temp: " + str(result_to_f) + " *F"
    tempC = " Temp: " + str(result) + "  *C "

    total = tempC + tempF 
    
    oled.draw_multiline_text(total, font_size=14)
    return result

oled = OLED()
down_button = DownButton()
up_button = UpButton()



while True:
    down_button.when_pressed = get_Host_name_IP
    up_button.when_pressed = get_cpu_temp
    sleep(10)
    oled.draw_multiline_text("", font_size=14)
    
