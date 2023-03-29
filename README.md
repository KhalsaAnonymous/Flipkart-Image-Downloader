# Flipkart Image Downloader

This is a simple Python script to download images from Flipkart URLs. It reads the URLs from a text file, converts the images to JPEG format, and saves them to a directory named `flipkart_IMG`.
## Features
- Automatically replaces the URLs' image sizes with the original size to download images in HD quality.

## How to Use

1. Create a text file named `flipkartURL.txt` and add the URLs of the Flipkart images you want to download, each on a new line.
2. Run the script by executing the following command: `python flipkart_image_downloader.py`
3. The downloaded images will be saved in the `flipkart_IMG` directory.

## Requirements

This script requires the following Python libraries:
- `Pillow`
- `requests`

You can install these libraries using the following command.
    
    pip install Pillow
    pip install requests

## Author

This script is developed and maintained by [KhalsaAnonymous](https://github.com/KhalsaAnonymous/).
