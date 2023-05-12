import time
import pyautogui
import keyboard

def generate_commands():
    # Read input file
    with open('give-rewards.txt', 'r') as file:
        lines = file.readlines()

    # Process each line and create slash commands
    commands = []
    for line in lines:
        parts = line.strip().split(' - ')
        if len(parts) == 2:
            user_id = parts[0]
            xp = parts[1].split(' XP')[0]
            command = f'/bonus member member: {user_id} change: {xp}\n'
            commands.append(command)

    # Write slash commands to output file
    with open('commands.txt', 'w') as file:
        file.writelines(commands)

    print("Slash commands generated successfully!")

def execute_commands():
    # Open the file with commands
    with open('commands.txt', 'r') as file:
        commands = file.readlines()

    # Iterate over each command
    for command in commands:
        # Check if the automation should be stopped
        if keyboard.is_pressed('esc'):
            print("Automation stopped.")
            return

        # Copy the command
        pyautogui.write(command.strip())
        time.sleep(0.5)

        # Press Enter to select the slash command
        pyautogui.press('enter')
        time.sleep(0.6)

        # Press Enter again to send the slash command
        pyautogui.press('enter')
        time.sleep(1)

def start_automation():
    print("Press 'Home' to start the automation. Press 'Esc' to stop the automation.")
    keyboard.wait('home')
    print("Automation started!")

    execute_commands()

    print("Automation completed successfully!")

generate_commands()
start_automation()
