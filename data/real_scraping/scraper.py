#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs
import os
import pandas as pd
import re

current_dir = './data/real_scraping'
dataset_dir = './data/datasets'

def get_image_from_article(row):
    title = row['Title']
    response = requests.get(row['Url'])
    soup = bs(response.content, features='html.parser')

    container_element = soup.find('div', class_='image__container')

    if container_element:
        img_tag = container_element.find('img')

        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None

    else:
        img_url = None

    if img_url:
        img_response = requests.get(img_url)

        os.makedirs(f'{current_dir}/images', exist_ok=True)

        title = title.replace(" ", "_").replace(".", "_")
        img_filename = f"{current_dir}/images/{title}.jpg"

        with open(img_filename, 'wb') as img_file:
            img_file.write(img_response.content)

        img_filename = img_filename.split('/')[1]
    else:
        img_filename = 'no_image_available.jpg'  # Example placeholder

    return img_filename

def sanitize_text(text):
  pattern = r'\(\s*CNN\s*.*?\)|\[\s*CNN\s*.*?\]'
  text = re.sub(pattern, '', text)
  return text

def sanitize_title(title):
  return title[:-6]

if __name__ == "__main__":

    # get the df
    df = pd.read_csv(f'{current_dir}/CNN_Articels_clean.csv')
    df = df.iloc[:250]

    # reformatting
    df.rename(columns={'Headline': 'Title', 'Article text': 'Text'}, inplace=True)

    df.loc[:, 'Text'] = df.apply(lambda row: sanitize_text(row['Text']), axis=1) # sanitize text
    df.loc[:, 'Title'] = df.apply(lambda row: sanitize_title(row['Title']), axis=1) # sanitize titles
    df['Image'] = df.apply(lambda row : get_image_from_article(row), axis=1) # get images

    df['Label'] = 0 # add labels
    df = df[['Title','Text','Label', 'Image']] # strip uneccessary columns

    df.to_csv(f"{current_dir}/real_dataset.csv")