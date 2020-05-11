def crawl(yes_list):
    result=[]
    end = len(yes_list)

    for i in range(0, end):
        yes = yes_list[i]

        if (i+1) % 2 != 0:
            title = yes.find("td", {"class":"goodsTxtInfo"}).find("p").find("a")
            img_src = yes.find("img")["src"]
            author = yes.find("div", {"class":"aupu"}).find_all("a")[0].string
            publisher = yes.find("div", {"class":"aupu"}).find_all("a")[-1].string
            price = yes.find("span", {"class":"priceB"}).string

            yes_info={
            "title" : title,
            "img_src" : img_src,
            "author" : author,
            "publisher" : publisher,
            "price" : price
            }

        else:
            summary_box = yes.find("p",{"class":"read"})
            
            if summary_box != None:
                summary = summary_box.string
            else:
                summary = "없음"

            yes_info["summary"] = summary.strip()
            result.append(yes_info)

    return result