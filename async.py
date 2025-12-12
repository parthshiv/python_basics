"""
Async is called as Non-Blockin-I/O-bound. A single thread runs many tasks
Example: One person is downloading all images. While waiting for network for image 1, switches to image 2, then 3, etc. One worker handles everything efficiently. One worker, switches between tasks while waiting.
Pros: Memory efficient. Handles thousands of task all together easily.
"""
import asyncio # this is in-built library to use async operations
import time
import requests

# normal process of function calling
def send_email(user):
    print(f"Sending to {user}...")
    time.sleep(3)
    print(f"Done {user}")

def main():
    send_email("User A") # this will run
    send_email("User B") # this will run once User A finishes
    send_email("User C") # this will run once User B finishes

# main()

# use Async for calling function
async def send_email(user):
    print(f"Sending to {user}...")
    await asyncio.sleep(3) # await means: “Wait here until this task finishes.”  asyncio.sleep will not block the task, whereas time.sleep will block the task. this is Simulate delay i.e takes time to send email  
    print(f"Done {user}")

async def main():
    await asyncio.gather(
        send_email("User A"), # this will run at same time all together, no waiting
        send_email("User B"), # this will run at same time all together, no waiting
        send_email("User C"), # this will run at same time all together, no waiting
    )

asyncio.run(main())

# use Async to download multiple images faster
url = 'https://picsum.photos/2000/3000'

def download_image_blocking(index):
    print(f"Downloading image {index}...")
    r = requests.get(url)
    with open(f"target/image_{index}.jpg", "wb") as f:
        f.write(r.content)
    print(f"Finished image {index}")

async def download_image_async(index):
    # Run blocking function in a separate thread without blocking event loop
    await asyncio.to_thread(download_image_blocking, index)

async def main_download():
    tasks = [download_image_async(i) for i in range(10)]
    await asyncio.gather(*tasks)
 
start_time = time.time()

asyncio.run(main_download())

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")

