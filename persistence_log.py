import os

if os.path.exists("database.txt") and os.path.getsize("database.txt") > 0:
    
    print("[WARNING]: 'database.txt' already exists.")
    print("New data will be appended. Avoid accidental overwrites.")
    print("!"*14 + "\n")

def daily_block(daily_blocker):
    with open("database.txt", "a", encoding="utf_8") as archive:
        archive.write(f"{daily_blocker}\n")
    print(" Blocker saved successfully.")

def fetch_blockers():
    
    if os.path.exists("database.txt"):
        with open("database.txt", "r", encoding="utf_8") as archivo:
            
            lines = archivo.readlines()
            
            if not lines:
                print("\n[INFO]: The log is empty.")
            else:
                print("\n--- CURRENT BLOCKERS ---")
                for id, line in enumerate(lines):
                    print(f"{id + 1}. {line.strip()}")
    else:
        # El 'else' obligatorio del requerimiento
        print("\n[ERROR]: The file 'database.txt' does not exist yet.")


while True:
    print("""
    ******** WELCOME TO THE BLOCKER PROGRAM ********
    1. Add blocker
    2. fetch blockers
    3. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        daily_blocker = input("Please, enter your daily blocker: ").lower()
        daily_block(daily_blocker)
    elif choice == "2":
        fetch_blockers()
    elif choice == "3":
        print("============ PROGRAM COMPLETED ============")
        break
    else:
        print("Invalid choice. Please try again.")

#"I will report the file lock via Slack to coordinate an immediate solution with the team."
#"I will report the error in Jira to document the technical failure and ensure its formal follow-up."
#"I will send an email to the supervisor with a summary of the problem to formalize the current status of the project."



# The script ensures data persistence by storing the team's locks in a local text file, guaranteeing that information is 
# not lost when the program closes. Upon startup, the system validates the file's existence to issue a warning and 
# prevent accidental overwriting of previous records. Through the fetch function, the user can retrieve and view the 
# team's current status in an organized manner; however, if a critical error occurs in the data flow, the protocol instructs 
# the team to reach out via Slack to resolve the lock immediately.
