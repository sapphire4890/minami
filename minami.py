import requests
import csv
import os

from array import array

"""
Author:             LAW Willson King Tin (3035443342)
Application Name:   Web Minami
Creation Date:      27/2/2018
Last Modified Date: 31/3/2018
"""

#deciding the path
dir_path = os.path.dirname(os.path.realpath('__file__'))

# Declare array, it's like vector in C++
web_array = []
webName_array = []
web_timer = []

what = raw_input("Do you need to create a new file?\n\"Y\" / \"N\"\n")

#store log file in comma separated file
#convert user input into upper case
if(what.upper() == 'Y'):
	file = open(dir_path + '/' + 'counting.csv', 'w')
else:
	file = open(dir_path + '/' + 'counting.csv', 'a')

head = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
	'cache-control':'no-cache, no-store, must-revalidate',
	'pragma': 'no-cache',
	'expires': 'Thu, 01 Jan 1970 00:00:00 GMT'
}

num_Iteration = int(input("\nPlease specify the number of websites\n"))


try:
  #iteration until the amount is match with user input
  for num_It in range(num_Iteration):
    web = raw_input("Enter the ["+ str(num_It+1) +"] website url: ")
    web_array.append(web)
    webName_array.append(web.split('/')[2])
    # Help web_timer to declare size first.
    web_timer.append(0.00)
except IndexError:
  print("Please enter a valid website URL, which have \"http://\" \"www.\" \".com\"")

attempts = 0
try:
  attempts = int(input("Enter a number of requests:\n"))

  print('-----------Line Breaker-----------\n')

  # all connection summary
  total = 0.0
except TypeError:
  print("Please enter integer, don't put it in decimal or character inside")


for n in range(num_Iteration):
  print("You are visiting \"" + webName_array[n] + "\"\n");
  file.write( str(webName_array[n]) + ",")

print('-----------Line Breaker-----------\n')

# separate line in the csv file.
file.write( "\r\n")

try:
  # how many connecting times
  for connecting_time in range(attempts):
    #for every connecting attempt, loop every web_array
    for loopArray in range(num_Iteration):
      each = float(requests.get(web_array[loopArray], headers=head, verify=True).elapsed.total_seconds())
      web_timer[loopArray] += each
      #print(str(requests.get("https://www.facebook.com/").elapsed.total_seconds())+'s')
      print( webName_array[loopArray] + "[" + str(connecting_time) +"] = "+ str(each) + 's' )
      total += float(each)
      file.write( str(each) + ',')

    print('')
    file.write("\r\n")

  #after finishing the attemps
  print('\n\n')
  file.write("\r\n")
  file.write("\r\n")

  for r_time in range(num_Iteration):
    print("\"" + str(webName_array[r_time]) + "\"\t speed = \t\"" + str(web_timer[r_time]) + "\" s\n")
    print("\"" + str(webName_array[r_time]) + "\"\t Avgerage = \t\"" + str((float(web_timer[r_time])/float(attempts))) + "\" s\n")
    file.write("Avgerage: " + str((float(web_timer[r_time])/float(attempts))) + ',')
    print('-----    -----   -----    -----    -----    -----')
except requests.exceptions.SSLError:
  print("Can't connect to some websites, which require SSL certificate. \nLike http://hku.hk")



print( "****************************************************\n")
print( "*** Total connections = " + str(num_Iteration * attempts) + ' times took ' + str(total) + 's ***\n')
print( "****************************************************\n")
#file.write( 'Total:' + str(total))

print( "Saved Automatically, please check the current folder")
print( "----------------------------------------------------" )
print( "-------Thanks for using Willson's Application-------" )
print( "----------------------------------------------------" )

file.close()
