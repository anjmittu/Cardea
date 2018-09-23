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

        # Today's data should be the end date
        enddate = datetime.date.today()

        for week in range(weeks):
            # Get the start day of the week
            startdate = (enddate - timedelta(days=7))
            # Get fitbit heart rate data for ht week
            heartRate_data = self.fb.get_avg_hearRate_by_date_range(startdate.strftime('%Y-%m-%d'), enddate.strftime('%Y-%m-%d'))
            # Try to get the weight lost for that week
            weightLoss_data = self.fb.get_weight_by_date_range(startdate.strftime('%Y-%m-%d'), enddate.strftime('%Y-%m-%d'))
            if weightLoss_data["weight"]:
                start_weight = weightLoss_data["weight"][0]["weight"]
                end_weight = weightLoss_data["weight"][len(weightLoss_data["weight"])-1]["weight"]
                weightLoss_data = start_weight - end_weight
            else:
                weightLoss_data = 0

            enddate = (startdate - timedelta(days=1))

            total, resting, fatBurn, cardio, peak = [0, 0, 0, 0, 0];

            # Tally up the different heartrate zones per the week
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
