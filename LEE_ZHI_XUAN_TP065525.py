# Python Programming Individual Assignment
# Lee Zhi Xuan (TP065525)
# APD1F2206ME

# Colour class
# This sets the classes for colours used throughout the program. This code is purely aesthetic and will not inhibit
# the function of the program.
import os
os.system("")


class colour:
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    cyan = '\033[96m'
    yellow = '\033[93m'
    pink = '\033[95m'
    white = '\033[97m'


# This imports the text files of stations and the travel interval timings. Then, the contents of the files are
# converted into lists to be used throughout the program.
# Stations list
a_stations_file = open("a_stations.txt")
a_stations_file_contents = a_stations_file.read()
a_station_content_list = a_stations_file_contents.splitlines()
a_stations_file.close()
b_stations_file = open("b_stations.txt")
b_stations_file_contents = b_stations_file.read()
b_station_content_list = b_stations_file_contents.splitlines()
b_stations_file.close()
c_stations_file = open("c_stations.txt")
c_stations_file_contents = c_stations_file.read()
c_station_content_list = c_stations_file_contents.splitlines()
c_stations_file.close()

# Station timings
a_timings_file = open("a_timings.txt")
a_timings_file_contents = a_timings_file.read()
a_timings_content_list = a_timings_file_contents.splitlines()
a_timings_file.close()
b_timings_file = open("b_timings.txt")
b_timings_file_contents = b_timings_file.read()
b_timings_content_list = b_timings_file_contents.splitlines()
b_timings_file.close()
c_timings_file = open("c_timings.txt")
c_timings_file_contents = c_timings_file.read()
c_timings_content_list = c_timings_file_contents.splitlines()
c_timings_file.close()
start_timings_file = open("start_timings.txt")
start_timings_file_contents = start_timings_file.read()
start_time_list = start_timings_file_contents.splitlines()
start_timings_file.close()


# KTM title screen
# This is the title logo of the program. This code is purely aesthetic.
def page_title():
    print(colour.bold + colour.blue + "\n=========================================" + colour.end)
    print(colour.bold + colour.yellow + "=====" + colour.white + " Malayan Railway Limited (KTM) "
          + colour.yellow + "=====" + colour.end)
    print(colour.bold + colour.blue + "=========================================" + colour.end)


# Role selection page.
# This page is the first menu to run when the user starts the program. This page allows users to select whether to run
# the program as a customer or an admin. The two different roles allow for different functions.
def page_select_role():
    page_title()
    print(colour.bold + colour.green + "-=- " + colour.white + "Role Selection" + colour.green + " -=-" + colour.end)
    print("Welcome to the KTM train scheduling system. Which role do you wish to proceed as?")
    role_selected = 0
    while role_selected == 0:
        print(colour.bold + colour.cyan + "[Customer: '1', Admin: '2', Exit program: 'e']" + colour.end)
        user_role = str(input(colour.white + "Role: " + colour.end))
        if user_role == str(1):
            print(colour.bold + colour.pink + "Role selected: Customer\n" + colour.end)
            role_selected = 1
            page_role_customer()
        elif user_role == str(2):
            print(colour.bold + colour.pink + "Role selected: Admin\n" + colour.end)
            role_selected = 1
            page_role_admin_login()
        elif user_role == str('e'):
            print(colour.bold + colour.green + " -=- Thank you for using KTM Systems -=- " + colour.end)
            role_selected = 1
            input()
        else:   # error handling
            print(colour.bold + colour.red + "[!] Invalid role, please try again." + colour.end)


# Admin role login page.
# The user lands on this page after selecting the admin role. This page adds the password functionality to the program
# and only allow users with password to enter. The default password is 12345.
def page_role_admin_login():
    passed = 0
    fail_count = 0
    print(colour.bold + colour.red + "=-= " + colour.white + "Admin Login" + colour.red + " =-=" + colour.end)
    while passed == 0:
        print(colour.bold + colour.cyan + "[Back: 'b']" + colour.end)
        password = input(str(colour.white + "Please enter the password: " + colour.end))
        if fail_count >= 4:
            print(colour.bold + colour.red + "[!] Maximum login attempts reached, please try again later." + colour.end)
            passed = 1
            page_select_role()
        if password == str(1111):
            passed = 1
            print(colour.bold + colour.green + "Login successful.\n" + colour.end)
            page_admin_action()
        elif password == str('b'):
            passed = 1
            print(colour.bold + colour.pink + "Back to role selection page.\n" + colour.end)
            page_select_role()
        else:  # error handling
            fail_count = fail_count + 1
            attempts_left = 5 - fail_count
            print(colour.bold + colour.red + "[!] Incorrect password, please try again. Attempts left: ", attempts_left)


