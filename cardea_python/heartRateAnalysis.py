import fitbitapi
import datetime
from datetime import timedelta
import json

class heartRateAnalysis:

    def __init__(self, userid, auth_tok):
        self.fb = fitbitapi.FitbitApi(userid, auth_tok)

    def heartRate_and_weightLoss(self, weeks):

        heartRate = []
        weightLoss = []

        enddate = datetime.date.today()

        for week in range(weeks):

            startdate = (enddate - timedelta(days=7))
            heartRate_data = self.fb.get_avg_hearRate_by_date_range(startdate.strftime('%Y-%m-%d'), enddate.strftime('%Y-%m-%d'))
            try:
                weightLoss_data = ((self.fb.get_weight_by_date(startdate.strftime('%Y-%m-%d'))["weight"][0]["weight"]) - (self.fb.get_weight_by_date(enddate.strftime('%Y-%m-%d'))["weight"][0]["weight"]))
            except IndexError:
                weightLoss_data = 0;
            enddate = (startdate - timedelta(days=1))

            total, resting, fatBurn, cardio, peak = [0, 0, 0, 0, 0];

            for day in heartRate_data["activities-heart"]:
                for heartRate_range in day["value"]["heartRateZones"]:
                    if heartRate_range["name"] == "Out of Range":
                        resting += heartRate_range["minutes"]
                        total += heartRate_range["minutes"]
                    elif heartRate_range["name"] == "Fat Burn":
                        fatBurn += heartRate_range["minutes"]
                        total += heartRate_range["minutes"]
                    elif heartRate_range["name"] == "Cardio":
                        cardio += heartRate_range["minutes"]
                        total += heartRate_range["minutes"]
                    elif heartRate_range["name"] == "Peak":
                        peak += heartRate_range["minutes"]
                        total += heartRate_range["minutes"]

            heartRate.append([total, resting, fatBurn, cardio, peak])
            weightLoss.append(weightLoss_data)

        return heartRate, weightLoss
