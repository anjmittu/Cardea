import cardea_python.fitbitapi as fitbitapi

class SleepAnalysis:

    def __init__(self, userid, auth_tok):
        self.fb = fitbitapi.FitbitApi(userid, auth_tok)

    def sleep_and_exercise(self, startdate, enddate):
        sleep_with_exercise = []
        sleep_without_exercise = []

        sleep_data = self.fb.get_sleep_by_date_range(startdate, enddate)
        for night_of_sleep in sleep_data["sleep"]:
            exercise_data = self.fb.get_exercise_by_date(night_of_sleep["dateOfSleep"])
            if len(exercise_data["activities"]) >= 1:
                sleep_with_exercise.append(night_of_sleep["minutesAsleep"])
            else:
                sleep_without_exercise.append(night_of_sleep["minutesAsleep"])

        avg_sleep_build = "You get an average night sleep of {} hours and {} minutes. "
        avg_sleep_without = sum(sleep_without_exercise)/len(sleep_without_exercise)
        avg_sleep_with = sum(sleep_with_exercise)/len(sleep_with_exercise)
        avg_sleep_without_hours, avg_sleep_without_minutes = divmod(avg_sleep_without, 60)
        avg_sleep_with_hours, avg_sleep_with_minutes = divmod(avg_sleep_with, 60)

        if not sleep_with_exercise:
            return avg_sleep_build.format(avg_sleep_without_hours, avg_sleep_without_minutes) + \
                    "You might sleep longer if you exercised more often."
        elif not sleep_without_exercise:
            return avg_sleep_build.format(avg_sleep_with_hours, avg_sleep_with_minutes) + \
                    "You always exercise so you must sleep well :)"
        else:
            avg_both = (avg_sleep_without+avg_sleep_with)/2
            avg_both_hours, avg_both_minutes = divmod(avg_both, 60)
            if avg_sleep_with > avg_sleep_without:
                return avg_sleep_build.format(avg_both_hours, avg_both_minutes) + \
                    "On days you exercise, you tend to get " + \
                    "{} more minutes of sleep".format(avg_sleep_with-avg_sleep_without)
            else:
                return avg_sleep_build.format(avg_both_hours, avg_both_minutes) + \
                    "On days you exercise, you tend to get " + \
                    "{} less minutes of sleep".format(avg_sleep_without-avg_sleep_with)
