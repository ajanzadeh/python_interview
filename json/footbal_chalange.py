# We want to be able to see how many goals a specific football team in the Premier League scored in total during the 2014/2015 season. All the information you need is contained in this JSON file https://raw.githubusercontent.com/openfootball/football.json/master/2014-15/en.1.json
#
# INPUT string teamKey ^^ the football team key name (is a parameter of the JSON)
#
# OUTPUT int goals ^^ an integer with the total number of goals scored by that team during the session
#
# EXAMPLE Input "arsenal" Output "X" ^^ number of goals scored by Arsenal in that JSON
#
# HTTP Libraries PHP: curl JavaScript: XMLHttpRequest - Example NodeJS: https - Example Python: urllib.request Ruby: net/http C#: System.Net.Http - Example Java: java.net - Example C++: curl/curl.h - Example Scala: scala.io.Source - Example Clojure: clj-http "3.8.0"
#
# JSON Libraries PHP: json_decode JavaScript: JSON.parse NodeJS: JSON.parse Python: import json Ruby: require 'json' C#: json.net 11.0.1 - Example Java: gson 2.8.2 - Example C++: jsoncpp 1.8.4 (json/json.h) - Example Scala: play.api.libs.json 2.6.x - Example Clojure: org.clojure/data.json 0.2.6


import urllib.request
import json
class Solution:
	def run(self, teamKey):
		goals = 0
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		def get_json(url):
			with urllib.request.urlopen(url) as data:
				data = data.read()
			return json.loads(data.decode())

		json_string = get_json("https://raw.githubusercontent.com/openfootball/football.json/master/2014-15/en.1.json")
		for item in json_string["rounds"]:
			#matches = item[counter]["matches"]
			for i in item["matches"]:
				if i["team1"]["key"] == teamKey :
					print(teamKey)
					goals += i["score1"]
				if i["team2"]["key"] == teamKey :
					goals += i["score2"]


		return goals
sl = Solution()
print(sl.run("arsenal"))
