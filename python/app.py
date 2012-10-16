import os
import json
import urllib
import urllib2
import pygeoip

# Get external IP address
ipaddr = urllib2.urlopen("http://icanhazip.com").read()

# Load GeoIP City database
gi = pygeoip.GeoIP(os.path.join(os.path.dirname(__file__), 'GeoLiteCity.dat'))

# Query GeoIP City database with received ipaddr
record = gi.record_by_addr(ipaddr)
city   = urllib.quote_plus(record["city"])
region = urllib.quote_plus(record["region_name"])

# Query Wunderground API
key = '9c63b3e80a883645'
url = "http://api.wunderground.com/api/" + key + "/conditions/q/" + region + "/" + city + ".json"
response = json.load(urllib2.urlopen(url))

print "The temperature in " + city.replace("+", " ") + ", " + region.replace("+", " ") + " is " + response["current_observation"]["temp_f"].__str__()
