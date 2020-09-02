# import requests
# import json
#
# url = 'https://api.themoviedb.org/3/person/1221114?api_key=&language=en-US'
#
# rawdata = requests.get(url)
# rawdra_text =
# json_raw = json.loads(rawdata)
# print(json_raw['birthday'])
#

# Python program to illustrate
# function with main
def getInteger():
	result = int(input("Enter integer: "))
	return result

def Main():
	print("Started")

	# calling the getInteger function and
	# storing its returned value in the output variable
	output = getInteger()
	print(output)

# now we are required to tell Python
# for 'Main' function existence
if __name__=="__main__":
	Main()
