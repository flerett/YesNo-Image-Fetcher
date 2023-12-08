import requests
from PIL import Image
from io import BytesIO
import pyperclip
import os


YESNO_API_URL = 'https://yesno.wtf/api'
COMMANDS = {
     'r': 'random',
     'y': 'yes',
     'n': 'no',
     'm': 'maybe',
}


def copy_image_to_clipboard(image_path):
     try:
         with open(image_path, 'rb') as image_file:
             image_data = image_file.read()
             pyperclip.copy(image_data)
             print(f'Image at {image_path} copied to clipboard.')
     except FileNotFoundError:
         print(f'Error: Image file not found at {image_path}.')


def get_yesno_image(command):
     if command == 'random':
         url = YESNO_API_URL
     elif command in ['yes', 'no', 'maybe']:
         url = f'{YESNO_API_URL}?force={command}'
     else:
         print('Invalid command. Please use "r", "y", "n", or "m".')
         return

     response = requests.get(url)
     data = response.json()
     image_url = data['image']

     # Get the image
     image_response = requests.get(image_url)
     image = Image.open(BytesIO(image_response.content))

     # Generate a file name
     image_name = f'{command}.png'
     counter = 1

     # Check for the existence of a file with the same name and change the name if it already exists
     while os.path.exists(image_name):
         image_name = f'{command}_{counter}.png'
         counter += 1

     # Save the image
     image.save(image_name)

     print(f'Image saved to {image_name} and copied to clipboard.')

if __name__ == "__main__":
     # Request a command from the user
     user_command = input('Enter command (r (random)/y (yes)/n (no)/m (maybe)): ').lower()
     user_command = COMMANDS[user_command]
     # Call the function with the entered command
     get_yesno_image(user_command)
