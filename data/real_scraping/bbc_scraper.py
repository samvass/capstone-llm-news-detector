import json
import csv
import os
import requests
from bs4 import BeautifulSoup

# https://data.world/opensnippets/bbc-uk-news-dataset

# Create a folder for storing images if it doesn't exist
image_folder = "./data/real_scraping/bbc_images"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Read JSON data from file
with open('./data/real_scraping/bbc_news_list_uk.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Extract 'title', 'content', and 'url' fields from each JSON object
rows = []
article_num = 1

for entry in data:
    if (article_num >= 250):
        break

    article_num += 1

    if 'content' in entry and entry['content']:
        rewritten_title = entry['title'].replace("\\'", "'").replace('""', '').replace('"', '').replace('\n', '').replace('\\', '').replace('\n', '').replace('/', '').replace('?', '').replace('*', '')

        url = entry['url']
        response = requests.get(url)
        # Parse HTML content to find the image URL
        soup = BeautifulSoup(response.text, 'html.parser')
        print(entry['url'])
        image = soup.find("main").find("img", class_="ssrcss-evoj7m-Image")

        if image:
            print("found image...")
            img_url = image.get('src')
            # Download the image
            if img_url.endswith('.jpg'):
                response = requests.get(img_url)
                if response.status_code == 200:
                    # Save the image to the folder
                    image_path = os.path.join(image_folder, f"{rewritten_title}.jpg")
                    with open(image_path, 'wb') as image_file:
                        image_file.write(response.content)
                    rows.append((rewritten_title, entry['content'], rewritten_title, 0))

# Write the extracted data into a CSV file
with open("./data/real_scraping/bbc_news.csv", 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # Write header
    writer.writerow(['Title', 'Text', 'Image', 'Label'])
    # Write rows
    writer.writerows(rows)