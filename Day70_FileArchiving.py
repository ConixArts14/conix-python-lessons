elif choice == "19":
    import os, shutil, datetime
    ...
elif choice == "19":
    import os, shutil, datetime

    # Create archive folder if it doesn’t exist
    if not os.path.exists("archive"):
        os.makedirs("archive")

    # Timestamp for unique backup names
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    files_to_archive = ["student_report.json", "student_report.csv"]

    for file in files_to_archive:
        if os.path.exists(file):
            new_name = f"archive/{file.replace('.', f'_{timestamp}.')}"
            shutil.copy(file, new_name)
            print(f"✅ {file} archived as {new_name}")
        else:
            print(f"🚫 {file} not found, skipping.")

20. Restore from Archive
elif choice == "20":
    import os, shutil

    archive_folder = "archive"

    if not os.path.exists(archive_folder):
        print("🚫 No archive folder found.")
    else:
        files = os.listdir(archive_folder)
        if not files:
            print("🚫 No backup files available.")
        else:
            print("📂 Available backups:")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")

            selection = input("Enter the number of the file to restore: ")

            try:
                index = int(selection) - 1
                chosen_file = files[index]

                if "json" in chosen_file:
                    shutil.copy(os.path.join(archive_folder, chosen_file), "student_report.json")
                    print(f"✅ Restored {chosen_file} as student_report.json")
                elif "csv" in chosen_file:
                    shutil.copy(os.path.join(archive_folder, chosen_file), "student_report.csv")
                    print(f"✅ Restored {chosen_file} as student_report.csv")
                else:
                    print("🚫 Invalid file type.")
            except (ValueError, IndexError):
                print("🚫 Invalid selection.")

21. Auto-Rotate Archives
elif choice == "21":
    import os

    archive_folder = "archive"

    if not os.path.exists(archive_folder):
        print("🚫 No archive folder found.")
    else:
        files = os.listdir(archive_folder)

        if len(files) <= 5:
            print("✅ Archive is within limit. No rotation needed.")
        else:
            # Sort files by last modified time
            files.sort(key=lambda f: os.path.getmtime(os.path.join(archive_folder, f)))

            # Keep latest 5, delete the rest
            to_delete = files[:-5]

            for file in to_delete:
                os.remove(os.path.join(archive_folder, file))
                print(f"🗑️ Deleted old backup: {file}")

            print("✅ Archive rotated. Only latest 5 backups kept.")

22. Scheduled Auto-Archive
elif choice == "22":
    import os, shutil, datetime

    archive_folder = "archive"

    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    files_to_archive = ["student_report.json", "student_report.csv"]

    for file in files_to_archive:
        if os.path.exists(file):
            new_name = f"{archive_folder}/{file.replace('.', f'_{timestamp}.')}"
            shutil.copy(file, new_name)
            print(f"💾 Auto-archived {file} as {new_name}")
        else:
            print(f"🚫 {file} not found, skipping.")

    # Auto-rotate: keep only latest 5 backups
    files = os.listdir(archive_folder)
    if len(files) > 5:
        files.sort(key=lambda f: os.path.getmtime(os.path.join(archive_folder, f)))
        to_delete = files[:-5]
        for old in to_delete:
            os.remove(os.path.join(archive_folder, old))
            print(f"🗑️ Deleted old backup: {old}")

    print("✅ Scheduled auto-archive complete. Latest backups preserved.")

23. Archive Compression
elif choice == "23":
    import os, zipfile, datetime

    archive_folder = "archive"

    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = f"{archive_folder}/student_report_{timestamp}.zip"

    files_to_compress = ["student_report.json", "student_report.csv"]

    with zipfile.ZipFile(zip_name, "w") as zipf:
        for file in files_to_compress:
            if os.path.exists(file):
                zipf.write(file, arcname=file)
                print(f"📦 Added {file} to {zip_name}")
            else:
                print(f"⚠️ {file} not found, skipping.")

    print(f"✅ Archive compressed as {zip_name}")
