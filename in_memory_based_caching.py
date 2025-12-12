from datetime import datetime, timedelta
import time

# Simulated database table. Assume below records are coming from database table dynamically
database = [
    {"id": 1, "name": "Alice", "updated_at": datetime.now()},
    {"id": 2, "name": "Bob", "updated_at": datetime.now()},
    {"id": 3, "name": "Charlie", "updated_at": datetime.now()},
    {"id": 4, "name": "David", "updated_at": datetime.now()},
    {"id": 5, "name": "Eve", "updated_at": datetime.now()},
]

# Cache structure
cache = {
    "html_content": None,
    "last_updated": None  # timestamp of latest record
}

def render_dashboard(records):
    # Simple HTML rendering
    html = "<h1>Dashboard</h1>\n<ul>\n"
    for r in records:
        html += f"<li>{r['id']}: {r['name']}</li>\n"
    html += "</ul>\n"
    return html

def get_dashboard():
    # Get latest update timestamp from "DB"
    table_last_updated = max(r["updated_at"] for r in database) if database else None

    # Check cache
    if cache["html_content"] and cache["last_updated"] == table_last_updated:
        print("Serving dashboard from cache")
        return cache["html_content"]

    # Otherwise, regenerate HTML
    print("Generating new dashboard HTML")
    html_content = render_dashboard(database)

    # Update cache
    cache["html_content"] = html_content
    cache["last_updated"] = table_last_updated

    return html_content

if __name__ == "__main__":
    # First request → generates HTML
    print(get_dashboard())

    time.sleep(2)

    # Second request → should serve from cache
    print(get_dashboard())

    time.sleep(2)

    # Simulate new records added to DB after 1 hour
    new_time = datetime.now() + timedelta(hours=1)
    database.append({"id": 6, "name": "Frank", "updated_at": new_time})
    database.append({"id": 7, "name": "Grace", "updated_at": new_time})

    # Next request → regenerates cache with new data
    print(get_dashboard())
