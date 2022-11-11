"""
Task 3

Echo server with asyncio

Create a socket echo server which handles each connection using asyncio Tasks.
"""
import asyncio


class AsyncEchoServer:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__clients = []

    async def handle_echo(self, reader, writer):
        addr = writer.get_extra_info('peername')
        print(f"Connected from {addr}")
        self.__clients.append(addr)
        while True:
            if writer.is_closing():
                writer.close()
                break
            data = await reader.read(1024)
            writer.write(data)
            await writer.drain()
        self.__clients.remove(addr)
        print(f"Disconnected from {addr}")

    async def main(self):
        server = await asyncio.start_server(self.handle_echo, self.__host, self.__port)
        async with server:
            await server.serve_forever()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(AsyncEchoServer("127.0.0.1", 32332).main())
