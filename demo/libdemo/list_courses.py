from bs4 import BeautifulSoup

f = open("courses.xml", "rt")
bs = BeautifulSoup(f.read(), "lxml-xml")
courses = bs.find_all("course")
for course in courses:
    title = course.find("title").text
    duration = course.find("duration").text
    fee = course.find("fee").text
    print(f"{title:20} {fee:5} {duration:3}")

f.close()