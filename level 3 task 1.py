import requests
from bs4 import BeautifulSoup
try:
    url=str(input("url-> "))
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print("\nList of specific datas=")
    print("Type 1 for <a> tags")
    print("Type 2 for <p> tags")
    print("Type 3 for <heading> tags")
    print("Type 4 for <img> tags")
    print("Type 5 for <ul> tags")
    print("Type 6 for <ol> tags")
    print("Type 7 for <table> tags")
    print("Type 8 for <span> tags")
    print("Type 9 for <b> tags")
    print("Type 10 for <u> tags")
    print("Type 11 for <strong> tags")
    print("Type 12 for <title> tags")
    print("Type 13 for <head> tags")
    print("Type 14 for <body> tags")
    print("Type 15 for <html> tags")
    print("Type 16 for <i> tags")
    print("Type 17 for <div> tags")
    print("Type 18 for <frame> tags")
    print("Type 19 for <em> tags")
    print("Type 20 for <form> tags")

    choice=int(input("choice="))



    if choice==1:
        links = soup.find_all('a')
        for link in links:
            print("Link:", link.get('href'))


    if choice==2:        
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print("Paragraph:", paragraph.get_text())


    if choice==3:        
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        for heading in headings:
            print("Heading:", heading.get_text())


    if choice==4:        
        images = soup.find_all('img')
        for image in images:
            print("Image Source:", image.get('src'))


    if choice==5:        
        lists = soup.find_all('ul')
        for ul in lists:
            items = ul.find_all('li')
            for item in items:
                print("List Item:", item.get_text())


    if choice==6:            
        lists = soup.find_all('ol')
        for ol in lists:
            items = ol.find_all('li')
            for item in items:
                print("List Item:", item.get_text())

    if choice==7:            
        tables = soup.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                for cell in cells:
                    print("Table Cell:", cell.get_text())


    if choice==8:
        spans = soup.find_all('span')
        for span in spans:
            print("Span Text:", span.get_text())

    if choice==9:
        bolds = soup.find_all('b')
        for bold in bolds:
            print("Bold Text:", bold.get_text())

    if choice==10:
        underlines = soup.find_all('u')
        for underline in underlines:
            print("Underline Text:", underline.get_text())

    if choice==11:
        strongs = soup.find_all('strong')
        for strong in strongs:
            print("Strong Text:", strong.get_text())

    if choice==12:
        title = soup.find('title')
        if title:
            print("Title:", title.get_text())

    if choice==13:
        head = soup.find('head')
        if head:
            print("Head:", head.get_text())

    if choice==14:
        body = soup.find('body')
        if body:
            print("Body:", body.get_text())

    if choice==15:
        html = soup.find('html')
        if html:
            print("HTML:", html.get_text())

    if choice==16:
        italics = soup.find_all('i')
        for italic in italics:
            print("Italic Text:", italic.get_text())

    if choice==17:
        divs = soup.find_all('div')
        for div in divs:
            print("Div Text:", div.get_text())

    if choice==18:
        frames = soup.find_all('frame')
        for frame in frames:
            print("Frame Source:", frame.get('src'))

    if choice==19:
        ems = soup.find_all('em')
        for em in ems:
            print("Emphasized Text:", em.get_text())

    if choice==20:
        forms = soup.find_all('form')
        for form in forms:
            print("Form Action:", form.get('action'))
except:
    print("Wrong Input.")
