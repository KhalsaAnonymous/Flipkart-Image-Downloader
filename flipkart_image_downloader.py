from io import BytesIO
import os
from PIL import Image
import requests

# Create directory to store downloaded images
if not os.path.exists("flipkart_IMG"):
    os.makedirs("flipkart_IMG")

# Read URLs from text file
with open("flipkartURL.txt", "r") as f:
    urls = f.readlines()

# Print the number of URLs found in the file
print(f"Found {len(urls)} URLs in the file.")

# Process each URL and download the corresponding image
for i, url in enumerate(urls):
    url = url.strip()
    new_url = url.replace("/416/416/", "/").replace("/832/832/", "/")
    new_file_path = f"flipkart_IMG/image_{i+1}.jpg"
    print(f"Processing image from URL {i+1}...")
    response = requests.get(new_url)
    img = Image.open(BytesIO(response.content))
    img = img.convert("RGB")
    img.save(new_file_path)
    print(f"Image converted to JPEG and saved at {new_file_path}")
