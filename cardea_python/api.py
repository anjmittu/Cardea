from flask import Flask, request
from flask_restful import Resource, Api
import datetime
from datetime import timedelta
import sleepAnalysis

app = Flask(__name__)
api = Api(app)


class CardeaSleep(Resource):
    def get(self):
        userid = request.args.get("userid")
        auth_tok = request.args.get("auth_tok")
        today = datetime.date.today()
        enddate = today.strftime('%Y-%m-%d')
        startdate = (today - timedelta(days=30)).strftime('%Y-%m-%d')
        sa = sleepAnalysis.SleepAnalysis(userid, auth_tok)
        return sa.sleep_and_exercise(startdate, enddate)


api.add_resource(CardeaSleep, '/CardeaSleep')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
