from flask import Flask
from flask_restful import Resource, Api
import datetime
from datetime import timedelta
import sleepAnalysis

app = Flask(__name__)
api = Api(app)


class CardeaSleep(Resource):
    def get(self):
        userid = request.args.get("userid")
        today = datetime.date.today()
        startdate = today.strftime('%Y-%m-%d')
        enddate = (today - timedelta(days=30)).strftime('%Y-%m-%d')
        sa = SleepAnalysis()
        sa.sleep_and_exercise(userid, startdate, enddate)

api.add_resource(CardeaAuth, '/')

if __name__ == '__main__':
    app.run(debug=True)