# Customer role page.
# The user lands on this page after selecting the customer role. This page allows the user to select which timetable
# they wish to view.
def page_role_customer():
    print(colour.bold + colour.green + "-=- " + colour.white + "Train Journey" + colour.green + " -=-" + colour.end)
    print("Which train journey schedule do you wish to view?")
    customer_journey_selection_complete = 0
    while customer_journey_selection_complete == 0:
        print(colour.bold + colour.cyan + "[Kuala Lumpur - Singapore: '1', Kuala Lumpur - Thailand Route A: '2', "
                                          "Kuala Lumpur - Thailand Route B: '3', Back: 'b', Exit program: 'e']" +
              colour.end)
        customer_journey_selection = str(input("Route: "))
        if customer_journey_selection == str('b'):
            customer_journey_selection_complete = 1
            print(colour.bold + colour.pink + "Back to role selection page.\n" + colour.end)
            page_select_role()
        elif customer_journey_selection == str('e'):
            customer_journey_selection_complete = 1
            print(colour.bold + colour.green + " -=- Thank you for using KTM Systems -=- " + colour.end)
            input()
        elif customer_journey_selection == str(1):
            customer_journey_selection_complete = 1
            print(colour.bold + colour.pink + "Journey selected: Kuala Lumpur - Singapore\n" + colour.end)
            page_customer_journey_kl_sg()
        elif customer_journey_selection == str(2):
            customer_journey_selection_complete = 1
            print(colour.bold + colour.pink + "Journey selected: Kuala Lumpur - Thailand Route A\n" + colour.end)
            page_customer_kl_thai_a()
        elif customer_journey_selection == str(3):
            customer_journey_selection_complete = 1
            print(colour.bold + colour.pink + "Journey selected: Kuala Lumpur - Thailand Route B\n" + colour.end)
            page_customer_kl_thai_b()
        else:  # error handling
            print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)


# Defining route between Kuala Lumpur and Singapore
# This compiles and displays the timetables for trains travelling between Kuala Lumpur and Singapore.
def page_customer_journey_kl_sg():
    page_title()
    print(colour.bold + colour.green + "-=- " + colour.white + "Kuala Lumpur - Singapore" + colour.green + " -=-"
          + colour.end)
    print("KTM offers 5 daily round trips from Kuala Lumpur to Singapore.")
    page_kl_sg_timetable(start_time_list[6], start_time_list[7])  # timetable functions with unique start times
    page_kl_sg_timetable(start_time_list[8], start_time_list[9])
    page_kl_sg_timetable(start_time_list[10], start_time_list[11])
    page_kl_sg_timetable(start_time_list[12], start_time_list[13])
    page_kl_sg_timetable(start_time_list[14], start_time_list[15])
    customer_journey_kl_sg_complete = 0
    while customer_journey_kl_sg_complete == 0:
        print(colour.bold + colour.cyan + "[Kuala Lumpur - Thailand Route A: '1', Kuala Lumpur - Thailand Route B: "
                                          "'2', Back: 'b', Exit program: 'e']" + colour.end)
        customer_journey_kl_sg = input(str(colour.white + "Action: " + colour.end))
        if customer_journey_kl_sg == str('b'):
            print(colour.bold + colour.pink + "Back to journey selection page.\n" + colour.end)
            customer_journey_kl_sg_complete = 1
            page_role_customer()
        elif customer_journey_kl_sg == str('e'):
            customer_journey_kl_sg_complete = 1
            print(colour.bold + colour.green + " -=- Thank you for using KTM Systems -=- " + colour.end)
            input()
        elif customer_journey_kl_sg == str(1):
            customer_journey_kl_sg_complete = 1
            print(colour.bold + colour.pink + "Action: View Kuala Lumpur - Thailand schedule Route A.\n" + colour.end)
            page_customer_kl_thai_a()
        elif customer_journey_kl_sg == str(2):
            customer_journey_kl_sg_complete = 1
            print(colour.bold + colour.pink + "Action: View Kuala Lumpur - Thailand schedule Route B.\n" + colour.end)
            page_customer_kl_thai_b()
        else:  # error handling
            print(colour.bold + colour.red + "[!] Invalid action, please try again." + colour.end)


# Defining Route Timetables
# Route Kuala Lumpur - Singapore
def page_kl_sg_timetable(a, b):
    print(colour.bold + "=========================" + colour.end)
    c_hour = int(a)  # importing the start hour and minute
    c_minute = int(b)
    c_departure = []  # creating empty lists
    c_arrival = []
    count = 0
    for i in range(len(c_timings_content_list) - 1):
        c_minute = c_minute + int(c_timings_content_list[i])  # adding the timings from list to start time in min
        count = count + 1
        while c_minute >= 60:  # time overflow, minute into hour
            c_minute = c_minute - 60
            c_hour = c_hour + 1
        while c_hour >= 24:  # time overflow, hour reduction
            c_hour = c_hour - 24
        c_time = str(c_hour).zfill(2) + ":" + str(c_minute).zfill(2)  # combining time to create a readable format
        if (count % 2) != 0:  # if count is odd number, it is a departure time.
            c_departure.append(c_time)
        else:  # if count is an even number, it is an arrival time.
            c_arrival.append(c_time)
    c_timings_content_list.reverse()  # reverse list for the return journey, the following is same as above.
    for i in range(len(c_timings_content_list) - 1):
        c_minute = c_minute + int(c_timings_content_list[i])
        count = count + 1
        while c_minute >= 60:
            c_minute = c_minute - 60
            c_hour = c_hour + 1
        while c_hour >= 24:
            c_hour = c_hour - 24
        c_time = str(c_hour).zfill(2) + ":" + str(c_minute).zfill(2)
        if (count % 2) != 0:
            c_departure.append(c_time)
        else:
            c_arrival.append(c_time)
    c_timings_content_list.reverse()  # reverse the list back to avoid future conflict
    count = 1
    c_duration = []
    for i in range(len(c_timings_content_list) - 1):  # for travel duration display
        if (count % 2) == 0:  # if count is even, it is a travel duration.
            c_duration.append(c_timings_content_list[i])
        count = count + 1
    c_timings_content_list.reverse()  # reverse the list for return journey, following is same as above.
    for i in range(len(c_timings_content_list) - 1):
        if (count % 2) == 0:
            c_duration.append(c_timings_content_list[i])
        count = count + 1
    c_timings_content_list.reverse()  # reverse the list back to avoid future conflict.
    count = 1
    print(colour.bold + f"{'Departure':21s} {'Destination':20s} {'Departure Time':20s} {'Arrival Time':20s} "
                        f"{'Travelling Duration (Min)':10s}" + colour.white)  # print header
    for i in range(len(c_station_content_list) - 1):  # printing the timetable
        print(f"{c_station_content_list[i]:15s} {'to':5s} {c_station_content_list[count]:20s} {c_departure[i]:20s} "
              f"{c_arrival[i]:20s} {c_duration[i]}")
        count = count + 1
    c_station_content_list.reverse()  # reverse the list for the return journey
    count = 1
    for i in range(len(c_station_content_list) - 1):
        print(f"{c_station_content_list[i]:15s} {'to':5s} {c_station_content_list[count]:20s} "
              f"{c_departure[i + (len(c_station_content_list) - 1)]:20s} "
              f"{c_arrival[i + (len(c_station_content_list) - 1)]:20s} "
              f"{c_duration[i + (len(c_station_content_list) - 1)]}")
        count = count + 1
    c_station_content_list.reverse()  # reverse list back to avoid future conflict.


