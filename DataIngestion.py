# text Loader
print('Text loader')
from langchain_community.document_loaders import TextLoader
loader=TextLoader('Speech.txt')
print(loader)

print('--------------')

text_documents=loader.load()
print(text_documents)
print('--------------')
#Reading the pdf
print('Reading the pdf')
from langchain_community.document_loaders import  PyPDFLoader
loader=PyPDFLoader('attention.pdf')
docs=loader.load()
print(docs)

print('--------------')

#web based loader
print('web based loader')
from langchain_community.document_loaders import WebBaseLoader
loader=WebBaseLoader(web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/"))
print(loader.load())
print('-----------------')
