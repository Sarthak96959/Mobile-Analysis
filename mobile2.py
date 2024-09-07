for number in range(1,43):
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh:",number)
    from bs4 import BeautifulSoup
    import csv

    # Read the HTML file
    with open(f'a{number}.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []
    # Find all divs with the specified class and data-tkid
    divs = soup.find_all('div', class_='tUxRFH')


    mob_name = []
    mob_price = []
    mob_rating = []
    mob_details = []
    mob_review = []


    for div in divs:
        try : 
            product_name = div.find("div",class_ = "KzDlHZ")
            name = product_name.get_text()
            mob_name.append(name)
        except :
            name = ""
            mob_name.append(name)
        
        try:
            product_price = div.find("div",class_ = "Nx9bqj _4b5DiR")
            price = product_price.get_text()
            mob_price.append(price)
        except:
            price = ""
            mob_price.append(price)
        
        try:
            product_rating = div.find("div",class_ = "XQDdHH")
            rating = product_rating.get_text(strip = True)
            mob_rating.append(rating)
        except :
            rating = "0"
            mob_rating.append(rating)

        try:
            r = div.find("div",class_ = "_5OesEi")
            review = r.find("span",class_ = "Wphh3N")
            revieww = []
            for kk in review:
                review = kk.get_text(strip = True)
                revieww.append(review)
                mob_review.append(review)
            
                

        except:
            mob_review.append("")
        
        details_div = div.find('div', class_='_6NESgJ')
        # for fine_details in details_div:
        m = details_div.find_all("li", class_="J+igdf")
        detailss = []
        for mobile_details in m:
            details = mobile_details.get_text()
            detailss.append(details)

        mob_details.append(detailss)

    
        
        
    #CLEANING PROCESS OF THE RAW DATA 
    #mob_name
    mob_price1 = []
    mob_star_rating = []
    ratings = []
    mob_review1 = []
    ram = []
    rom = []
    display = []
    brand = []
    mob_var = []
    battery = []
    camera = []
    # mob_details
    try:
        for i in mob_price:
            num = (i[1::]).replace(",","")
            mob_price1.append(int(num))
            # print(i)
    except :
        mob_price1.append("")

    for i in mob_rating:
        mob_star_rating.append(float(i))
    for  i in mob_review:
        r = list(i.split())
        if len(r) == 0:
            ratings.append(0)
        else:
            ratings.append(int(r[0].replace(",","")))
    for t in mob_review:
        if len(t) < 3:
            mob_review1.append(0)
        else:
            index  = t.find("&")
            fi_space = t.find(" ")
            se_space = t.find(" ",fi_space+1)
            numm = int(t[index+1:se_space].replace(",",""))
            mob_review1.append(numm)
    for i in mob_details:
        ram_rom = (i[0])
        lst = ram_rom.split("|")
        if len(lst) >1:
            ram_ = lst[0]
            try:
                ram.append(int(ram_[0]))
            except:
                ram.append("")

            rom_ = lst[1].split()
            print(rom_)
            try:
                rom.append(int(rom_[0]))
            except:
                rom.append("")
        else:
            ram.append("")
            rom.append("")

    for i in mob_name:
        lstt = i.split()
        brand.append(lstt[0])
    # i = mob_name[4]
        last_index = i.find("(")
        first_index = i.find(" ")
        mob_var.append(i[first_index:last_index])
    for i in mob_details:
        if "Battery" in i[3]:
            battery.append(i[3])
        else :
            battery.append("")

    for i in mob_details:
        if "Camera" in i[2]:
            camera.append(i[2])
        else :
            camera.append("")




    # WE HAVE FOLLOWING LIST WHICH WE HAVE TO CHANGE INTO DATAFRAME




    # battery = []
    # camera = []
    import pandas as pd
    mob_name_ = pd.DataFrame({"Mob_Name":mob_name})
    mob_price_ = pd.DataFrame({"Mob_Price":mob_price1})
    mob_star_rating_ = pd.DataFrame({"Mob_Star_Rating":mob_star_rating})
    ratings_ = pd.DataFrame({"Ratings":ratings})
    mob_review1_ = pd.DataFrame({"Mob_Review":mob_review1})
    ram1 = pd.DataFrame({"Ram":ram})
    rom1 = pd.DataFrame({"Rom":rom})
    display_ = pd.DataFrame({"Display":display})
    brand_ = pd.DataFrame({"Brand":brand})
    mob_var_ = pd.DataFrame({"Mob_Variant":mob_var})
    battery_ = pd.DataFrame({"Battery":battery})
    camera_ = pd.DataFrame({"Camera":camera})
    table = pd.concat([mob_name_,brand_,mob_var_,mob_price_,mob_star_rating_,ratings_,mob_review1_,ram1,rom1,display_,battery_,camera_],axis = 1)

    print(table)

    table.to_csv(f"a{number}.csv")



















