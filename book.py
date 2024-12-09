import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
bookurl="https://books.toscrape.com/"

bookheader={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

bookresp=rq.get(url=bookurl,headers=bookheader)

booksoup=BeautifulSoup(bookresp.content,'html.parser')

#print('booksoup',booksoup)

bookname= booksoup.find_all('h3')

book= [book.text for book in bookname]
booklist=pd.DataFrame(book,columns=['book name'])
booklist.to_csv('bookname.csv')