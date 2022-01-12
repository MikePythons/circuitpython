from board import *
import busio

board_id = "mikepython_smolduino_ohno"

_I2C0 = None
_I2C1 = None
_SPI0 = None
_SPI1 = None
_UART = None


SDA0 = GP24
SCL0 = GP25
SDA1 = GP18
SCL1 = GP19

SCK0 = GP22
MOSI0 = GP23
MISO0 = GP20
SCK1 = GP14
MOSI1 = GP11
MISO1 = GP12
CS1 = GP13

RX = GP5
TX = GP4

# 5V shifted outputs
HV_OUT_A = GP15
HV_OUT_B = GP16
HV_OUT_CLOCK = SCK1
HV_OUT_DATA = MOSI1

CHARGE_DISABLE = GP21

def I2C():
    global _I2C0

    if not _I2C0:
        _I2C0 = busio.I2C(SCL0, SDA0)

    return _I2C0


def I2C1():
    global _I2C1

    if not _I2C1:
        _I2C1 = busio.I2C(SCL1, SDA1)

    return _I2C1


def STEMMA_I2C():
    return I2C1()


def SPI(): # 2x3 SPI header
    global _SPI0

    if not _SPI0:
        _SPI0 = busio.SPI(SCK0, MOSI0, MISO0)

    return _SPI0


def SPI1():
    global _SPI1

    if not _SPI1:
        _SPI1 = busio.SPI(SCK1, MOSI1, MISO1)

    return _SPI0


def UART(baudrate=9600):
    global _UART

    if not _UART:
        _UART = busio.UART(TX, RX, baudrate=baudrate)

    return _UART

