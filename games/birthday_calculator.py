#
# Wouldn't it be neat if every year, your birthday would fall on a Friday, Saturday or Sunday? Given a certain date, return a string with the day of the week and the year it will fall in a weekend, starting with the year (2016). Do this for 50 years in the future.
#
# INPUT string date_of_birth ^ with this format: dd-mm
#
# OUTPUT string future_dates ^ wday-yyyy wday-yyyy … (where wday can be any of this three values: Fry, Sat, Sun) Every date should be separated by one space
#
# EXAMPLE Input "23-10"
#
# Output "Sun-2016 Fri-2020 Sat-2021 Sun-2022 Fri-2026 Sat-2027 Sat-2032 Sun-2033 Fri-2037 Sat-2038 Sun-2039 Fri-2043 Sun-2044 Fri-2048 Sat-2049 Sun-2050 Fri-2054 Sat-2055 Sat-2060 Sun-2061 Fri-2065"


class Solution:

	def run(birthday_date):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		future_dates_list = []
		days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ] 	# 01-01-2016 Friday.
		months_dic_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		date = int(birthday_date[:2])
		month = int(birthday_date[3:5])
		number_of_days_from_start = 0
		y_index = 0

		def day(date, month):
			number_of_days_from_start = 0
			if month > 1:
				for i in range(0, month -1):
					 number_of_days_from_start += months_dic_leap[i]+date -1

			else:
				number_of_days_from_start = date -1

			d_index = (number_of_days_from_start % 7) -3
			day_of_week_2016 = days[d_index]
			return d_index

		print(day(1,4))

		for i in range(2016,2066):
			day_index = day(date,month)
			if i % 4 == 0:
				future_dates_list +=[days[y_index %7 + day_index ]+"-"+str(i)]
				y_index += 2
			else:
				future_dates_list +=[days[y_index %7 + day_index ]+"-"+str(i)]

				y_index += 1
		future_dates_list = " ".join(map(str,future_dates_list))
		return future_dates_list

print(Solution.run("01-01"))
