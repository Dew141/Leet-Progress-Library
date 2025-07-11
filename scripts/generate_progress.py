
import os, json

def read_top_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    top_10 = lines[:10]
    top_10_stripped = [line.strip() for line in top_10]
    return top_10_stripped

def parse_metadata(filepath):
    read_lines = read_top_lines(filepath)
    metadata = {
        "id": "",
        "title" : "", 
        "difficulty": "",
        "link": "", 
        "tags": [], 
        "filename": ""}

    for line in read_lines:
        if line.startswith("# Title:"):
            metadata["title"] = line.split(":", 1)[1].strip()
        elif line.startswith("# Problem ID:"):
            metadata["id"] = int(line.split(":", 1)[1].strip())
        elif line.startswith("# Difficulty:"):
            metadata["difficulty"] = line.split(":", 1)[1].strip()
        elif line.startswith("# URL:") or line.startswith("# Link:"):
            metadata["link"] = line.split(":", 1)[1].strip()
        elif line.startswith("# Tags:"):
            tags_string = line.split(":", 1)[1].strip()
            if tags_string:
                metadata["tags"] = [tag.strip() for tag in tags_string.split(",")]

    metadata["filename"] = filepath
    return metadata

def scan_problems(folders=['easy', 'medium', 'hard']):
    all_metadata = []

    for folder in folders:
        # checks if the folder is in the directory
        if not os.path.isdir(folder):
            print(f"Folder '{folder}' does not exist, skipping.")
            continue
        
        # list files in folder
        for filename in os.listdir(folder):

            if filename.endswith('.py') :
                filepath = os.path.join(folder, filename)
                print(f"Processing {filepath}...")

                metadata = parse_metadata(filepath)
                all_metadata.append(metadata)

    return all_metadata

def save_progress_json(metadata_list, filename='progress.json'): 
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(metadata_list, f, indent=4)

if __name__ == "__main__":
    print("Starting scan...")
    all_metadata = scan_problems()
    print(f"Collected metadata for {len(all_metadata)} problems.")
    
    save_progress_json(all_metadata)
    print("progress.json created!")
