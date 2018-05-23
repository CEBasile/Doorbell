#!/usr/bin/env python
import requests, time

message = {'date': time.asctime().split()}  # strftime("%l:%M %p on %d.%m.%Y")
print(message)
r = requests.post('https://hooks.zapier.com/hooks/catch/3260910/fnmj4n/silent/', data=message)
print (r.status_code)
