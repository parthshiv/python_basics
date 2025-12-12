"""
multi_processing is called CPU-bound task. Multiprocessing in Python is a way to run multiple processes at the same time. CPU-bound tasks are not accelerated by threads or asyncio — for CPU-heavy tasks, you need multiprocessing.
CPU-bound = heavy computation (like image processing, math calculations, encryption)
Example:
--------
Threads = multiple workers in same office sharing tools (memory) → can help with some tasks, but one tool at a time slows down CPU-heavy work

Multiprocessing = multiple workers in separate offices → each has their own tools → can work independently on heavy tasks
"""
from multiprocessing import Process
import time
import requests

def download_image(url, index):
    print(f"Process {index} downloading {url}...")
    response = requests.get(url)
    filename = f"target/image_{index}.jpg"
    open(filename, "wb").write(response.content)
    print(f"Process {index} finished downloading {filename}")

# below if condition line is important for using multiprocessing, or else it will go to infinite processing 
if __name__ == "__main__": 
    start_time = time.time()
    
    processes = []
    url = 'https://picsum.photos/2000/3000'
    for i in range(10):
        p = Process(target=download_image, args=(url, i))
        processes.append(p)
        p.start()  # Start process

    for p in processes:
        p.join()  # Wait for all processes to finish

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
