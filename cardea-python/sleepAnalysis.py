import fitbitapi

class SleepAnalysis:

    def __init__(self, userid, auth_tok):
        self.fb = FitbitApi(userid, auth_tok)

    def sleep_and_exercise(startdate, enddate):
        sleep_with_exercise = []
        sleep_without_exercise = []

        sleep_data = self.fb.get_sleep_by_date_range(startdate, enddate)
        for night_of_sleep in sleep_data["sleep"]:
            if night_of_sleep["isMainSleep"]:
                exercise_data = self.fb.get_exercise_by_date(sleep_data["dateOfSleep"])
                if len(exercise_data["activities"]) > 1:
                    sleep_with_exercise.append(sleep_data["minutesAsleep"])
                else:
                    sleep_without_exercise.append(sleep_data["minutesAsleep"])

        avg_sleep_build = "You get an average night sleep of {} hours."
        avg_sleep_without = sum(sleep_without_exercise)/len(sleep_without_exercise)
        avg_sleep_with = sum(sleep_with_exercise)/len(sleep_with_exercise)

        if not sleep_with_exercise:
            return avg_sleep_build.format(int(avg_sleep_without/60)) +
                    "You could sleep longer if you exercised."
        elif not sleep_without_exercise:
            return avg_sleep_build.format(int(avg_sleep_with/60)) +
                    "You always exercise so you must sleep well :)"
        else:
            avg_both = (avg_sleep_without+avg_sleep_with)/2
            if avg_sleep_with > avg_sleep_without
                return avg_sleep_build.format(int(avg_both/60)) +
                    "When you exercise you tend to get" +
                    "{} more minutes of sleep".format(avg_sleep_with-avg_sleep_without)
            else:
                return ""
