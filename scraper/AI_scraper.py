import requests
from bs4 import BeautifulSoup as bs
import unicodedata
import pandas as pd
import os
import re

def sanitize_filename(filename):
    # Replace non-English characters with their English letter equivalents
    normalized_filename = ''.join(c for c in unicodedata.normalize('NFD', filename) if unicodedata.category(c) != 'Mn')
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', normalized_filename)

def parse_news_article(link):
    response = requests.get(link)
    soup = bs(response.content, features='html.parser')
    
    # get title
    title = soup.find('h1', class_="fusion-title-heading title-heading-left").text
    
    # get text content
    p_section = soup.find('div', class_="fusion-content-tb fusion-content-tb-1")
    p = p_section.find_all('p') if p_section else []
    p = [x.text for x in p]
    
    # image
    img_url = soup.find('img', alt=title)['src']
    img_response = requests.get(img_url)

    os.makedirs('images', exist_ok=True)
    
    # title_fixed = title.replace(" ", "_").replace("/", "_").replace(";", "").replace("'", "").replace(",", "").replace("“", "").replace("”", "").replace(":", "").replace("’", "").replace("-", "")
    sanitize_img_filename = sanitize_filename(title)
    img_filename = f"images/{sanitize_img_filename}.jpg"
    
    # Save image to the file
    if img_response.status_code == 200:
        with open(img_filename, 'wb') as img_file:
            # print(img_filename)
            img_file.write(img_response.content)
    else:
        print(f"Failed to fetch image from {img_url}. Status code: {img_response.status_code}")

        
    img_filename = img_filename.split('/')[1]
    
    # return parsed article
    return title, p, img_filename

def get_articles_links(homepage_url, news_links):
    response = requests.get(homepage_url)
    soup = bs(response.content, features='html.parser')

    # parse through main news page
    news_a_tags = soup.find_all('a', class_="awb-custom-text-color awb-custom-text-hover-color")

    for link in news_a_tags:
        news_links.append(link['href'])

news_links = []

# loops through 5 pages of homepage and stores the link from every news article
for page_num in range(1,6):
    base_url = 'https://newsgpt.ai/ai-news/page/'
    updated_url = base_url + str(page_num) 
    get_articles_links(updated_url, news_links)

titles = []
paragraphs_df = []
images = []

# os.makedirs('data/AI_articles', exist_ok=True)

for link in news_links:
    t,p,i = parse_news_article(link)
    sanitized_title = sanitize_filename(t)

    titles.append(sanitized_title)
    
    p_single_string = ' '.join(p)
    paragraphs_df.append(p_single_string)
    images.append(i)

# create pd df to store the data
df = pd.DataFrame({
    'Title': titles,
    'Paragraph': paragraphs_df,
    'Image': images
})

# Save to CSV
df.to_csv('./data/ai_data/AI_data.csv', index=False)

print(df)