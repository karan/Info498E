import csv
from collections import defaultdict
import time

hours = defaultdict(int)

hours_list = []

def getHour(string):
  # Sat May 17 05:59:52 +0000 2014
  return time.strptime(string, "%a %b %d %H:%M:%S +0000 2014").tm_hour


with open('positive-tweets.csv', 'rU') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    hours[getHour(row[0])] = hours[getHour(row[0])] + 1
    hours_list.append(getHour(row[0]))

print hours
