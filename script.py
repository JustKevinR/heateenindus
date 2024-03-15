import random
import sys
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

def ask_for_num_runs():
    while True:
        num_runs_input = input("How many times do you want to run the script? Enter a number or 'endless' for an endless script: ").strip().lower()
        if num_runs_input == "endless":
            return "endless"
        try:
            num_runs = int(num_runs_input)
            if num_runs <= 0:
                raise ValueError
            return num_runs
        except ValueError:
            print("Please enter a valid positive integer or 'endless'.")

def ask_for_cooldown_type():
    while True:
        cooldown_type = input("Choose the cooldown type ('fixed' or 'realistic'): ").lower()
        if cooldown_type in ('fixed', 'realistic'):
            return cooldown_type
        print("Invalid choice. Please choose 'fixed' or 'realistic'.")

def ask_for_cooldown_duration():
    while True:
        try:
            cooldown_minutes = input("Enter the cooldown duration in minutes: ")
            if cooldown_minutes.lower() == "none":
                return None
            cooldown_minutes = int(cooldown_minutes)
            if cooldown_minutes < 0:
                raise ValueError
            return cooldown_minutes
        except ValueError:
            print("Please enter a valid non-negative integer for the cooldown duration, or 'none' to skip cooldown.")

# Read comments from the text file with UTF-8 encoding
with open("comments.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# If file is empty, exit the script
if not lines:
    print("The comments file is empty. Exiting the script.")
    sys.exit()

# Ask user for the URL
url = input("Please enter the URL to visit: ")

# Ask user for the number of times to run the script
num_runs = ask_for_num_runs()

# Choose the cooldown type and duration if applicable
cooldown_type = ask_for_cooldown_type()
if cooldown_type == 'fixed':
    cooldown_minutes = ask_for_cooldown_duration()

# Loop for the specified number of runs or endlessly
run_count = 0
while num_runs == "endless" or run_count < num_runs:
    # Launch Microsoft Edge browser
    driver = webdriver.Edge()

    # Open the desired website
    driver.get(url)

    # Initialize last_comment variable
    last_comment = None

    # Loop until the generated comment is different from the last one
    while True:
        # Generate a random line number
        random_line_number = random.randint(0, len(lines) - 1)

        # Select a random line from the file
        comments = lines[random_line_number].strip()

        # Check if the comment is different from the last one
        if comments != last_comment:
            last_comment = comments
            break

    # Print the comment and loop number
    print(f"Loop {run_count + 1}/{num_runs if num_runs != 'endless' else 'Endless'}: Comment - {comments}")

    # Find the input field and send keys
    input_field = driver.find_element(By.ID, "kiidan_est___acclaim_text")
    input_field.send_keys(comments)

    # Find the comment element and print confirmation
    comment = driver.find_element(By.ID, 'kiidan_est___acclaim_text')

    # Prompt the user to press Enter before closing the browser
    input("Press Enter to close the browser...")

    # Close the browser
    driver.quit()

    # If not running endlessly or it's the last run, break out of the loop
    if num_runs != "endless" and run_count >= num_runs - 1:
        break

    # Cooldown period
    if cooldown_type == 'fixed':
        print(f"Cooldown for {cooldown_minutes} minute(s)...")
        time.sleep(cooldown_minutes * 60)  # Convert minutes to seconds
    elif cooldown_type == 'realistic':
        cooldown_time = random.uniform(15, 240)  # Random time between 15 minutes to 4 hours
        print(f"Cooldown for {cooldown_time:.2f} minute(s)...")
        time.sleep(cooldown_time * 60)  # Convert minutes to seconds

    run_count += 1




#cooldown
    #ask user to type in how long is the cooldown in minutes
    # releastic cooldown beatween 15minutes -4 hours using a randomnumber gen

#endless
    #option that scrip would run until you stop it

# maybe step by step user guid
#disclaimer i made it for fun and dont recoment using it


#fix endless with real
