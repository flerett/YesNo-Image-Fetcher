# YesNo Image Fetcher

This Python script fetches YesNo images using the YesNo API and allows you to copy the image to the clipboard.

## Usage

1. Install the required dependencies:

  ```bash
  pip install -r requirements.txt
  ```
   
2. Run the script:

  ```bash
  python script_name.py
  ```
3. Enter one of the following commands when prompted:

- r (random)
- y (yes)
- n (no)
- m (maybe)

The script will save the fetched image and copy it to the clipboard.

## Requirements
requests: Used to make HTTP requests to the YesNo API.  
Pillow: A powerful image processing library.  
pyperclip: Provides a cross-platform Python module for clipboard access.  

**requirements.txt:**

```
requests==2.26.0
Pillow==8.4.0
pyperclip==1.8.2
```
