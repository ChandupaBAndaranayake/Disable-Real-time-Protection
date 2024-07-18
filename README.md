# Disabling Real-time Protection on Windows using Python
Strictly for gamers

This guide provides instructions on how to use a Python script to disable real-time protection on a Windows machine.

## Prerequisites

- Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
- Ensure PowerShell is available on your system and accessible from the command line.
- You need administrative privileges to disable real-time protection.

## Step 1: Save the Script

1. Open a text editor like Notepad.
2. Copy and paste the following script into the text editor:

    ```python
    import ctypes
    import subprocess
    import os
    import sys

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def disable_realtime_protection():
        # Command to disable real-time protection using PowerShell
        powershell_cmd = 'Set-MpPreference -DisableRealtimeMonitoring $true'

        try:
            # Run PowerShell command silently
            subprocess.run(['powershell', '-Command', powershell_cmd], check=True, shell=True)
            print("Real-time protection disabled successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to disable real-time protection. {e}")
            sys.exit(1)

    def main():
        if is_admin():
            # Disable real-time protection
            disable_realtime_protection()
        else:
            # Re-run the script with admin rights
            print("Script requires admin rights. Re-running with elevated privileges...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    if __name__ == "__main__":
        main()
    ```

3. Save the file with a `.py` extension, for example, `disable_realtime_protection.py`.

## Step 2: Run the Script with Python

1. **Open Command Prompt as Administrator**:
    - Click on the Start menu, type `cmd`, right-click on `Command Prompt`, and select `Run as administrator`.

2. **Navigate to the Script Location**:
    - Use the `cd` command to change the directory to where you saved the script. For example:

    ```sh
    cd C:\path\to\your\script
    ```

3. **Run the Script**:
    - Execute the script using Python:

    ```sh
    python disable_realtime_protection.py
    ```

### Example

If your script is saved in `C:\Scripts\disable_realtime_protection.py`, the commands would be:

```sh
cd C:\Scripts
python disable_realtime_protection.py
