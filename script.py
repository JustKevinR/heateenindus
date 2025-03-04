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

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"Cooldown: {remaining} seconds remaining...", end="\r", flush=True)
        time.sleep(1)
    print("Cooldown complete!             ")

# Read comments from the text file
with open("comments.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

if not lines:
    print("The comments file is empty. Exiting the script.")
    sys.exit()

url = input("Please enter the URL to visit: ")
num_runs = ask_for_num_runs()
cooldown_type = ask_for_cooldown_type()
cooldown_minutes = ask_for_cooldown_duration() if cooldown_type == 'fixed' else None

run_count = 0

while num_runs == "endless" or run_count < num_runs:
    try:
        driver = webdriver.Edge()
        driver.get(url)

        last_comment = None

        while True:
            comment = random.choice(lines).strip()
            if comment != last_comment:
                last_comment = comment
                break

        print(f"Loop {run_count + 1}/{num_runs if num_runs != 'endless' else 'Endless'}: Comment - {comment}")

        input_field = driver.find_element(By.ID, "kiidan_est___acclaim_text")
        input_field.send_keys(comment)

        submit_button = driver.find_element(By.NAME, "Submit")
        submit_button.click()
    
    finally:
        driver.quit()

    if num_runs != "endless" and run_count >= num_runs - 1:
        break

    # Cooldown logic with countdown timer
    if cooldown_type == 'fixed' and cooldown_minutes:
        print(f"Cooldown for {cooldown_minutes} minute(s)...")
        countdown_timer(cooldown_minutes * 60)
    elif cooldown_type == 'realistic':
        cooldown_time = random.uniform(15, 240)
        print(f"Cooldown for {cooldown_time:.2f} minute(s)...")
        countdown_timer(int(cooldown_time * 60))

    run_count += 1
