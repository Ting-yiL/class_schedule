from class_info import raw_data
from course_info_management import Course
from current_time import get_day, time_check
from GUI import *

course_list = raw_data["Course Title"].to_list()
date_list = raw_data["Date"].to_list()
time_list = raw_data["Time"].to_list()
platform_list = raw_data["Platform"].to_list()
link_list = raw_data["Link"].to_list()
today = get_day()
course_list_obj = [Course(course) for course in course_list]
have_class = False

for i in range(len(course_list_obj)):
    course = course_list_obj[i]
    course.date = date_list[i]
    course.time = time_list[i]
    course.platform = platform_list[i]
    course.link = link_list[i]

for course in course_list_obj:
    if course.date == "Fri" and time_check(current_time="08", class_time="09.00-12.00"):
        gui = GUI()
        gui.COURSE_LINK = course.link
        gui.COURSE_TITLE = course.title
        gui.COURSE_DATE = course.date
        gui.COURSE_TIME = course.time
        gui.PLATFORM = course.platform
        gui.setup()
        have_class = True

if not have_class:
    print("No class Today!!!")

