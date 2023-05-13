# Give Rewards Automation Script

This python script is designed to automate the process of giving rewards in a system using slash commands. The script generates slash commands from a given input file and then uses pyautogui and keyboard libraries to automate typing these commands.

## Installation

### Dependencies

The script requires the following python libraries:

1. `pyautogui` - For automating the mouse and keyboard actions.
2. `keyboard` - To detect keyboard inputs.

You can install these libraries using pip:

```
pip install pyautogui keyboard
```

## Usage

1. Prepare an input file named `give-rewards.txt` in the following format:

    ```
    user_id1 - xp1 XP
    user_id2 - xp2 XP
    ...
    ```

    For example:

    ```
    user123 - 500 XP
    user456 - 300 XP
    ```

    Each line should contain a user_id, followed by ' - ', followed by the amount of XP, and ending with ' XP'.

2. Run the script:

    ```
    python bonus-automation.py
    ```

3. Press 'Home' to start the automation. If you want to stop the automation at any point, press 'Esc'.

## Features

- The script will read the `give-rewards.txt` file, process each line and generate corresponding slash commands in the format `/bonus member member: {user_id} change: {xp}`. These commands are then saved to `commands.txt`.

- The script will then read the `commands.txt` file and starts executing each command one by one. It will type the command, then press 'Enter' to select the slash command and press 'Enter' again to send the command.

- The script provides controls to start and stop the automation. You can start the automation by pressing the 'Home' button and stop it at any point by pressing the 'Esc' button.

## Disclaimer

Please be aware that automating input actions can sometimes result in unintended consequences. Always make sure that you have the correct window active and are prepared to stop the script if something goes wrong.

This script is provided for educational purposes only. Please use it responsibly. Any misuse of this script and its consequences are solely the user's responsibility. The author does not take any responsibility for any misuse of this script.

## License

This project is released under the [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) License](LICENSE.md).

## Author
- [@AyalX](https://github.com/AyalX) on GitHub.

## Contributions
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/AyalX/discord-server-info/issues) if you want to contribute.

## Show your support
Give a ⭐️ if this project helped you!
