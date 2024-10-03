import asyncio


async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman('Samson', 3)),
        asyncio.create_task(start_strongman('Gilgamesh', 4)),
        asyncio.create_task(start_strongman('Heracles', 5)),
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(start_tournament())
