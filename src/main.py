from machine import Pin
import uasyncio as a

p2 = Pin(2, Pin.OUT)

async def main():
    while True:
        await a.sleep_ms(200)
        
        p2.on()
        await a.sleep_ms(1000)
        p2.off()
        await a.sleep_ms(200)
        p2.on()
        await a.sleep_ms(1000)
        p2.off()
        await a.sleep_ms(200)
        p2.on()
        await a.sleep_ms(1000)
        p2.off()
        await a.sleep_ms(200)

        p2.on()
        await a.sleep_ms(500)
        p2.off()
        await a.sleep_ms(200)
        p2.on()
        await a.sleep_ms(500)
        p2.off()
        await a.sleep_ms(200)
        p2.on()
        await a.sleep_ms(500)
        p2.off()
        await a.sleep_ms(200)

        print('SOS!')

a.run(main())