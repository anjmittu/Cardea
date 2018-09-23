import requests
import json

class FitbitApi:
    fitbit_url = "https://api.fitbit.com/1.2/user/{}/{}"

    def get_sleep_by_date_range(userid, startdate, enddate):
        urlend = "sleep/date/{}/{}.json".format(startdate, enddate)
        r = requests.get(fitbit_url.format(userid, urlend))
        return r.json()

    def get_exercise_by_date(userid, date):
        urlend = "activities/date/{}.json".format(date)
        r = requests.get(fitbit_url.format(userid, urlend))
        return r.json()
