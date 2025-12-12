"""
This program called for file-based caching because we'll compare the last modification time of the file.

File-based cache:
-----------------
Storage: Python dictionary in memory (or could also write to file if you want).
Data source: Static template file (homepage.html).
Cache invalidation trigger: File modification time (mtime).
Scope: Only valid within the current Python process.
Use case: Avoid re-reading / re-rendering static files.
"""

import os
import time

# In-memory cache dictionary
cache = {
    "html_content": None,
    "file_mtime": None
}

TEMPLATE_PATH = "target/homepage.html"

def get_homepage():
    # Check file modification time
    file_mtime = os.path.getmtime(TEMPLATE_PATH)
    print(cache)
    print(file_mtime)
    # If cache exists and template hasn't changed → return cached HTML
    if cache["html_content"] and cache["file_mtime"] == file_mtime:
        print("Serving from cache")
        return cache["html_content"]

    # Otherwise, read template from file
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Update cache
    cache["html_content"] = html_content
    cache["file_mtime"] = file_mtime
    print("Template changed or cache empty → caching new content")

    return html_content

# -------------------------------
# Example usage: simulate server requests
# -------------------------------
if __name__ == "__main__":    
        for i in range(3):
            #if you see output will be 3 time, 1st time will take time as it will generate a new output but then 2 times it wil be fast as it will show you cached output from cache     
            content = get_homepage()
            time.sleep(2)
