import asyncio
import os

async def wait_for_directory_creation(directory_path):
    print(f"Ожидание создания директории {directory_path}...")

    while not await asyncio.to_thread(lambda: os.path.exists(directory_path)):
        await asyncio.sleep(1)

    print(f"Директория {directory_path} была создана!")

async def create_directory(directory_path):
    print(f"Создание директории {directory_path}...")
    await asyncio.to_thread(lambda: os.makedirs(directory_path, exist_ok=True))

async def main():
    directory_path = os.getcwd()
    Image_path = directory_path + '\Input_img'
    Output_path = directory_path + '\Output_img'

    # Запуск задачи создания директории/Run the directory creation task
    create_task_Image_path = asyncio.create_task(create_directory(Image_path))

    # Запуск задачи ожидаия создания директории/Running a task waiting for directory creation
    await wait_for_directory_creation(Image_path)

    # Ожидание завершения создания директории/Waiting for directory creation to complete
    await create_task_Image_path
# ___________________________________________________________________________________________________
# Запуск задачи создания директории/Run the directory creation task
    create_task_Output_path = asyncio.create_task(create_directory(Output_path))

    # Запуск задачи ожидаия создания директории/Running a task waiting for directory creation
    await wait_for_directory_creation(Output_path)

    # Ожидание завершения создания директории/Waiting for directory creation to complete
    await create_task_Output_path

