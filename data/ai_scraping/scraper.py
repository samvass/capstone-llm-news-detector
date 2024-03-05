import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
import re
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)
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
paragraphs = []
paragraphs_df = []
images = []
j = 0 

print(len(news_links))
os.makedirs('AI_articles', exist_ok=True)



hello = 1
test_set = set()
for link in news_links:
    t,p,i = parse_news_article(link)
    titles.append(t)

    if (test_set.__contains__(t)):
        print("ALREADY DONE " + str(hello))
        hello += 1
    

    test_set.add(t)
    paragraphs_df.append(p)
    paragraphs.extend(p)
    images.append(i)

    # Concatenate all paragraphs into a single string
    full_text = '\n\n'.join(p)
    sanitized_title = sanitize_filename(t)

    # Save the concatenated text into a single file in 'AI_texts' folder
    file_path = os.path.join("./AI_articles", f"{sanitized_title}.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(full_text)
        # print(hello)

    # print(hello)
    
# create pd df to store the data
df = pd.DataFrame({
    'Title': titles,
    'Paragraph': paragraphs_df,
    'Image': images
})
df
def count_items_in_folder(folder_path):
    count = 0
    for _, _, files in os.walk(folder_path):
        count += len(files)
    return count

folder_path = "./AI_articles"
num_items = count_items_in_folder(folder_path)
print(num_items)