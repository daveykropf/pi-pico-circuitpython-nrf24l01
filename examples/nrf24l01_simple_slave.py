"""
Simple example of using the RF24 class.
"""
import time
import struct
import board
import busio
from digitalio import DigitalInOut

# if running this on a ATSAMD21 M0 based board
# from circuitpython_nrf24l01.rf24_lite import RF24
from circuitpython_nrf24l01.rf24 import RF24

SPI_BUS = busio.SPI(board.GP6, MOSI=board.GP7, MISO=board.GP4)
CE_PIN = DigitalInOut(board.GP12)
CSN_PIN = DigitalInOut(board.GP5)

# initialize the nRF24L01 on the spi bus object
nrf = RF24(SPI_BUS, CSN_PIN, CE_PIN)
# On Linux, csn value is a bit coded
#                 0 = bus 0, CE0  # SPI bus 0 is enabled by default
#                10 = bus 1, CE0  # enable SPI bus 2 prior to running this
#                21 = bus 2, CE1  # enable SPI bus 1 prior to running this

# set the Power Amplifier level to -12 dBm since this test example is
# usually run with nRF24L01 transceivers in close proximity
nrf.pa_level = -12

# addresses needs to be in a buffer protocol object (bytearray)
address = [b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0"]

# set TX address of RX node into the TX pipe
nrf.open_tx_pipe(address[1])  # always uses pipe 0

# set RX address of TX node into an RX pipe
nrf.open_rx_pipe(1, address[0])  # using pipe 1

# using the python keyword global is bad practice. Instead we'll use a 1 item
# list to store our float number for the payloads sent
payload = [0.0]

# uncomment the following 3 lines for compatibility with TMRh20 library
# nrf.allow_ask_no_ack = False
# nrf.dynamic_payloads = False
# nrf.payload_length = 4

"""Polls the radio and prints the received value."""
nrf.listen = True  # put radio into RX mode and power up

while True:
    if nrf.available():
        # grab information about the received payload
        payload_size, pipe_number = (nrf.any(), nrf.pipe)
        # fetch 1 payload from RX FIFO
        buffer = nrf.read()  # also clears nrf.irq_dr status flag
        # expecting a little endian float, thus the format string "<f"
        # buffer[:4] truncates padded 0s if dynamic payloads are disabled
        payload[0] = struct.unpack("<f", buffer[:4])[0]
        # print details about the received packet
        print(
            "Received {} bytes on pipe {}: {}".format(
                payload_size, pipe_number, payload[0]
            )
        )