# Route Kuala Lumpur - Thailand via Butterworth (Route A)
# These define the timetables for the route between Kuala Lumpur and Thailand via Butterworth, known as route A.
# The timetable functions the same as above, just with different lists. All the calculations and logic are the same.
def page_kl_thai_timetable_a(a, b):
    print(colour.bold + "=========================" + colour.end)
    a_hour = int(a)
    a_minute = int(b)
    a_departure = []
    a_arrival = []
    count = 0
    for i in range(len(a_timings_content_list) - 1):
        a_minute = a_minute + int(a_timings_content_list[i])
        count = count + 1
        while a_minute >= 60:
            a_minute = a_minute - 60
            a_hour = a_hour + 1
        while a_hour >= 24:
            a_hour = a_hour - 24
        a_time = str(a_hour).zfill(2) + ":" + str(a_minute).zfill(2)
        if (count % 2) != 0:
            a_departure.append(a_time)
        else:
            a_arrival.append(a_time)
    a_timings_content_list.reverse()
    for i in range(len(a_timings_content_list) - 1):
        a_minute = a_minute + int(a_timings_content_list[i])
        count = count + 1
        while a_minute >= 60:
            a_minute = a_minute - 60
            a_hour = a_hour + 1
        while a_hour >= 24:
            a_hour = a_hour - 24
        a_time = str(a_hour).zfill(2) + ":" + str(a_minute).zfill(2)
        if (count % 2) != 0:
            a_departure.append(a_time)
        else:
            a_arrival.append(a_time)
    a_timings_content_list.reverse()
    count = 1
    a_duration = []
    for i in range(len(a_timings_content_list) - 1):
        if (count % 2) == 0:
            a_duration.append(a_timings_content_list[i])
        count = count + 1
    a_timings_content_list.reverse()
    for i in range(len(a_timings_content_list) - 1):
        if (count % 2) == 0:
            a_duration.append(a_timings_content_list[i])
        count = count + 1
    a_timings_content_list.reverse()
    count = 1
    print(colour.bold + f"{'Departure':21s} {'Destination':20s} {'Departure Time':20s} {'Arrival Time':20s} "
                        f"{'Travelling Duration (Min)':10s}" + colour.white)
    for i in range(len(a_station_content_list) - 1):
        print(f"{a_station_content_list[i]:15s} {'to':5s} {a_station_content_list[count]:20s} {a_departure[i]:20s} "
              f"{a_arrival[i]:20s} {a_duration[i]}")
        count = count + 1
    a_station_content_list.reverse()
    count = 1
    for i in range(len(a_station_content_list) - 1):
        print(f"{a_station_content_list[i]:15s} {'to':5s} {a_station_content_list[count]:20s} "
              f"{a_departure[i + (len(a_station_content_list) - 1)]:20s} "
              f"{a_arrival[i + (len(a_station_content_list) - 1)]:20s} "
              f"{a_duration[i + (len(a_station_content_list) - 1)]}")
        count = count + 1
    a_station_content_list.reverse()


