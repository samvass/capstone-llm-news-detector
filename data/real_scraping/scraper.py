def get_image_from_article(row):
    title = row['Headline']
    response = requests.get(row['Url'])
    soup = bs(response.content, features='html.parser')
        
    picture_element = soup.find('picture', class_='image__picture')

    if picture_element:
        img_tag = picture_element.find('img')

        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None

    else:
        img_url = None

    if img_url:
        img_response = requests.get(img_url)

        os.makedirs('cnn-images', exist_ok=True)

        img_filename = f"cnn-images/{title.replace(' ', '_').replace('/', '_')}.jpg"
        
        with open(img_filename, 'wb') as img_file:
            img_file.write(img_response.content)
        
        img_filename = img_filename.split('/')[1]
    else:
        img_filename = 'no_image_available.jpg'  # Example placeholder

    return img_filename