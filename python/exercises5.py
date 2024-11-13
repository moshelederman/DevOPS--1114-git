#1
import datetime
with open("journal_entries.txt", "w") as file:
    while True:
        entry = input("please write a few lines of text (or type 'done' to finish):")
        if entry.lower() == 'done':
            break
        current_time = datetime.datetime.now().strftime("%x %X")
        file.write(f"{current_time} {entry} \n")

#2
print("\ncurrent journal entries:")
with open("journal_entries.txt", "r") as file:
     for line in file:
        print(line.strip())

#3
with open("journal_entries.txt", "a") as file:
    while True:
        new_entry = input("please write another few lines of text(or type 'done' to finish):")
        if new_entry.lower() == 'done':
            break
        file.write(f"{current_time} {new_entry} \n")

#4
print("\nupdate journal entries:")
with open("journal_entries.txt", "r") as file:
    lines = file.readlines()
    entry_count = 0
    word_count = 0
    for line in lines:
        entry_count += 1
        words = line.split()
        word_count += len(words[2:])
print(f"Total number of entries: {entry_count}")
print(f"Total number of words: {word_count}")     