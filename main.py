"""
Author: Soad17339-blip
Description: Automatic File Organizer script to sort files in Downloads folder by extension.
"""

import os
import shutil

# Directory to clean up (default is Downloads folder)
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")

# File categories and their extension mapping
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".html", ".css", ".js", ".json", ".cpp"],
    "Executables": [".exe", ".msi", ".dmx"]
}

def organize_downloads():
    if not os.path.exists(DOWNLOADS_DIR):
        print(f"Directory {DOWNLOADS_DIR} does not exist.")
        return

    print("Starting organization...")
    
    for filename in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in CATEGORIES.items():
            if file_ext in extensions:
                category_dir = os.path.join(DOWNLOADS_DIR, category)
                os.makedirs(category_dir, exist_ok=True)
                
                shutil.move(file_path, os.path.join(category_dir, filename))
                print(f"Moved: {filename} -> {category}/")
                moved = True
                break

        if not moved and file_ext:
            other_dir = os.path.join(DOWNLOADS_DIR, "Others")
            os.makedirs(other_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(other_dir, filename))
            print(f"Moved: {filename} -> Others/")

    print("Organization completed!")

if __name__ == "__main__":
    organize_downloads()
