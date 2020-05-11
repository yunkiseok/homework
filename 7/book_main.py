import requests
from bs4 import BeautifulSoup
from book_func import crawl
import csv

file = open("naver_books.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["title", "img_src", "link", "author", "publisher", "price"])

final_result = []
for i in range(8):
    print(f"{i+1}번째 페이지 크롤링 중..")
    html = requests.get(f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}")
    doc = BeautifulSoup(html.text, "html.parser")
    book_list_box = doc.find("ol", {"class" : "basic"})
    book_list = book_list_box.find_all("li")

    final_result += crawl(book_list)

for result in final_result:
    row = []
    row.append(result["title"])
    row.append(result["img_src"])
    row.append(result["link"])
    row.append(result["author"])
    row.append(result["publisher"])
    row.append(result["price"])
    writer.writerow(row)

print("크롤링 끝!")