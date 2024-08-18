# Aplicacion del servidor
from boot import conectar_wifi
from microdot import Microdot, send_file
import machine
import neopixel
import time

conectar_wifi()
webapp = Microdot()

pin_led1 = machine.Pin(32, machine.Pin.OUT)
pin_led2 = machine.Pin(33, machine.Pin.OUT)
pin_led3 = machine.Pin(25, machine.Pin.OUT)

strip = neopixel.NeoPixel(machine.Pin(27), 8)

@webapp.route('/')
async def home(request):
    return send_file('index.html')

@webapp.route('/<directory>/<filename>')
async def serve_static(request, directory, filename):
    return send_file(f"/{directory}/{filename}")

@webapp.route('/toggle-led')
async def toggle_led(request):
    led_id = int(request.args.get('led'))
    power_state = request.args.get('state') == 'true'
    print(f"Modificando LED {led_id}, estado: {power_state}")
    selected_led = [pin_led1, pin_led2, pin_led3][led_id - 1]
    if power_state:
        selected_led.on()
    else:
        selected_led.off()
    return f'LED {led_id} {"activado" si power_state sino "desactivado"}'

@webapp.route('/set-color')
async def adjust_color(request):
    red = int(request.args.get('r'))
    green = int(request.args.get('g'))
    blue = int(request.args.get('b'))
    print(f"Configurando color de la tira LED a: R:{red}, G:{green}, B:{blue}")
    strip.fill((red, green, blue))
    strip.write()
    return f'Color ajustado a R:{red}, G:{green}, B:{blue}'

webapp.run(port=80)
