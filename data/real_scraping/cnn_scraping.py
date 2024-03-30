#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import os
import re
import unicodedata


config = {
    "cnn_articles_path": "./CNN.csv",
    "saved_images_path": "./cnn_images",
    "csv_file_path": "./cnn_dataset.csv",
}

def get_cnn_articles_dataframe(num_articles: int) -> str:
    df = pd.read_csv(config["cnn_articles_path"])[:num_articles]
    df.rename(columns={'Headline':'Title', 'Article text': 'Text'}, inplace=True)
    return cnn_df

def sanitize_title(title: str) -> str:
    title = title[:-6] # remove the [CNN] tag at the end of title
    return title

def sanitize_text(text: str) -> str:
    pattern = r'\(\s*CNN\s*.*?\)|\[\s*CNN\s*.*?\]'
    text = re.sub(pattern, '', text)
    return text

def sanitize_filename(filename: str, replace=' ', max_length=255) -> str:
    # Normalize Unicode characters to their closest ASCII representation
    filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')
    
    # Replace unwanted characters
    filename = re.sub(r'[\/:*?"<>|\r\n\t]+', replace, filename)
    
    # Replace spaces with a chosen character (e.g., underscore)
    filename = re.sub(r'\s+', replace, filename).strip(replace)
    
    # Ensure the filename is not too long
    filename = filename[:max_length].rstrip(replace)
    
    filename = filename.lower()
    
    return filename

def find_article_img(article: pd.Series) -> str:
    
    # get the article
    res = requests.get(article['Url'])

    # find the main image from the article
    soup = bs(res.content, features='html.parser')
    container_element = soup.find('div', class_='image__container')  
    
    if container_element:
        img_tag = container_element.find('img')
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None

    else:
        img_url = None

    if img_url:

        img_res = requests.get(img_url)

        os.makedirs(config["saved_images_path"], exist_ok=True)

        filename = sanitize_filename(article['Title'])

        img_path = f"{config["saved_images_path"]}/{filename}.jpg"

        with open(img_path, 'wb') as img_file:
            img_file.write(img_res.content)

    else:
        filename = 'no_image_available.jpg'  # Example placeholder

    return filename

if __name__ == "__main__":
    cnn_df = get_cnn_articles_dataframe(250)
    cnn_df['Text'] = cnn_df['Text'].apply(sanitize_text)
    cnn_df['Title'] = cnn_df['Title'].apply(sanitize_title)
    cnn_df['Image'] = cnn_df.apply(lambda article : find_article_img(article), axis=1)
    cnn_df['Label'] = 0 # non ai articles
    
    cnn_df = cnn_df[['Title','Text','Image', 'Label']] # strip uneccessary columns
    cnn_df.to_csv(config["csv_file_path"], index=False)





