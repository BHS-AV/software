import asyncio
import serial_asyncio


class Output(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print('port opened', transport)
        transport.serial.rts = False
        #transport.write(b'hello world\n')

    def data_received(self, data):
        print('data received', repr(data))
        #self.transport.close()

    def connection_lost(self, exc):
        print('port closed')
        asyncio.get_event_loop().stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = serial_asyncio.create_serial_connection(loop, Output, 'COM7', baudrate=115200)
    loop.run_until_complete(coro)
    loop.run_forever()