# Route Kuala Lumpur - Thailand via Kelantan (Route B)
# This defines the timetable for the route between Kuala Lumpur and Thailand via Kelantan/Terengganu, known as route B.
# The timetable functions the same as above, just with different lists. All the calculations and logic are the same.
def page_kl_thai_timetable_b():
    b_hour = int(start_time_list[4])
    b_minute = int(start_time_list[5])
    b_departure = []
    b_arrival = []
    count = 0
    for i in range(len(b_timings_content_list) - 1):
        b_minute = b_minute + int(b_timings_content_list[i])
        count = count + 1
        while b_minute >= 60:
            b_minute = b_minute - 60
            b_hour = b_hour + 1
        while b_hour >= 24:
            b_hour = b_hour - 24
        b_time = str(b_hour).zfill(2) + ":" + str(b_minute).zfill(2)
        if (count % 2) != 0:
            b_departure.append(b_time)
        else:
            b_arrival.append(b_time)
    b_timings_content_list.reverse()
    for i in range(len(b_timings_content_list) - 1):
        b_minute = b_minute + int(b_timings_content_list[i])
        count = count + 1
        while b_minute >= 60:
            b_minute = b_minute - 60
            b_hour = b_hour + 1
        while b_hour >= 24:
            b_hour = b_hour - 24
        b_time = str(b_hour).zfill(2) + ":" + str(b_minute).zfill(2)
        if (count % 2) != 0:
            b_departure.append(b_time)
        else:
            b_arrival.append(b_time)
    b_timings_content_list.reverse()
    count = 1
    b_duration = []
    for i in range(len(b_timings_content_list) - 1):
        if (count % 2) == 0:
            b_duration.append(b_timings_content_list[i])
        count = count + 1
    b_timings_content_list.reverse()
    for i in range(len(b_timings_content_list) - 1):
        if (count % 2) == 0:
            b_duration.append(b_timings_content_list[i])
        count = count + 1
    b_timings_content_list.reverse()
    count = 1
    print(colour.bold + f"{'Departure':21s} {'Destination':20s} {'Departure Time':20s} {'Arrival Time':20s} "
                        f"{'Travelling Duration (Min)':10s}" + colour.white)
    for i in range(len(b_station_content_list) - 1):
        print(f"{b_station_content_list[i]:15s} {'to':5s} {b_station_content_list[count]:20s} {b_departure[i]:20s} "
              f"{b_arrival[i]:20s} {b_duration[i]}")
        count = count + 1
    b_station_content_list.reverse()
    count = 1
    for i in range(len(b_station_content_list) - 1):
        print(f"{b_station_content_list[i]:15s} {'to':5s} {b_station_content_list[count]:20s} "
              f"{b_departure[i + (len(b_station_content_list) - 1)]:20s} "
              f"{b_arrival[i + (len(b_station_content_list) - 1)]:20s} "
              f"{b_duration[i + (len(b_station_content_list) - 1)]}")
        count = count + 1
    b_station_content_list.reverse()


# KL-Thai Butterworth Route A.
# This compiles and displays the timetables for Kuala Lumpur to Thailand via Butterworth route, route A.
def page_customer_kl_thai_a():
    page_title()
    print(colour.bold + colour.green + "-=- " + colour.white + "Kuala Lumpur - Thailand [Route A]" + colour.green
          + " -=-" + colour.end)
    page_kl_thai_timetable_a(start_time_list[0], start_time_list[1])
    page_kl_thai_timetable_a(start_time_list[2], start_time_list[3])
    customer_kl_thai_a_complete = 0
    while customer_kl_thai_a_complete == 0:
        print(colour.bold + colour.cyan + "[Kelantan route(B) : '1', Back: 'b', Exit program: 'e']" + colour.end)
        customer_kl_thai_a = input(str(colour.white + "Action: " + colour.end))
        if customer_kl_thai_a == str('b'):
            print(colour.bold + colour.pink + "Back to journey selection page.\n" + colour.end)
            customer_kl_thai_a_complete = 1
            page_role_customer()
        elif customer_kl_thai_a == str('e'):
            customer_kl_thai_a_complete = 1
            print(colour.bold + colour.green + " -=- Thank you for using KTM Systems -=- " + colour.end)
            input()
        elif customer_kl_thai_a == str(1):
            print(colour.bold + colour.pink + "View Kelantan route(B)\n" + colour.end)
            customer_kl_thai_a_complete = 1
            page_customer_kl_thai_b()
        else:  # error handling
            print(colour.bold + colour.red + "[!] Invalid action, please try again." + colour.end)


# KL-Thai Kelantan Route B.
# This compiles and displays the timetables for Kuala Lumpur to Thailand via Kelantan route, route B.
def page_customer_kl_thai_b():
    page_title()
    print(colour.bold + colour.green + "-=- " + colour.white + "Kuala Lumpur - Thailand [Route B]" + colour.green
          + " -=-" + colour.end)
    page_kl_thai_timetable_b()
    customer_kl_thai_b_complete = 0
    while customer_kl_thai_b_complete == 0:
        print(colour.bold + colour.cyan + "[Butterworth route(A) : '1', Back: 'b', Exit program: 'e']" + colour.end)
        customer_kl_thai_b = input(str(colour.white + "Action: " + colour.end))
        if customer_kl_thai_b == str('b'):
            print(colour.bold + colour.pink + "Back to journey selection page.\n" + colour.end)
            customer_kl_thai_b_complete = 1
            page_role_customer()
        elif customer_kl_thai_b == str('e'):
            customer_kl_thai_b_complete = 1
            print(colour.bold + colour.green + " -=- Thank you for using KTM Systems -=- " + colour.end)
            input()
        elif customer_kl_thai_b == str(1):
            print(colour.bold + colour.pink + "View Butterworth route(B)\n" + colour.end)
            customer_kl_thai_b_complete = 1
            page_customer_kl_thai_a()
        else:  # error handling
            print(colour.bold + colour.red + "[!] Invalid action, please try again." + colour.end)


