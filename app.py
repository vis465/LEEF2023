from flask import *
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "https://www.townscript.com/api/bookingflow/eventPageData?eventCode=leef-2023-140234"
    headers = {
        "accept": "application/json",
        "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJST0xFIjoiUk9MRV9VU0VSIiwic3ViIjoidmlzdjY4MTJAZ21haWwuY29tIiwiYXVkaWVuY2UiOiJ3ZWIiLCJjcmVhdGVkIjoxNjk4NjA2ODYwNDk2LCJNQUdJQ19MT0dJTiI6ZmFsc2UsIlVTRVJfSUQiOjQzNjExNzQsImV4cCI6MTcwNjM4Mjg2MH0.hl5UKkR5OKb2ki1tXNEfLFbOrc6nI5hjHV7k2l15gTD86P0erEHu3np787usBsvrf0mwGNazfveqaMO0ENQZLg"
    }
    data = requests.get(url, headers=headers)   
    json_data = json.loads(data.text)
    total = (json_data['data']['normalDisplayTicketList'][0]['ticket']['totalTickets'] - json_data['data']['normalDisplayTicketList'][0]['availableCount'])
    new_var = (total/250)*100
    return render_template("index.html", total_tickets_sold=total, new_percent=new_var)


@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="80")