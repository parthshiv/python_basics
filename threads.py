"""
Thread are called as Blocking-I/O-bound but runs concurrently.
example: You hire 5 people, each downloads one image at the same time. Each person still “waits” for 3 seconds, but all run concurrently. Multiple workers, each waiting for their task
Pros: good for Small number of tasks
Cons: Memory-heavy; Extra Memory uses
"""

import threading
import time

# Simulate sending email
def send_email(user):
    print(f"Sending email to {user}...")
    time.sleep(3)  # Simulate delay (like sending real email)
    print(f"Email sent to {user}")

# List of users
users = ["Alice", "Bob", "Charlie", "David"]

# Create threads for each user
threads = []

for user in users:
    t = threading.Thread(target=send_email, args=[user])
    threads.append(t)
    t.start()  # Start the thread. it runs in the background

# Wait for all threads to finish
for t in threads:
    t.join() # Wait for particular thread to finish

print("All emails sent!")
