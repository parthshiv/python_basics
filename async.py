"""
Async is called as Non-Blocking I/O. A single thread runs many tasks
Example: One person is downloading all images. While waiting for network for image 1, switches to image 2, then 3, etc. One worker handles everything efficiently. One worker, switches between tasks while waiting.
Pros: Memory efficient. Handles thousands of task all together easily.
"""
import asyncio # this is in-built library to use async operations
import time

def send_email(user):
    print(f"Sending to {user}...")
    time.sleep(3)
    print(f"Done {user}")

def main():
    send_email("User A") # this will run
    send_email("User B") # this will run once User A finishes
    send_email("User C") # this will run once User B finishes

# main()


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

