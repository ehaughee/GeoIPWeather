require 'geoip'
require 'json'
require 'curb'
require 'socket'

key = '9c63b3e80a883645'
ipaddr = Curl::Easy.perform("http://icanhazip.com").body_str
c = GeoIP.new(File.expand_path("./GeoLiteCity.dat")).city(ipaddr)
region = c.region_name
city   = c.city_name.gsub(' ', '_')

url = "http://api.wunderground.com/api/#{key}/conditions/q/#{region}/#{city}.json"
#puts url
response = Curl::Easy.perform(url).body_str
response = JSON.parse(response)
puts "The temperature in #{city}, #{region} is #{response["current_observation"]["temp_f"]}"

