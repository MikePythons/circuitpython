import adafruit_bus_device.i2c_device

class Simple_AT24C02():
    AT24C02_DEFAULT_ADDR = 0x50

    def __init__(self, i2c, address=AT24C02_DEFAULT_ADDR, probe=True):
        self.i2c_device = adafruit_bus_device.i2c_device.I2CDevice(i2c, address, probe)

    def read_byte(self, address) -> int:
        response = self.read_bytes(address, 1)
        return response[0]

    def read_bytes(self, starting_address, count) -> bytearray:
        page = bytearray([starting_address])
        buffer = bytearray(count)
        with self.i2c_device as device:
            device.write_then_readinto(out_buffer=page, in_buffer=buffer)
        return buffer

    def write_bytes(self, starting_address, bytes: bytearray):
        count = len(bytes)
        if count > 8:
            raise ValueError("Cannot write more than 8 bytes in one operation")
        if starting_address + count > 255:
            raise ValueError("Cannot write. Addresses exceed maximum range")
        out_msg = bytearray([starting_address]) + bytes
        with self.i2c_device as device:
            device.write(out_msg)

    def write_page(self, page_address, bytes):
        if len(bytes) > 8:
            raise ValueError("Cannot write more than 8 bytes in one operation")
        if not 0 <= page_address < 32:
            raise ValueError("Page address must be between 0 and 32")
        self.write_bytes(page_address*8, bytes)