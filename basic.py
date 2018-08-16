from gpiozero import LED, Button

# led = LED(21)
relays = [LED(pin) for pin in [26, 20, 21]]
pump = relays[0]
fanlow = relays[1]
fanhigh = relays[2]

button = Button(16)

while True:
    if button.is_pressed:
        # led.on()
        for r in relays:
          r.on()
    else:
        for r in relays:
          r.off()
        # led.off()

        