# Admin actions page.
# The admin lands on this page after a successful login. This allows the admin to select which action they wish to take.
# The feature for resetting the timetables is present on this function. All the other actions are redirected to
# other functions.
def page_admin_action():
    admin_action_selected = 0
    print(colour.bold + colour.red + "=-= " + colour.white + "Admin Panel" + colour.red + " =-=" + colour.end)
    print("Which action would you like to take?")
    while admin_action_selected == 0:
        print(colour.bold + colour.cyan + "[Edit Timings: '1', Add Stations: '2', Remove stations: '3', "
                                          "Edit trip starting time: '4', Restore default settings: 'r', "
                                          "Back: 'b', Exit program: 'e']" + colour.end)
        admin_action = str(input(colour.white + "Action: " + colour.end))
        if admin_action == str('b'):
            print(colour.bold + colour.pink + "Back to role selection page.\n" + colour.end)
            admin_action_selected = 1
            page_select_role()
        elif admin_action == str(1):
            print(colour.bold + colour.pink + "Action selected: Edit Timings\n" + colour.end)
            admin_action_selected = 1
            page_admin_edit_timings()
        elif admin_action == str(2):
            print(colour.bold + colour.pink + "Action selected: Add Stations\n" + colour.end)
            admin_action_selected = 1
            page_admin_add_station()
        elif admin_action == str(3):
            print(colour.bold + colour.pink + "Action selected: Remove Stations\n" + colour.end)
            admin_action_selected = 1
            page_admin_remove_station()
        elif admin_action == str(4):
            print(colour.bold + colour.pink + "Action selected: Edit trip starting time.\n" + colour.end)
            admin_action_selected = 1
            page_edit_trip_starting_time()
        elif admin_action == str('r'):
            admin_action_selected = 1
            print(colour.bold + colour.red + "Are you sure you want to restore to default settings?" + colour.end)
            reset_confirmation = str(input(colour.bold + colour.white + "Type out 'YES' to confirm: "))
            if reset_confirmation == str('YES'):  # double confirmation to make sure the user is fully agreeable
                print(colour.bold + colour.pink + "Action selected: Restore default settings." + colour.end)
                default_a_stations = ['Kuala Lumpur', 'Butterworth', 'Kedah', 'Perlis', 'Thailand']
                with open("a_stations.txt", "w") as restore_a_stations:  # these write the default values into the files
                    for station in default_a_stations:
                        restore_a_stations.write("%s\n" % station)
                restore_a_stations.close()
                default_b_stations = ['Kuala Lumpur', 'Terengganu', 'Kelantan', 'Thailand']
                with open("b_stations.txt", "w") as restore_b_stations:
                    for station in default_b_stations:
                        restore_b_stations.write("%s\n" % station)
                restore_b_stations.close()
                default_c_stations = ['Kuala Lumpur', 'Johore', 'Singapore']
                with open("c_stations.txt", "w") as restore_c_stations:
                    for station in default_c_stations:
                        restore_c_stations.write("%s\n" % station)
                restore_c_stations.close()
                default_a_timings = [45, 240, 10, 60, 10, 45, 30, 15, 20]
                with open("a_timings.txt", "w") as restore_a_timings:
                    for timings in default_a_timings:
                        restore_a_timings.write("%s\n" % timings)
                restore_a_timings.close()
                default_b_timings = [45, 285, 10, 90, 30, 45, 20]
                with open("b_timings.txt", "w") as restore_b_timings:
                    for timings in default_b_timings:
                        restore_b_timings.write("%s\n" % timings)
                restore_b_timings.close()
                default_c_timings = [45, 270, 30, 30, 20]
                with open("c_timings.txt", "w") as restore_c_timings:
                    for timings in default_c_timings:
                        restore_c_timings.write("%s\n" % timings)
                restore_c_timings.close()
                default_start_timings = [5, 15, 12, 15, 7, 15, 0, 15, 4, 15, 6, 15, 8, 15, 12, 15]
                with open("start_timings.txt", "w") as restore_start_timings:
                    for timings in default_start_timings:
                        restore_start_timings.write("%s\n" % timings)
                restore_start_timings.close()
                print(colour.bold + colour.green + "Default settings restored.\n" + colour.end)
                print(colour.bold + colour.red + "Program must be restarted.\n" + colour.end)
                input()
            else:
                print(colour.bold + colour.red + "Settings reset cancelled.\n" + colour.end)
                page_admin_action()
        elif admin_action == str('e'):
            print(colour.bold + colour.green + " -=- Logout Successful -=- " + colour.end)
            admin_action_selected = 1
            input()
        else:  # error handling
            print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)


# Admin edit timings page.
# These functions allow the admin to edit the travel time, stopover time, and turnaround time of the stations.
# The edits are made on an individual basis and will not affect other timings.
def page_admin_edit_timings():
    print(colour.bold + colour.yellow + "-=- " + colour.white + "Edit Timings" + colour.yellow + " -=-" + colour.end)
    admin_edit_timings_complete = 0
    print(colour.end + "Please select the route of which the timings you wish to edit:")
    while admin_edit_timings_complete == 0:
        print(colour.bold + colour.cyan + "KL-Thai via Butterworth (Route A): '1'\nKL-Thai via Kelantan (Route B): '2'"
                                          "\nKL-SG (Route C): '3'\n[Back: 'b', Exit program: 'e']" + colour.end)
        admin_edit_timings_selection = str(input(colour.white + "Action: " + colour.end))
        if admin_edit_timings_selection == str('b'):
            print(colour.bold + colour.pink + "Back to admin panel page.\n" + colour.end)
            admin_edit_timings_complete = 1
            page_admin_action()
        elif admin_edit_timings_selection == str('e'):
            print(colour.bold + colour.green + " -=- Logout Successful -=- " + colour.end)
            admin_edit_timings_complete = 1
            input()
        elif admin_edit_timings_selection == str('1'):
            print(colour.bold + colour.pink + "Route A selected.\n" + colour.end)
            admin_edit_timings_complete = 1
            page_edit_timings(a_station_content_list, a_timings_content_list, "a_timings.txt")
        elif admin_edit_timings_selection == str('2'):
            print(colour.bold + colour.pink + "Route B selected.\n" + colour.end)
            admin_edit_timings_complete = 1
            page_edit_timings(b_station_content_list, b_timings_content_list, "b_timings.txt")
        elif admin_edit_timings_selection == str('3'):
            print(colour.bold + colour.pink + "Route C selected.\n" + colour.end)
            admin_edit_timings_complete = 1
            page_edit_timings(c_station_content_list, c_timings_content_list, "c_timings.txt")
        else:  # error handling
            print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)


