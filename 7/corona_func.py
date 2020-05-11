def crawl(corona_list):
    result = []
    for corona in corona_list:
        provinces = corona.contents[1].text
        district = corona.contents[2].text
        name_box = corona.contents[3].text
        if "*" in name_box: 
            name = name_box[:-10]
        else: 
            pass
        phone_number = corona.contents[4].text


        corona_info = {
            "provinces" : provinces,
            "district" : district,
            "name" : name,
            "phone_number" : phone_number,
        }
        result.append(corona_info)

    return result