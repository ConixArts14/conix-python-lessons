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
