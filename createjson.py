from tkinter.messagebox import NO, YES
import requests
import json

def catch_cases(country):
    url =("https://api.covid19api.com/total/dayone/country/"+country+"/status/confirmed")
    response = requests.get(url)
    json_data = response.json()
    cases = json_data[504]['Cases']
    catch_active(country,cases)

def catch_active(country,cases):
    url =("https://api.covid19api.com/live/country/"+country)
    response = requests.get(url)
    json_data = response.json()
    active = json_data[18]['Active']
    trend = trend_seven_days(json_data[18]['Active'],json_data[17]['Active'],json_data[11]['Active'],json_data[10]['Active'])
    lockdown = calculate_lockdown(json_data[18]['Active'])
    dictionary ={
        "cases" : cases,
        "active": active,
        "trend": trend,
        "lockdown": lockdown
    } 
    with open ('rawdata.json', 'w') as f:
        json.dump(dictionary,f)
def trend_seven_days(day1,day2,day7,day8):
    average_present=day1-day7
    average_past=day2-day8
    if average_present > average_past:
        trend = "down"
    else: 
        trend = "up"
    return trend
def calculate_lockdown(active):
    if active > 10000:
        lockdown = YES
    else:
        lockdown = NO
    return lockdown

