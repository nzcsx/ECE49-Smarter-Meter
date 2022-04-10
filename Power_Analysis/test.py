import Power_Analysis.db_login as login
import Power_Analysis.db_search as search
import Power_Analysis.db_update as update
import Power_Analysis.analysis as anal
from datetime import datetime

now = datetime.now()
client, db, tab = login.connect_host("Power", "user_info")
login.remove_collection(db["user_1"])
login.remove_collection(db["user_2"])
login.remove_collection(tab)

# dd-mm-YY H:M:S
now = datetime.now()
dt_string = now.strftime("%b-%d-%Y %H:%M:%S")
print("date and time =", dt_string)

# format: [[appliance, wattage, quantity, usage frequency],...] -> [[string, int/float, int, string],...]
        # usage frequency choices: "all day", "often", "rare", "not in use"
user_info = {
# need to add more information here
        "id": 1,
        "name": "Lee",
        "size": "3",
        "readings": {"1": "102555"}, # readings should be in a dictionary form with {t_id: reading}
        "date": {"1": "Dec-29-2021 17:13:24"},  # date should be in a dictionary form with {t_id:date}
        "appliance": [["fridge", 362, 3, "often"]],
        "password": "yes",
        "reset_Q": "My name?",
        "reset_A": "Default"
}
login.add_user(db, db["user_info"], user_info)
search.print_collection(tab)

# test 1
update.update_appliance_info(db, tab,1,[["fridge", 362, 3, "often"], ["laptop", 36, 1, "rare"]])
search.print_collection(tab)

# test 2
# dd-mm-YY H:M:S
update.add_power_reading(tab,1,readings = ["103555"],dates = ["Dec-31-2021 17:45:24"])
search.print_collection(tab)

# dd-mm-YY H:M:S
update.add_power_reading(tab,1,readings = ["104555"],dates = ["Jan-01-2022 19:13:24"])
search.print_collection(tab)

# dd-mm-YY H:M:S
update.add_power_reading(tab,1,readings = ["104888"],dates = ["Jan-03-2022 07:13:24"])
search.print_collection(tab)

# dd-mm-YY H:M:S
update.add_power_reading(tab,1,readings = ["105999"],dates = ["Jan-05-2022 15:23:45"])
search.print_collection(tab)

# dd-mm-YY H:M:S
update.add_power_reading(tab,1,readings = ["108555"],dates = ["Jan-10-2022 12:13:24"])
search.print_collection(tab)

# dd-mm-YY H:M:S
update.add_power_reading(tab,1,readings = ["112444"],dates = ["Jan-12-2022 22:13:24"])
search.print_collection(tab)

# dd-mm-YY H:M:S
update.add_power_reading(tab,1,readings = ["114544"],dates = ["Jan-12-2022 23:13:24"])
search.print_collection(tab)

update.add_power_reading(tab,1,readings = ["114550"],dates = ["Jan-13-2022 12:13:24"])
search.print_collection(tab)
# dd-mm-YY H:M:S
update.add_power_reading(tab,1,readings = ["118770"],dates = ["Jan-13-2022 22:13:24"])
search.print_collection(tab)

update.fetch_power_data(tab, 1, "1s1lpZeqlldYExhBcNcVJrDK6zZDvThCg")
search.print_collection(tab)

# # dd-mm-YY H:M:S
now = datetime.now()
dt_string = now.strftime("%b-%d-%Y %H:%M:%S")
print("date and time =", dt_string)
update.add_power_reading(tab,1,readings = ["125333"],dates = [dt_string])
search.print_collection(tab)

update.add_power_reading(tab,1,readings = ["128222"],dates = ["Apr-13-2022 12:13:24"])
search.print_collection(tab)
#
# test 3
p,d = search.search_power_reading_date(tab, 1, min_date = 'Dec-29-2021 18:50:12', max_date = "Dec-31-2021 18:14:00")
print("result is", p,d)
update.update_last_login(tab, 1)
anal.plot_temporal(tab, 1, min_date = 'Dec-29-2021 12:50:12', max_date = "Jan-15-2022 20:14:00")
#
# # test 4
# p,d = search.search_power_interval(tab, 1, 120, 130)
# print(p,d)
#
# # test 5
# user_info = {
# # need to add more information here
#         "id": login.get_new_id(tab),
#         "name": "Someone",
#         "size": "3",
#         "readings": {"1": "123"}, # readings should be in a dictionary form with {t_id: reading}
#         "date": {"1": "Dec-29-2021 19:20:21"},  # date should be in a dictionary form with {t_id:date}
#         "appliance": [["fridge", 362, 3, "often"]],
#         "password": "yes",
#         "reset_Q": "My name?",
#         "reset_A": "Default"
# }
# login.add_user(db, tab, user_info)
# search.print_collection(tab)
#
# print("after deletion")
# login.remove_user(db, tab,2)
# search.print_collection(tab)
#
# search.print_user_info(db, tab,1)
#
# print(login.get_id_by_name(tab, 'Default'))
# login.reset_pwd(tab, 1, "Default", "No")
# update.update_last_login(tab, 1)
# print(search.search_last_update(tab, 1))
# search.print_collection(tab)

login.remove_user(db, tab,1)
login.remove_collection(tab)
login.remove_connection(client)

# dates = []
# dates.append('Apr-1-2005')
# dates.append('Aug-28-2007')
# from datetime import datetime
# for d in dates:
#      date = datetime.strptime(d, '"%b-%m-%Y %H:%M:%S"')
#      print (type(date))
#      print (date)
#
# print(datetime.strptime(dates[0], '%b-%d-%Y')<datetime.strptime(dates[1], '%b-%d-%Y'))
# now = datetime.now()
# dt_string = now.strftime("%b-%d-%Y %H:%M:%S")
# date = datetime.strptime(dt_string, "%b-%d-%Y %H:%M:%S")
# print(date)