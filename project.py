import requests,json

def main_function()
	done = ""
	while(done != 'q'):
		user_input = input("Enter your zip code or city:")
		result = conn_weatherapi(user_input)
		formatoutput(result, user_input)
		done = input"Enter q to quit the program or enter anything else to continue:")


def conn_weatherapi(user_input):
	key = "93e587b9a34ee4e1dc45a4aeb0c69f49"
	url = "http://api.openweathermap.org/data/2.5/weather?"
	invoke_url = url+"q="+user_input+"&appid="+key
	r = requests.get(invoke_url)
	return r

def formatoutput(result, user_input)
	format = result["main"]
	temp = convertktof(format['temp'])	
	humidity = format['humidity']
	print(temp + " F")
	print(humidity + " Humidity")
	format2 = result["wind"]
	speed = format2['speed']
	print(speed + " Wind Speed (mph)")  

def convertktof(kelvin)
	return 1.8*(kelvin - 273)+32import requests,json


main_function()
