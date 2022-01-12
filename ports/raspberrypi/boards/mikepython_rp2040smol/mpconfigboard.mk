USB_VID = 0x1209
USB_PID = 0x2040
USB_PRODUCT = "RP2040smol"
USB_MANUFACTURER = "MikePython"

CHIP_VARIANT = RP2040
CHIP_FAMILY = rp2

EXTERNAL_FLASH_DEVICES = "W25Q64JVxM"

CIRCUITPY__EVE = 1

FROZEN_MPY_DIRS += $(TOP)/ports/raspberrypi/boards/mikepython_rp2040smol
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_BusDevice
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_Register
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_LC709203F