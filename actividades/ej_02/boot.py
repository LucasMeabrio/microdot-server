def conectar_wifi():
    import network
    from time import sleep
    wifi = network.WLAN(network.STA_IF)
    
    if not wifi.isconnected():
        print("Intentando conectarse a la red...")
        wifi.active(True)
        wifi.connect("Cooperadora Alumnos", "")
        
        while not wifi.isconnected():
            print("...", end="")
            sleep(0.25)
    
    print("Configuración de red:", wifi.ifconfig())

conectar_wifi()
