import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are in charge of rewriting text documents to your best abilities."),
    ("user", "{input}")
])

chain = prompt | llm 


# Set up input and output directories
input_dir = "data"
output_dir = "new_data"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get list of .txt files in input directory
txt_files = [file for file in os.listdir(input_dir) if file.endswith('.txt')]

# Loop through each .txt file, rewrite using GPT-3.5, and save to new directory
for file_name in txt_files:
    input_file_path = os.path.join(input_dir, file_name)
    output_file_path = os.path.join(output_dir, "new_" + file_name)
    
    with open(input_file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    print("************ TEXT ************")
    print(text)
    
    rewritten_text = chain.invoke({"input": text})

    print("************ REWRITTEN TEXT ************")
    print(rewritten_text.content)
    print('\n')


    # Save rewritten text to new file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(rewritten_text.content)