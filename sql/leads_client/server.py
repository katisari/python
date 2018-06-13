from flask import Flask, render_template, redirect, request, session
from mysqlconnect import connectToMySQL
app = Flask(__name__)
app.secret_key = "HELLO"
mysql = connectToMySQL('lead_gen_business')

@app.route('/')
def index():
    if 'query' in session:
        print("")
    else:
        session['query'] = "SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS 'name', COUNT(leads.leads_id) AS 'num_leads' from clients LEFT JOIN sites on sites.client_id = clients.client_id LEFT JOIN leads on leads.site_id = sites.site_id GROUP BY clients.client_id ORDER BY num_leads DESC"
    session['all_clients'] = mysql.query_db(session['query'])
    # start_date ="2011-01-01"
    # end_date = "2015-03-25"
    # session['query'] = f"SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS 'name', COUNT(leads.leads_id) AS 'num_leads' from clients LEFT JOIN sites on sites.client_id = clients.client_id LEFT JOIN leads on leads.site_id = sites.site_id WHERE leads.registered_datetime >= DATE_FORMAT('{start_date}', '%Y') AND leads.registered_datetime <= DATE_FORMAT('{end_date}', '%Y') GROUP BY clients.client_id ORDER BY num_leads DESC"
    print(session['query'])
    return render_template("index.html", clients=session['all_clients'])

@app.route('/time', methods=['POST'])
def time():
    print(request.form['start_date'])
    print(type(request.form['start_date']))
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    session['query'] = f"SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS 'name', COUNT(leads.leads_id) AS 'num_leads' from clients LEFT JOIN sites on sites.client_id = clients.client_id LEFT JOIN leads on leads.site_id = sites.site_id WHERE leads.registered_datetime >= DATE_FORMAT('{start_date}', '%Y') AND leads.registered_datetime <= DATE_FORMAT('{end_date}', '%Y') GROUP BY clients.client_id ORDER BY num_leads DESC"
    # print(session['all_clients'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)