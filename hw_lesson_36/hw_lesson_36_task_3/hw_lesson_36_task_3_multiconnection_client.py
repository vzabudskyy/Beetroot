import asyncio
from time import sleep


class AsyncEchoClient:
    def __init__(self, host, port, conn_amount=1):
        self.__host = host
        self.__port = port
        self.__conn_amount = conn_amount

    async def echo_to_server(self):
        reader, writer = await asyncio.open_connection(self.__host, self.__port)
        try:
            while True:
                sleep(1)
                writer.write(f"Hello, I'm client {writer.get_extra_info('sockname')}".encode())
                await writer.drain()
                data = await reader.read(100)
                print(f'Received: {data.decode()!r}')
        except KeyboardInterrupt:
            writer.close()

    async def run(self):
        tasks = [asyncio.create_task(self.echo_to_server()) for _ in range(self.__conn_amount)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(AsyncEchoClient("127.0.0.1", 32332, 5).run())
    """
        If there are some troubles with this client,
        use the client from hw_lesson_34._.'
    """