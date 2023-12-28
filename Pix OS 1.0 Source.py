print('Welcome to Pix OS ')

import password 
# Minimum length
min_length = 10
required_classes = {
}

notif = input("Enter Password")

if not password.check(login_key, min_length, required_classes):
    print("Login key does not meet complexity requirements.")
    print("Please ensure your password has:")
    print(f"- At least {min_length} characters")
    print("- One uppercase letter")
    print("- One lowercase letter")
    print("- One number")
    print("- One symbol")
    quit()

import bcrypt

salt = bcrypt.gensalt()

password = "[PLACEHOLDER_PASSWORD]".encode('utf-8')
hashed_password = bcrypt.hashpw(password, salt)

if bcrypt.checkpw(password, hashed_password):
    print("Password matched")
else:
    print("Password did not match.")

if input == "[PLACEHOLDER_PASSWORD]":
    print('Access Granted')
else:
    print(f"Access Denied")

import datetime
now = datetime.datetime.now()

formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Example format: 2023-12-27 11:42:00

print("Current time:", formatted_time)

if input == "time":
    print("Current time:", formatted_time)
else: quit()

import psutil

battery = psutil.sensors_battery()
percent = battery.percent
print("Battery charge:", percent, "%")

if input == "battery status":
    print("Battery charge:", percent, "%")
else: quit()

import psutil

# Get the CPU usage percentage
cpu_percent = psutil.cpu_percent(interval=1)  # Sample over a 1-second interval

# Print the CPU usage
print("CPU usage:", cpu_percent, "%")

import requests

def download_file(url, filename):
    """Downloads a file from a given URL and saves it with the specified filename."""

    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Raise an exception for error status codes

        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # Filter out keep-alive new chunks
                    downloaded_size += len(chunk)
                    f.write(chunk)

                    # Progress bar
                    done = int(50 * downloaded_size / total_size)
                    print(f'\r[{"#" * done}{"." * (50 - done)}] {downloaded_size}/{total_size} bytes', end='')

    print('\nDownload complete!')

# Example usage:
url = 'https://example.com/file.zip'
filename = 'downloaded_file.zip'
download_file(url, filename)