# Admin edits timings function
# This function is responsible for editing all the timings in the program.
def page_edit_timings(a, b, c):
    print(colour.bold + colour.yellow + "-=- " + colour.white + "Edit Timings" + colour.yellow + " -=-"
          + colour.end)
    edit_timings_intervals = []
    count = 0
    for i in range(len(a) - 1):  # creating a timings table
        edit_timings_intervals.append(a[i])
        count = count + 1
        station_append = a[i] + " to " + a[count]
        edit_timings_intervals.append(station_append)
    edit_timings_intervals.append(a[-1])
    count = 0
    print(colour.bold + "Index\t", f"{'Intervals':35s} {'Timings (In minutes)'}" + colour.white)
    for i in range(len(edit_timings_intervals)):  # printing timings table
        count = count + 1
        print(count, "\t\t", f"{edit_timings_intervals[i]:35s} {b[i]}")
    print(colour.end + "Please select the interval to edit.")
    edit_timings_completed = 0
    while edit_timings_completed == 0:
        print(colour.bold + colour.cyan + "[Select Interval: 'Index Number', Back: 'b', Exit program: 'e']"
              + colour.end)
        edit_timings_select = input(colour.white + "Action: " + colour.end)
        if edit_timings_select == str('b'):
            print(colour.bold + colour.pink + "Back to timing edits page.\n" + colour.end)
            edit_timings_completed = 1
            page_admin_edit_timings()
        elif edit_timings_select == str('e'):
            print(colour.bold + colour.green + " -=- Logout Successful -=- " + colour.end)
            edit_timings_completed = 1
            input()
        elif edit_timings_select.isnumeric() and count >= int(edit_timings_select) > 0:
            new_timings = str(input(colour.white + "New timing (in minutes): " + colour.end))
            if new_timings.isnumeric():  # if new timing is an integer, it will accept the new value
                b[int(edit_timings_select) - 1] = new_timings
                with open(c, "w") as edit_timings:
                    for timings in b:
                        edit_timings.write("%s\n" % timings)
                edit_timings.close()
                print(colour.bold + colour.green + "Changes saved." + colour.end)
            else:  # error handling
                print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)
        else:
            print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)


# Admin add stations page.
# These functions allow the admin to add a station in between existing stations. Once a station is added and the timings
# inputted, the existing travelling duration between the 2 existing stations will also change to fit the total travel
# duration.
def page_admin_add_station():
    print(colour.bold + colour.yellow + "-=- " + colour.white + "Add Stations" + colour.yellow
          + " -=-" + colour.end)
    admin_add_station_complete = 0
    while admin_add_station_complete == 0:
        print(colour.bold + colour.cyan + "KL-Thai via Butterworth (Route A): '1'\nKL-Thai via Kelantan (Route B): '2'"
                                          "\nKL-SG (Route C): '3'\n[Back: 'b', Exit program: 'e']" + colour.end)
        admin_edit_station_selection = str(input(colour.white + "Action: " + colour.end))
        if admin_edit_station_selection == str('b'):
            print(colour.bold + colour.pink + "Back to admin panel page.\n" + colour.end)
            admin_add_station_complete = 1
            page_admin_action()
        elif admin_edit_station_selection == str('e'):
            print(colour.bold + colour.green + " -=- Logout Successful -=- " + colour.end)
            admin_add_station_complete = 1
            input()
        elif admin_edit_station_selection == str(1):
            print(colour.bold + colour.pink + "Route A selected.\n" + colour.end)
            admin_add_station_complete = 1
            page_add_station(a_station_content_list, a_timings_content_list, "a_stations.txt", "a_timings.txt")
        elif admin_edit_station_selection == str(2):
            print(colour.bold + colour.pink + "Route B selected.\n" + colour.end)
            admin_add_station_complete = 1
            page_add_station(b_station_content_list, b_timings_content_list, "b_stations.txt", "b_timings.txt")
        elif admin_edit_station_selection == str(3):
            print(colour.bold + colour.pink + "Route C selected.\n" + colour.end)
            admin_add_station_complete = 1
            page_add_station(c_station_content_list, c_timings_content_list, "c_stations.txt", "c_timings.txt")
        else:  # error handling
            print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)


