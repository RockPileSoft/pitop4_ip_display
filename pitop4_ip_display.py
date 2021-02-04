from pitop.miniscreen import Miniscreen, DownButton, UpButton
from time import sleep
import socket
import os

def get_Host_name_IP(): 
    try: 
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       s.connect(("8.8.8.8", 80))
       ip = s.getsockname()[0]
       # print(s.getsockname()[0])
       
       text = "IP : " + ip

       s.close()

       oled.display_multiline_text(text,[0,15], font_size=16)

       return 


    except: 
        print("Unable to get Hostname and IP")

def get_cpu_temp():
    
    result = 0.0
    
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
    
        if line.isdigit():
            
            result = round((float(line) / 1000),1)
    
    result_to_f = round((result * 1.8 + 32),1)
    tempC = " Temp: " + str(result) + " *C"
    tempF = "\n Temp: " + str(result_to_f) + " *F"
     

    total = tempC + tempF 
    
    oled.display_multiline_text(total,[0,15], font_size=16)
    

    
    
    return result

oled = Miniscreen()
down_button = DownButton()
up_button = UpButton()



while True:
    down_button.when_pressed = get_Host_name_IP
    up_button.when_pressed = get_cpu_temp
    sleep(10)
    oled.display_multiline_text("")
    
