"""
to run enter commands in terminal:
export FLASK_APP=mysql-test.py
export FLASK_ENV=development
python -m flask run
"""

from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)
# Database connection info. Note that this is not a secure connection.
app.config['MYSQL_DATABASE_USER'] = '233user' #database user 
app.config['MYSQL_DATABASE_PASSWORD'] = 'CSCIproject233#' #password
app.config['MYSQL_DATABASE_DB'] = 'financials' #database name 
app.config['MYSQL_DATABASE_HOST'] = 'localhost' #host 
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

#homepage
@app.route('/')
def menu_page():
    return render_template('index.html')

#endpoint for Company Name or Ticker 
@app.route('/ticker', methods=['GET', 'POST'])
def name_search():
    if request.method == "POST": 
        company = request.form['company']
        # search by company name 
        cursor.execute("SELECT Company_Name, Symbol FROM company_details WHERE Company_Name LIKE %s OR Symbol LIKE %s", (company, company))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT Company_Name, Symbol FROM company_details")
            conn.commit()
            data = cursor.fetchall()
        return render_template('ticker-results.html', data=data)
    return render_template('ticker.html') 
    
#endpoint for EPS
@app.route('/EPS', methods=['GET', 'POST'])
def EPS_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, EPS FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE (Company_Name LIKE %s OR income_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, EPS FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, EPS FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE Company_Name LIKE %s OR income_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('EPS-results.html', data=data)
    return render_template('EPS.html') 

#endpoint for assets
@app.route('/assets', methods=['GET', 'POST'])
def assets_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, balance_sheets.Total_Current_Assets, balance_sheets.Total_Assets FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol WHERE (Company_Name LIKE %s OR balance_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, balance_sheets.Total_Current_Assets, balance_sheets.Total_Assets FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, balance_sheets.Total_Current_Assets, balance_sheets.Total_Assets FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol WHERE Company_Name LIKE %s OR balance_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('asset-results.html', data=data)
    return render_template('assets.html') 

#endpoint for liabilities
@app.route('/liabilities', methods=['GET', 'POST'])
def liabilities_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, balance_sheets.Total_Current_Liabilities, balance_sheets.Total_Liabilities FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol WHERE (Company_Name LIKE %s OR balance_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, balance_sheets.Total_Current_Liabilities, balance_sheets.Total_Liabilities FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, balance_sheets.Total_Current_Liabilities, balance_sheets.Total_Liabilities FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol WHERE Company_Name LIKE %s OR balance_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('liability-results.html', data=data)
    return render_template('liabilities.html') 

#endpoint for FCF
@app.route('/FCF', methods=['GET', 'POST'])
def FCF_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT cashFLow_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Free_Cash_Flow FROM cashFLow_sheets INNER JOIN company_details ON company_details.Symbol =  cashFLow_sheets.Symbol WHERE (Company_Name LIKE %s OR cashFlow_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT cashFLow_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Free_Cash_Flow FROM cashFLow_sheets INNER JOIN company_details ON company_details.Symbol =  cashFLow_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT cashFLow_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Free_Cash_Flow FROM cashFLow_sheets INNER JOIN company_details ON company_details.Symbol =  cashFLow_sheets.Symbol WHERE Company_Name LIKE %s OR cashFlow_sheets.Symbol LIKE %s", (company,company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('FCF-results.html', data=data)
    return render_template('FCF.html') 

#endpoint for revenue 
@app.route('/revenue', methods=['GET', 'POST'])
def revenue_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Revenue FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE (Company_Name LIKE %s OR income_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Revenue FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Revenue FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE Company_Name LIKE %s OR income_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('revenue-results.html', data=data)
    return render_template('revenue.html') 

#endpoint for equity 
@app.route('/equity', methods=['GET', 'POST'])
def equity_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Total_Shareholders_Equity FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol WHERE (Company_Name LIKE %s OR balance_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Total_Shareholders_Equity FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Total_Shareholders_Equity FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol WHERE Company_Name LIKE %s OR balance_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('equity-results.html', data=data)
    return render_template('equity.html') 

#endpoint for debt 
@app.route('/debt', methods=['GET', 'POST'])
def debt_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Total_Debt FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol WHERE (Company_Name LIKE %s OR balance_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Total_Debt FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT balance_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Total_Debt FROM balance_sheets INNER JOIN company_details ON company_details.Symbol = balance_sheets.Symbol WHERE Company_Name LIKE %s OR balance_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('debt-results.html', data=data)
    return render_template('debt.html') 

#endpoint for net income 
@app.route('/netIncome', methods=['GET', 'POST'])
def netIncome_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Net_Income FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE (Company_Name LIKE %s OR income_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Net_Income FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Net_Income FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE Company_Name LIKE %s OR income_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('netIncome-results.html', data=data)
    return render_template('netIncome.html') 

#endpoint for operating income 
@app.route('/operatingIncome', methods=['GET', 'POST'])
def operatingIncome_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Operating_Income FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE (Company_Name LIKE %s OR income_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Operating_Income FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Operating_Income FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE Company_Name LIKE %s OR income_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('operatingIncome-results.html', data=data)
    return render_template('operatingIncome.html') 

#endpoint for profit margin 
@app.route('/profitMargin', methods=['GET', 'POST'])
def profitMargin_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Profit_Margin FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE (Company_Name LIKE %s OR income_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Profit_Margin FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Profit_Margin FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE Company_Name LIKE %s OR income_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('profitMargin-results.html', data=data)
    return render_template('profitMargin.html') 

#endpoint for DPS 
@app.route('/DPS', methods=['GET', 'POST'])
def DPS_search():
    if request.method == "POST": 
        company = request.form['company']
        year = request.form['year']
        # search by company name 
        cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Dividend_per_Share FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE (Company_Name LIKE %s OR income_sheets.Symbol LIKE %s) AND YEAR(Date) = %s", (company, company, year))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and company == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Dividend_per_Share FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol")
            conn.commit()
            data = cursor.fetchall()
        if len(data) == 0 and year == 'all': 
            cursor.execute("SELECT income_sheets.Symbol, Company_Name, YEAR(Date) AS Year, Dividend_per_Share FROM income_sheets INNER JOIN company_details ON company_details.Symbol = income_sheets.Symbol WHERE Company_Name LIKE %s OR income_sheets.Symbol LIKE %s", (company, company))
            conn.commit()
            data = cursor.fetchall()
        return render_template('DPS-results.html', data=data)
    return render_template('DPS.html') 

if __name__ == '__main__':
    app.debug = True
    app.run()

