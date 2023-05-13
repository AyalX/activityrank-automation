import time
import pyautogui
import keyboard

def read_file(file_name):
    """Reads a file and returns its lines."""
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return []

def write_to_file(file_name, data):
    """Writes data to a file."""
    try:
        with open(file_name, 'w') as file:
            file.writelines(data)
    except Exception as e:
        print(f"Failed to write to the file {file_name}. Error: {str(e)}")

def generate_commands(input_file, output_file):
    """Generates slash commands from the given input file and writes them to the output file."""
    # Read input file
    lines = read_file(input_file)

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
    write_to_file(output_file, commands)

    print("Slash commands generated successfully!")

def execute_commands(file_name):
    """Reads commands from the given file and executes them."""
    # Open the file with commands
    commands = read_file(file_name)

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

def start_automation(input_file, output_file):
    """Starts the automation process."""
    print("Press 'Home' to start the automation. Press 'Esc' to stop the automation.")
    keyboard.wait('home')
    print("Automation started!")

    generate_commands(input_file, output_file)
    execute_commands(output_file)

    print("Automation completed successfully!")

# Configuration
input_file = 'give-rewards.txt'
output_file = 'commands.txt'

start_automation(input_file, output_file)
