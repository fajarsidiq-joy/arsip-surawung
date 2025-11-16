import os
import json

base_dir = r"D:\Dokumen\PROJECT MANDIRI\arsip-surawung\kenangan"
output_dir = "data"

os.makedirs(output_dir, exist_ok=True)

for location in os.listdir(base_dir):
    location_path = os.path.join(base_dir, location)
    if not os.path.isdir(location_path):
        continue

    photos = []
    videos = []

    for file in os.listdir(location_path):
        ext = file.lower().split('.')[-1]
        path = f"{base_dir}/{location}/{file}"

        if ext in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
            photos.append({"src": path, "alt": file})
        elif ext in ['mp4', 'mov', 'mkv', 'avi']:
            videos.append({"src": path})

    data = {
        "name": location.capitalize(),
        "description": f"Kenangan seru di {location.capitalize()}",
        "photos": photos,
        "videos": videos
    }

    with open(f"{output_dir}/{location.lower()}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Semua file JSON berhasil dibuat di folder /data")
