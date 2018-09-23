import requests
import json

class FitbitApi:

    def __init__(self, userid, auth_tok):
        self.fitbit_url = "https://api.fitbit.com/1.2/user/{}/{}"
        self.userid = userid
        self.header = {"Authorization": "Bearer " + auth_tok}

    def get_sleep_by_date_range(self, startdate, enddate):
        urlend = "sleep/date/{}/{}.json".format(startdate, enddate)
        r = requests.get(self.fitbit_url.format(self.userid, urlend), headers=self.header)
        return r.json()

    def get_exercise_by_date(self, date):
        urlend = "activities/date/{}.json".format(date)
        r = requests.get(self.fitbit_url.format(self.userid, urlend), headers=self.header)
        return r.json()

    def get_avg_hearRate_by_date_range(self, startdate, enddate):
        urlend = "activities/heart/date/{}/{}.json".format(startdate, enddate)
        r = requests.get(self.fitbit_url.format(self.userid, urlend), headers=self.header)
        return r.json()

    def get_weight_by_date(self, date):
        urlend = "body/log/weight/date/{}.json".format(date)
        r = requests.get(self.fitbit_url.format(self.userid, urlend), headers=self.header)
        return r.json()
