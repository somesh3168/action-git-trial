import os
import platform
import socket
import subprocess

def main():
    # Get OS information
    os_info = f"Operating System: {platform.system()} {platform.release()}"

    # Get hostname
    hostname = f"Hostname: {socket.gethostname()}"

    # Run shell command 'whoami'
    whoami_result = subprocess.run(['whoami'], capture_output=True, text=True)
    username = f"Current User: {whoami_result.stdout.strip()}"

    # Get machine information
    machine_info = f"Machine Information: {platform.machine()}"

    # Print information
    print(os_info)
    print(hostname)
    print(username)
    print(machine_info)

if __name__ == "__main__":
    main()
