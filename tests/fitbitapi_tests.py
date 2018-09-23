import cardea_python.fitbitapi

def setup(module):
    self.fb = fitbitapi.FitbitApi("6KT96H",
        "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2S1Q5NkgiLCJhdWQiOiIyMkQ3QjkiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyd2VpIHJociByYWN0IHJudXQgcnNsZSIsImV4cCI6MTUzNzY5NzQ1MiwiaWF0IjoxNTM3NjY4NjUyfQ.WsFw9PONJlCd384YWSmCnzFvtCI_2VxeIXL91-a5Jkg")

def test_get_exercise_by_date:
    self.fb.get_exercise_by_date("2018-09-22")
