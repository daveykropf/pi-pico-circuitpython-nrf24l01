# Raspberry Pi Pico and nRF24L01(+) transceiver using Circuitpython
This Github Repo is showing you how to connect a Raspberry Pi Pico and nRF24L01(+) transceiver using Circuitpython.

# Introduction
I couldn't find a working example on the internet for using a nRF24L01(+) transceiver with a Raspberry Pi Pico with CircuitPython. I found the tutorials [How to easily connect a NRF24L01+ transceiver to your Raspberry Pi Pico](https://coffeebreakpoint.com/micropython/how-to-connect-a-nrf24l01-transceiver-to-your-raspberry-pi-pico/) and [Raspberry Pi Pico with nRF24L01 using MicroPython](https://bekyelectronics.com/raspberry-pi-pico-nrf24l01-micropython/), except these were made for MicroPython. After digging on the internet I found this cool library, named [CircuitPython_nRF24L01](https://circuitpython-nrf24l01.readthedocs.io/en/latest/index.html#using-the-examples). I looked very promising, except the code is not working on a Raspberry Pi Pico (RP2040).

## Wiring

| Pico                                | NRF24L01+ |
|-------------------------------------|-----------|
| Pin 36 / 3V3 Out                    | VCC       |
| Pin 38 / GND (or any other GND Pin) | GND       |
| Pin 16 / GP12                       | CE        |
| Pin 7 / GP5                         | CS        |
| Pin 9 / GP6                         | SCK       |
| Pin 10 / GP7                        | MOSI      |
| Pin 6 / GP4                         | MISO      |

![wiring-image](assets/pico-nrf2401-wiring.png)

**Note:** Add a capacitor between the VCC and GND pins of the nRF24L01 for better stability. In my case I added a 10uf capacitor which worked fine. 

## Using the examples

In general I used the original examples files from the [CircuitPython_nRF24L01](https://github.com/nRF24/CircuitPython_nRF24L01/) repo and made some small changes, like referring to the correct pins. So how to get this code working on your Pico?

> 1. Download the content of the [CircuitPython_nRF24L01](https://github.com/nRF24/CircuitPython_nRF24L01/) repo.
> 2. Copy the `circuitpython_nrf24l01` folder in your lib folder on your Pico.
> 3. Download in this repo the correct example file and rename it to `main.py` or `code.py`
> 4. Profit

The folder sturcture on your Pico should be something like this

![folder-structure-pico](assets/files-on-pico.png)
