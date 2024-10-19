import time
from machine import Pin

from boot import status_led


def main():
    second = 0
    minute = 0
    tick = 0
    led_state = status_led.value()  # Początkowy stan LED
    led_on_time = 3  # Czas włączenia LED w tickach (1 tick = 0.1 s)
    led_off_time = 10  # Czas wyłączenia LED w tickach (1 tick = 0.1 s)
    led_timer = 0  # Licznik do kontroli czasu migania LED

    while True:
        # Zarządzanie czasem (licznik sekund, minut)
        if tick == 10:  # 1 sekunda (tick = 0.1 sekundy)
            tick = 0
            second += 1
            if second == 59:
                second = 0
                minute += 1
            if minute == 15:
                machine.reset()  # Reset po 15 minutach
        time.sleep(0.1)  # Odstęp czasu dla ticka
        tick += 1

        # Miganie LED bez blokowania pętli
        led_timer += 1
        if led_state and led_timer >= led_on_time:  # LED włączony przez zadany czas
            status_led.off()
            led_state = False
            led_timer = 0  # Reset licznika
        elif not led_state and led_timer >= led_off_time:  # LED wyłączony przez zadany czas
            status_led.on()
            led_state = True
            led_timer = 0  # Reset licznika


main()
