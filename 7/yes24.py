import requests
from bs4 import BeautifulSoup
from yes_func import crawl
import csv

file = open("yes24.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["Tilte", "Img Link", "Author", "Publisher", "Price", "Summary"])

final_result = []
for i in range(20):
    print(f"{i+1}번째 페이지 크롤링 중..")
    html = requests.get(f"http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03&PageNumber={i+1}")
    doc = BeautifulSoup(html.text, "html.parser")
    yes_list_box = doc.find("table", {"class" : "list"})
    yes_list = yes_list_box.find_all("tr")

    final_result += crawl(yes_list)

for result in final_result:
    row = []
    row.extend(result["title"])
    row.append(result["img_src"])
    row.append(result["author"])
    row.append(result["publisher"])
    row.append(result["price"])
    row.append(result["summary"])
    writer.writerow(row)

print("크롤링 끝!")