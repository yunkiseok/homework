import requests
from bs4 import BeautifulSoup
from corona_func import crawl
import csv

hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'

hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")

# 이제부터 시도, 시군구, 선별진료소(이름), 전화번호 크롤링 후 csv 파일에 저장하시면 됩니다!
file = open("corona_hospital.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["provinces&cities", "district", "hospital name", "phone number"])


corona_list_box = hospital_soup.find("tbody", {"class" : "tb_center"})
corona_list = corona_list_box.find_all("tr")

final_result = []
final_result += crawl(corona_list)

for result in final_result:
    row = []
    row.append(result["provinces"])
    row.append(result["district"])
    row.append(result["name"])
    row.append(result["phone_number"])
    writer.writerow(row)