# Admin add station function.
# This function is responsible for the add station function of the program.
def page_add_station(a, b, c, d):
    print(colour.bold + colour.yellow + "-=- " + colour.white + "Add Stations" + colour.yellow + " -=-"
          + colour.end)
    count = 1
    print(colour.bold + "Index\t", f"{'Stations':35s}" + colour.white)
    for i in range(len(a) - 1):
        print(count, "\t\t", a[i])
        count = count + 1
    print("Please select the station after which the new station will be placed.")
    admin_add_station_complete = 0
    while admin_add_station_complete == 0:
        print(colour.bold + colour.cyan + "[Select Interval: 'Index Number', Back: 'b', Exit program: 'e']"
              + colour.end)
        add_select = input(colour.white + "Action: " + colour.end)
        if add_select == str('b'):
            print(colour.bold + colour.pink + "Back to add stations page.\n" + colour.end)
            admin_add_station_complete = 1
            page_admin_add_station()
        elif add_select == str('e'):
            print(colour.bold + colour.green + " -=- Logout Successful -=- " + colour.end)
            admin_add_station_complete = 1
            input()
        elif add_select.isnumeric() and 0 < int(add_select) <= count - 1:
            new_station = str(input(colour.white + "New Station Name: " + colour.end))
            print("Please set the travel duration from previous station to the new station. Max:",
                  b[(int(add_select)) * 2 - 1])
            new_station_travel_duration = input(colour.white + "Time in minutes: " + colour.end)
            if new_station_travel_duration.isnumeric() and new_station_travel_duration <= \
                    b[(int(add_select)) * 2 - 1]:
                print("Please set the stopover time at the new station.")
                new_station_stopover = input(colour.white + "Time in minutes: " + colour.end)
                if new_station_stopover.isnumeric():  # if the input timings is in integer, it will accept the value
                    a.insert(int(add_select), new_station)  # insert new station name
                    b.insert((int(add_select) * 2) - 1, new_station_travel_duration)  # insert travel time
                    b.insert((int(add_select) * 2), new_station_stopover)  # insert stopover time
                    b[(int(add_select) * 2) + 1] = int(b[(int(add_select)*2)+1]) - int(new_station_travel_duration)
                    with open(c, "w") as edit_stations:  # write the changes into the files
                        for stations in a:
                            edit_stations.write("%s\n" % stations)
                    edit_stations.close()
                    with open(d, "w") as edit_timings:
                        for timings in b:
                            edit_timings.write("%s\n" % timings)
                    edit_timings.close()
                    print(colour.bold + colour.green + "Changes saved\n." + colour.end)
                    admin_add_station_complete = 1
                    page_admin_add_station()
                else:  # error handling
                    print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)
            else:
                print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)
        else:
            print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)


# Admin remove stations page.
# These functions allow the admin to remove existing stations.
# Once a station is removed , the existing travelling duration between the adjacent 2 existing stations will also
# change to fit the total travel duration.
def page_admin_remove_station():
    print(colour.bold + colour.yellow + "-=- " + colour.white + "Remove Stations" + colour.yellow
          + " -=-" + colour.end)
    admin_remove_station_complete = 0
    while admin_remove_station_complete == 0:
        print(colour.bold + colour.cyan + "KL-Thai via Butterworth (Route A): '1'\nKL-Thai via Kelantan (Route B): '2'"
                                          "\nKL-SG (Route C): '3'\n[Back: 'b', Exit program: 'e']" + colour.end)
        admin_edit_station_selection = str(input(colour.white + "Action: " + colour.end))
        if admin_edit_station_selection == str('b'):
            print(colour.bold + colour.pink + "Back to admin panel page.\n" + colour.end)
            admin_remove_station_complete = 1
            page_admin_action()
        elif admin_edit_station_selection == str('e'):
            print(colour.bold + colour.green + " -=- Logout Successful -=- " + colour.end)
            admin_remove_station_complete = 1
            input()
        elif admin_edit_station_selection == str(1):
            print(colour.bold + colour.pink + "Route A selected.\n" + colour.end)
            admin_remove_station_complete = 1
            page_remove_station(a_station_content_list, a_timings_content_list, "a_stations.txt", "a_timings.txt")
        elif admin_edit_station_selection == str(2):
            print(colour.bold + colour.pink + "Route B selected.\n" + colour.end)
            admin_remove_station_complete = 1
            page_remove_station(b_station_content_list, b_timings_content_list, "b_stations.txt", "b_timings.txt")
        elif admin_edit_station_selection == str(3):
            print(colour.bold + colour.pink + "Route C selected.\n" + colour.end)
            admin_remove_station_complete = 1
            page_remove_station(c_station_content_list, c_timings_content_list, "c_stations.txt", "c_timings.txt")
        else:  # error handling
            print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)


