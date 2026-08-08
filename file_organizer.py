import os
import shutil

DIRECTORIES = {
    "Spreadsheets": [".csv", ".xlsx", ".xls"],
    "Documents": [".pdf", ".txt", ".docx", ".doc"],
    "Code": [".py", ".html", ".css", ".js", ".cpp"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"]
}

def organize_files(target_directory):
    if not os.path.exists(target_directory):
        print(f"Error: The directory {target_directory} does not exist.")
        return

    moved_count = 0
    # List all items in the target directory
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        # CRITICAL FIX: If it's a folder (like 'Documents' or 'Code'), skip it entirely so we never touch already sorted files!
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()

        moved = False
        for category, extensions in DIRECTORIES.items():
            if file_extension in extensions:
                category_folder = os.path.join(target_directory, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                destination_path = os.path.join(category_folder, filename)
                
                # Check if file already exists in destination to prevent overwriting/deleting
                if os.path.exists(destination_path):
                    print(f"Skipped (Already exists): {filename}")
                    moved = True
                    break

                shutil.move(file_path, destination_path)
                print(f"Moved: {filename} -> {category}/")
                moved_count += 1
                moved = True
                break
        
        if not moved:
            print(f"Skipped (Unknown type): {filename}")

    print(f"\nOptimization complete! Successfully organized {moved_count} new files.")

if __name__ == "__main__":
    path_to_organize = input("Enter the full path of the folder you want to organize: ")
    organize_files(path_to_organize)