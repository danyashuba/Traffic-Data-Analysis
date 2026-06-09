from graphics import *
import csv
import math


def find_coefficient(elm_data: list, hanley_data: list):
    
    """
        This function is used to find the appropriate coefficient for the histogram to fit in the window.
        It takes the lists of numbers of cars hourly recorded on Elm Avenue/Rabbit Road and Hanley Highway/Westway junctions.
        Each index of the list represents the hour: e.x. elm_data[1] shows how many cars were recorded on  Elm Avenue/Rabbit Road at 01:00.
        This function returns the coeficient which will be used while representing the numbers on the histogram.
    """
    
    max_value = max([max(elm_data), max(hanley_data)])          # to find the highest number of vehicles recorded on both Elm Avenue/Rabbit Road and Hanley Highway/Westway
    coefficient = 1
    while True:                                                 # to iterate through infinite numbers
        interim_value = max_value * coefficient                 # to find how far it will be shown on graph (the established height equels to 800)
        if interim_value >= 670:                                # as we put the legend of the histogram on the height of starting from 690, it is better to allow more space. That is why 670 was chosen.
            break                                               # to exit the loop, as we found the coefficient we were interested in
        coefficient += 1
    return coefficient - 1                                      # as we excessed the height of the chart, we need to take a lower value 
    
    
def histogram(day: str, month: str, year: str, elm_data: list, hanley_data: list):
    
    """
        This function is used to create the histogram on the number of vehicles coming through Elm Avenue/Rabbit Road and Hanley Highway/Westway each hour.
        It takes the day, month and year to set the appropriate title.
        It also takes the lists of numbers of cars hourly recorded on Elm Avenue/Rabbit Road and Hanley Highway/Westway junctions.
        As a result, it makes the histogram appear on the screen.
    """
    
    win = GraphWin(f"Histogram {day}/{month}/{year}", 1400, 800)                             # to set the histogram, which is called Historgram and the appropriate date (we use format string to make it versatile). The width of the window is 1400, and the height of the window is 800.
    win.setBackground('white')                                                               # to make the window white
    win.setCoords(0, 0, 1400, 800)                                                           # to make the coordinate system more similar to Cartesian coordinate system: the (0, 0) point starts at the lower left edge when the (1400, 800) point is at the upper right edge.
    title = Text(Point(1200, 750), f"Hourly volume of vehicles on ({day}/{month}/{year})")   # to set the title at the right edge and to give a more prescribed title
    title.setFace('times roman')                                                             # to set the face to times roman
    title.setSize(20)                                                                        # to make the font equal to 20
    title.setStyle('bold')                                                                   # to make it bold
    title.setTextColor('black')                                                              # to make the text appear in black
    title.draw(win)                                                                          # to put the text on our window
    
    rect_elm = Rectangle(Point(1026, 715), Point(1046, 735))                                # to create legend at the right for Elm Avenue/Rabbit Road
    rect_elm.setFill("blue")                                                                # to make it blue
    rect_elm.draw(win)                                                                      # to put the text on our window
    
    elm_title = Text(Point(1223, 725), "The traffic volume on Elm Avenue/Rabbit Road")      # to put the text near the rectangle to state what this color means
    elm_title.setSize(16) # set the font to 16
    elm_title.draw(win) # to show it on our chart
    
    rect_hanley = Rectangle(Point(1026, 690), Point(1046, 710)) # to create legend at the right for Hanley Highway/Westway
    rect_hanley.setFill("red") # to state what red bars represent
    rect_hanley.draw(win) # to show it on our chart
    
    hanley_title = Text(Point(1223, 700), "The traffic volume on Hanley Highway/Westway") # to set the text on it
    hanley_title.setSize(16)
    hanley_title.draw(win)
    
    x_axis = Line(Point(50, 50), Point(1300, 50))
    x_axis.setWidth(2)
    x_axis.draw(win)
    
    coefficient = find_coefficient(elm_data=elm_data, hanley_data=hanley_data) # found coefficient
    
    i = 100             # manually chosen number to position bars and times (x coordinate)
    for hour in range(24): # to iterate through each hour (0 is 12 am; 23 - 23:00)
        elm_vol = elm_data[hour] # hour is index 
        hanley_vol = hanley_data[hour]
        hour = str(hour)
        if len(hour) == 1: 
            hour = '0' + hour
        hour_text = Text(Point(i, 43), hour)
        hour_text.draw(win)
        

        rect_vol_elm = Rectangle(Point(i - 15, 50), Point(i - 5, elm_vol * coefficient)) # manually chosen numbers (each bar)
        rect_vol_elm.setFill("blue")
        rect_vol_elm.draw(win)
        
        vol_elm_title = Text(Point(i - 7.5, (elm_vol * coefficient) + 5), str(elm_vol)) # in the middle of rectangle (that i why -7.5)
        vol_elm_title.draw(win)
        
        rect_vol_hanley = Rectangle(Point(i + 5, 50), Point(i + 15, hanley_vol * coefficient))
        rect_vol_hanley.setFill("red")
        rect_vol_hanley.draw(win)
        
        vol_hanley_title = Text(Point(i + 7.5, (hanley_vol * coefficient) + 5), str(hanley_vol))
        vol_hanley_title.draw(win)
        i += 50             # to move x coordinate
        
    
    y_axis = Line(Point(50, 50), Point(50, 690)) # create an y axis
    y_axis.setWidth(2)
    y_axis.draw(win)
    
    win.getMouse()
    win.close()