# Admin remove station function.
# This function is responsible for removing stations in the program.
def page_remove_station(a, b, c, d):
    print(colour.bold + colour.yellow + "-=- " + colour.white + "Remove Stations" + colour.yellow + " -=-"
          + colour.end)
    count = 1
    print(colour.bold + "Index\t", f"{'Stations':35s}" + colour.white)
    for i in range(len(a)):
        print(count, "\t\t", a[i])
        count = count + 1
    print("Please select the station that you wish to remove.")
    admin_remove_station_complete = 0
    while admin_remove_station_complete == 0:
        print(colour.bold + colour.cyan + "[Select Station: 'Index Number', Back: 'b', Exit program: 'e']"
              + colour.end)
        remove_select = input(colour.white + "Action: " + colour.end)
        if remove_select == str('b'):
            print(colour.bold + colour.pink + "Back to remove stations page.\n" + colour.end)
            admin_remove_station_complete = 1
            page_admin_remove_station()
        elif remove_select == str('e'):
            print(colour.bold + colour.green + " -=- Logout Successful -=- " + colour.end)
            admin_remove_station_complete = 1
            input()
        elif remove_select.isnumeric() and 1 < int(remove_select) <= count - 2:
            a.pop(int(remove_select) - 1)  # remove station from list
            b.pop((int(remove_select) * 2) - 2)  # remove its timing from list
            b[(int(remove_select) * 2) - 3] = int(b[(int(remove_select)*2)-2]) + int(b[(int(remove_select)*2)-3])
            b.pop((int(remove_select) * 2) - 2)  # adjusting travel duration between the 2 stations
            with open(c, "w") as edit_stations:  # write changes into files
                for stations in a:
                    edit_stations.write("%s\n" % stations)
            edit_stations.close()
            with open(d, "w") as edit_timings:
                for timings in b:
                    edit_timings.write("%s\n" % timings)
            edit_timings.close()
            print(colour.bold + colour.green + "Changes saved.\n" + colour.end)
            admin_remove_station_complete = 1
            page_admin_remove_station()
        elif int(remove_select) == 1:  # the first station cannot be removed
            print(colour.bold + colour.red + "[!] Cannot remove hub station, please try again." + colour.end)
        elif int(remove_select) == count - 1:  # the last station cannot be removed
            print(colour.bold + colour.red + "[!] Cannot remove terminus station, please try again." + colour.end)
        else:  # error handling
            print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)


# Edit trip starting time page.
# This function allows the admin to change the starting time of the trains. Note that these timings does not include
# the stopover time of the departure station which is included in the final timings.
def page_edit_trip_starting_time():
    print(colour.bold + colour.yellow + "-=- " + colour.white + "Edit Trip Starting Times" + colour.yellow + " -=-"
          + colour.end)
    start_time_1 = str(start_time_list[0]).zfill(2) + ":" + str(start_time_list[1]).zfill(2)  # compile time
    start_time_2 = str(start_time_list[2]).zfill(2) + ":" + str(start_time_list[3]).zfill(2)
    start_time_3 = str(start_time_list[4]).zfill(2) + ":" + str(start_time_list[5]).zfill(2)
    start_time_4 = str(start_time_list[6]).zfill(2) + ":" + str(start_time_list[7]).zfill(2)
    start_time_5 = str(start_time_list[8]).zfill(2) + ":" + str(start_time_list[9]).zfill(2)
    start_time_6 = str(start_time_list[10]).zfill(2) + ":" + str(start_time_list[11]).zfill(2)
    start_time_7 = str(start_time_list[12]).zfill(2) + ":" + str(start_time_list[13]).zfill(2)
    start_time_8 = str(start_time_list[14]).zfill(2) + ":" + str(start_time_list[15]).zfill(2)
    print(colour.bold + "Index\t", f"{'Trains':35s} {'Starting Time'}" + colour.white)
    print("1\t\t", f"{'KL-Thai Route A Train 1':35s} {start_time_1}")  # print time
    print("2\t\t", f"{'KL-Thai Route A Train 2':35s} {start_time_2}")
    print("3\t\t", f"{'KL-Thai Route B Train 1':35s} {start_time_3}")
    print("4\t\t", f"{'KL-SG Route C Train 1':35s} {start_time_4}")
    print("5\t\t", f"{'KL-SG Route C Train 2':35s} {start_time_5}")
    print("6\t\t", f"{'KL-SG Route C Train 3':35s} {start_time_6}")
    print("7\t\t", f"{'KL-SG Route C Train 4':35s} {start_time_7}")
    print("8\t\t", f"{'KL-SG Route C Train 5':35s} {start_time_8}" + colour.end)
    print("Note that the actual start time accounts for the starting station's stopover time.")
    trip_start_time_complete = 0
    while trip_start_time_complete == 0:
        print(colour.bold + colour.cyan + "[Edit start time: 'Index Number', Back: 'b', Exit program: 'e']"
              + colour.end)
        trip_start_time_selection = input(colour.white + "Action: " + colour.end)
        if trip_start_time_selection == str('b'):
            print(colour.bold + colour.pink + "Back to timing edits page.\n" + colour.end)
            trip_start_time_complete = 1
            page_admin_action()
        elif trip_start_time_selection == str('e'):
            print(colour.bold + colour.green + " -=- Logout Successful -=- " + colour.end)
            trip_start_time_complete = 1
            input()
        elif trip_start_time_selection.isnumeric() and 0 < int(trip_start_time_selection) <= 8:
            print("Please enter the new starting time.")
            new_start_hour = input("Start hour: ")
            if new_start_hour.isnumeric() and 0 <= int(new_start_hour) < 24:  # if input is numeric, it will accept.
                new_start_min = input("Start minute: ")
                if new_start_min.isnumeric() and 0 <= int(new_start_min) < 60:
                    start_time_list[int(trip_start_time_selection) * 2 - 1] = new_start_min
                    start_time_list[int(trip_start_time_selection) * 2 - 2] = new_start_hour
                    with open("start_timings.txt", "w") as edit_start_timings:  # write changes into file
                        for timings in start_time_list:
                            edit_start_timings.write("%s\n" % timings)
                    edit_start_timings.close()
                    trip_start_time_complete = 1
                    print(colour.bold + colour.green + "Changes saved." + colour.end)
                    page_edit_trip_starting_time()
                else:  # error handling
                    print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)
            else:
                print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)
        else:
            print(colour.bold + colour.red + "[!] Invalid selection, please try again." + colour.end)


# Start of program.
# This initiates the first function which kickstart the program. The rest of the program is run from function to
# function in a menu-driven system.
page_select_role()
