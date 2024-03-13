import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import ast

# Load environment variables from .env file
load_dotenv()

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are in charge of rewriting text documents to your best abilities."),
    ("user", "{input}")
])

chain = prompt | llm 

df = pd.read_csv("AI_data.csv")
# df['Paragraph'] = df['Paragraph'].apply(ast.literal_eval)

rewritten_data = []

count = 0

# Loop through each .txt file, rewrite using GPT-3.5, and save to new directory
for index, row in df.iterrows():

    if (count == 10):
        break
    count += 1

    article_title = row["Title"]
    article_text = row["Paragraph"]
    article_image = row["Image"]
        
    # Process each paragraph individually
    print("************ TEXT ************")
    print(article_text)

    rewritten_article_text = chain.invoke({"input": article_text})
    rewritten_article_text = rewritten_article_text.content
    print("************ REWRITTEN TEXT ************")
    new_rewritten_article_text = rewritten_article_text.replace("\\'", "'").replace('""', '"').replace('\n', '')
    print(new_rewritten_article_text)
    print('\n')

    rewritten_data.append({
        'Title': article_title,
        'Paragraph': new_rewritten_article_text,
        'Image': article_image
    })

rewritten_df = pd.DataFrame(rewritten_data)
rewritten_df.to_csv('rewritten_AI_data.csv', index=False)