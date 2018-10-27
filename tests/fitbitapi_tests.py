import cardea_python.fitbitapi as fitbitapi


def test_get_exercise_by_date():
        fb = fitbitapi.FitbitApi("6KT96H",
            "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2S1Q5NkgiLCJhdWQiOiIyMkQ3QjkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyd2VpIHJociByYWN0IHJudXQgcnNsZSIsImV4cCI6MTUzNzczNjkyNSwiaWF0IjoxNTM3NzA4MTI1fQ.AEOGSVFjOfu3dBhOP6Tu6siDukKvV9nAqVHc4575ko4")
        assert "activities" in fb.get_exercise_by_date("2018-09-22")

def test_get_sleep_by_date_range():
    fb = fitbitapi.FitbitApi("6KT96H",
        "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2S1Q5NkgiLCJhdWQiOiIyMkQ3QjkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyd2VpIHJociByYWN0IHJudXQgcnNsZSIsImV4cCI6MTUzNzczNjkyNSwiaWF0IjoxNTM3NzA4MTI1fQ.AEOGSVFjOfu3dBhOP6Tu6siDukKvV9nAqVHc4575ko4")
    assert "sleep" in fb.get_sleep_by_date_range("2018-09-12", "2018-09-22")

def test_get_avg_hearRate_by_date_range():
    fb = fitbitapi.FitbitApi("6KT96H",
        "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2S1Q5NkgiLCJhdWQiOiIyMkQ3QjkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyd2VpIHJociByYWN0IHJudXQgcnNsZSIsImV4cCI6MTUzNzczNjkyNSwiaWF0IjoxNTM3NzA4MTI1fQ.AEOGSVFjOfu3dBhOP6Tu6siDukKvV9nAqVHc4575ko4")
    assert "activities-heart" in fb.get_avg_hearRate_by_date_range("2018-09-12", "2018-09-22")

def test_get_weight_by_date_range():
    fb = fitbitapi.FitbitApi("6KT96H",
        "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2S1Q5NkgiLCJhdWQiOiIyMkQ3QjkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyd2VpIHJociByYWN0IHJudXQgcnNsZSIsImV4cCI6MTUzNzczNjkyNSwiaWF0IjoxNTM3NzA4MTI1fQ.AEOGSVFjOfu3dBhOP6Tu6siDukKvV9nAqVHc4575ko4")
    assert "weight" in fb.get_weight_by_date_range("2018-09-12", "2018-09-22")
