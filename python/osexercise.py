import os
import time

def list_old_files(directory, days):
    current_time = time.time()
    age_threshold = current_time - (days * 86400)  # 86400 seconds in a day

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_mod_time = os.path.getmtime(file_path)
            if file_mod_time < age_threshold:
                print(file_path)

def main():
    directory = input("Enter the directory path: ")
    days = int(input("Enter the age threshold in days: "))
    list_old_files(directory, days)

if __name__ == "__main__":
    main()