def require_day():
    while True:                 # keep asking user
        try:
            day = input("Please enter the day of the survey in the format dd: ") 
            int_day = int(day) # if it is not possible to make it int then it will be an exeption
            if int_day >= 1 and int_day <= 31:
                break
            else:
                print("Out of range - values must be in the range 1 to 31")
        except:
            print("Integer required")
    return day


def require_month():
    while True:
        try:
            month = input("Please enter the month of the survey in the format MM: ")
            int_month = int(month)
            if int_month >= 1 and int_month <= 12:
                break
            else:
                print("Out of range month - values must be in the range 1 to 12")
        except:
            print("Integer required")
    return month


def require_year():
    while True:
        try:
            year = input("Please enter the year of the survey in the format YYYY: ")
            int_year = int(year)
            if int_year >= 2000 and int_year <= 2024:
                break
            else:
                print("Out of range year - values must be in the range 2000 to 2024")
        except:
            print("Integer required")
    return year
    
           
while True:
    
    data_list = []   # An empty list to load and hold data from csv file

    day = require_day()
    month = require_month()
    year = require_year()

    outcomes = [] # to keep the results of each task

    data_file_required = f"traffic_data{day}{month}{year}.csv" # selected file
    outcomes.append(f"You have chosen the file named {data_file_required}")

    # Code to load the csv file into dataList
    with open(data_file_required, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)

    # The code below accesses and prints different elements of data_list
    
    # the number of elements in data_list equals to the total number of vehicles
    total_vehicles = len(data_list)
    outcomes.append(f"There were {total_vehicles} vehicles passing through all junctions on {day}/{month}/{year}")

    number_of_trucks = 0
    for row in data_list:
        if row[8].lower() == 'truck': # the 9th column represents (Vehicle Type)
            number_of_trucks += 1
    outcomes.append(f"There were {number_of_trucks} trucks passing through all junctions on {day}/{month}/{year}")

    number_of_electric_vehicles = 0
    for row in data_list:
        if row[9].lower() == 'true': # the 10th column represents whether the car is electric
            number_of_electric_vehicles += 1
    outcomes.append(f"There were {number_of_electric_vehicles} electric vehicles passing through all junctions on {day}/{month}/{year}")
        
    number_of_two_wheeled = 0
    for row in data_list:
        if row[8].lower() == 'bicycle' or row[8].lower() == 'motorcycle' or row[8].lower() == 'scooter' or row[8].lower() == 'bike' or row[8].lower() == 'motorbike':
            number_of_two_wheeled += 1
    outcomes.append(f"There were {number_of_two_wheeled} two wheeled vehicles passing through all junctions on {day}/{month}/{year}")

    busses_traveling_north = 0
    for row in data_list:
        if row[0] == 'Elm Avenue/Rabbit Road' and (row[8].lower() == 'bus' or row[8].lower() == 'buss') and row[4].lower() == 'n':
            busses_traveling_north += 1
    outcomes.append(f"There were {busses_traveling_north} busses leaving Elm Avenue/Rabbit Road heading north on {day}/{month}/{year}")

    # number of cars not traveling right or left 
    no_turning = 0
    for row in data_list:
        if row[3] == row[4]: # they kept their way. There are 4th column which shows the travel direction in and 5th column which shows the trevel direction out. If they stay the same then no turns have been made
            no_turning += 1
    outcomes.append(f"There were {no_turning} vehicles which did not turn right or left on junctions on {day}/{month}/{year}")  

    truck_perc = round((number_of_trucks / total_vehicles) * 100)
    outcomes.append(f"There were {truck_perc} % of vehicles recoreded as trucks on {day}/{month}/{year}")

    number_bicycles = 0
    for row in data_list:
        if row[8].lower() == 'bicycle': # vehicle type is bicycle
            number_bicycles += 1
    bicycles_per_hour_perc = round(number_bicycles / 24)
    outcomes.append(f"The average number of bicycles on {day}/{month}/{year} is {bicycles_per_hour_perc}")

    over_speed_vehicles = 0
    for row in data_list:
        if float(row[7]) > float(row[6]): # the 8th column shows Vehicle's speed while the 7th column shows the speed limit
            over_speed_vehicles += 1
    outcomes.append(f"The total number of vehicles recorded as over the speed limit for {day}/{month}/{year} is {over_speed_vehicles}")

    elm_avenue_vehicles = 0
    for row in data_list:
        if row[0] == 'Elm Avenue/Rabbit Road': # first column contains the name of junction
            elm_avenue_vehicles += 1
    outcomes.append(f"The total number of vehicles recorded through only Elm Avenue/Rabbit Road junction for {day}/{month}/{year} is {elm_avenue_vehicles}")

    hanley_vehicles = 0
    for row in data_list:
        if row[0] == 'Hanley Highway/Westway':
            hanley_vehicles += 1
    outcomes.append(f"The total number of vehicles recorded through only Hanley Highway/Westway junction for {day}/{month}/{year} is {hanley_vehicles}")

    scooter_elm = 0
    for row in data_list:
        if row[0] == 'Elm Avenue/Rabbit Road' and row[8].lower() == 'scooter': 
            scooter_elm += 1
    perc_scooters = round((scooter_elm / elm_avenue_vehicles) * 100)
    outcomes.append(f"The percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters (rounded to integer) for {day}/{month}/{year} is {perc_scooters}")

    number_vehicles_peak = 0
    for hour in range(24):
        interim_num = 0
        for row in data_list:
            if int(row[2][:2]) == hour and row[0] == 'Hanley Highway/Westway': # the 3d column contains time. First two symbols show hour
                interim_num += 1
        if interim_num > number_vehicles_peak:
            number_vehicles_peak = interim_num
        
    outcomes.append(f"The number of vehicles recorded in the peak (busiest) hour on Hanley Highway/Westway is {number_vehicles_peak}")

    for hour in range(24):
        interim_num = 0
        for row in data_list:
            if int(row[2][:2]) == hour and row[0] == 'Hanley Highway/Westway':
                interim_num += 1
        if interim_num == number_vehicles_peak:
            hour_1 = str(hour)
            hour_2 = str(hour + 1)
            if len(hour_1) == 1:
                hour_1 = '0' + hour_1
            elif len(hour_2) == 1:
                hour_2 = '0' + hour_2
                
            outcomes.append(f"The most vehicles through Hanley Highway/Westway on {day}/{month}/{year} were recorded between {hour_1}:00 and {hour_2}:00")


    rain_data = [] # to handle those data where it was rainy
    for row in data_list:
        if 'rain' in row[5].lower(): # 6th column shows the weather condtions
            rain_data.append(row)  
    hours = []     
    for row in rain_data:
        hour = int(row[2][:2])
        hours.append(hour)
    rain_hours = len(set(hours))   
    outcomes.append(f"The total number of hours of rain on {day}/{month}/{year} is {rain_hours}")

    for outcome in outcomes: # to print each result
        print(outcome)
        
    with open("results.txt", "a") as file: # to put the result into a txt file. 'a' is used to keep previously saved information ('w' would clear the content).
        for outcome in outcomes:
            file.write(f"{outcome}\n")
    
    # data for the histogram
    elm_hourly = []           # to handle the number of cars on Elm Avenue/Rabbit Road each hour
    hanley_hourly = []        # to handle the number of cars on Hanley Highway/Westway each hour
    for hour in range(24):
        elm_vehicles = 0
        hanley_vehicles = 0
        for row in data_list:
            if int(row[2][:2]) == hour and row[0] == 'Elm Avenue/Rabbit Road':
                elm_vehicles += 1
            elif int(row[2][:2]) == hour and row[0] == 'Hanley Highway/Westway':
                hanley_vehicles += 1
        elm_hourly.append(elm_vehicles)
        hanley_hourly.append(hanley_vehicles)
    histogram(day=str(day), month=str(month), year=str(year), elm_data=elm_hourly, hanley_data=hanley_hourly)

    # to ask user whether he wants to choose anothe dataset: the program will stop only if user enters 'n' or 'N'
    user_decision = input("Do you want to select a data file for a different date? (Y/N) ")
    
    if user_decision.lower() == 'n':
        print("Thank you. Have a good day!")
        break
    elif user_decision.lower() == 'y':
        with open("results.txt", "a") as file:
            file.write("\n") # to create a new line
            file.write("*" * 60) # to add 60 stars
            file.write("\n" * 2)    # to allow more space
        continue 
      
