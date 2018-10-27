import cardea_python.analysis.heartRateAnalysis as heartRateAnalysis
import cardea_python.analysis.sleepAnalysis as sleepAnalysis

def test_get_exercise_by_date():
        sleepA = sleepAnalysis.SleepAnalysis("6KT96H",
            "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2S1Q5NkgiLCJhdWQiOiIyMkQ3QjkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyd2VpIHJociByYWN0IHJudXQgcnNsZSIsImV4cCI6MTUzNzczNjkyNSwiaWF0IjoxNTM3NzA4MTI1fQ.AEOGSVFjOfu3dBhOP6Tu6siDukKvV9nAqVHc4575ko4")
        answer = "You get an average night sleep of 6.0 hours and 33.75 minutes. On days you exercise, you tend to get 33.5 more minutes of sleep"
        assert sleepA.sleep_and_exercise("2018-08-30", "2018-09-22") == answer
