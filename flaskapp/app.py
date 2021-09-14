from flask import Flask, render_template, request, render_template, url_for, flash
from flask_mysqldb import MySQL
import pandas as pd
from pandas import DataFrame
import yaml

# import mysql.connector


app = Flask(__name__)

# config db
db = yaml.safe_load(open('config.yaml'))
app.config['MYSQL_HOST'] = db['host']
app.config['MYSQL_USER'] = db['user']
app.config['MYSQL_PASSWORD'] = db['password']
app.config['MYSQL_DB'] = db['db']
app.config['MYSQL_PORT'] = db['port']

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index2():
    if request.method == "GET":
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM covid2020")
            data = cur.fetchall()
            cur1 = mysql.connection.cursor()
            cur1.execute("SELECT * FROM covid2021")
            data1 = cur1.fetchall()
            cur2 = mysql.connection.cursor()
            cur2.execute("SELECT * FROM patients")
            data2 = cur2.fetchall()
            cur3 = mysql.connection.cursor()
            cur3.execute("SELECT * FROM statesid")
            data3 = cur3.fetchall()

            return render_template('index.html', titles1=data1, titles=data, titles2=data2, titles3=data3 )
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

        finally:
            cur1.close()

    else:
        return render_template('index.html')


@app.route('/insert1', methods=['POST'])
def insert1():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        state = request.form['state']
        cases = request.form['cases']
        deaths = request.form['deaths']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO covid2020 (id, state, cases, deaths) VALUES (%s, %s, %s, %ss)",
                    (id, state, cases, deaths))
        mysql.connection.commit()
        return render_template('index.html')


@app.route('/insert2', methods=['POST'])
def insert2():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id = request.form['id']
        state = request.form['state']
        cases = request.form['cases']
        deaths = request.form['deaths']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO covid2021 (id, State, Cases, Deaths) VALUES (%s, %s, %s, %s)",
                    (id, state, cases, deaths))
        mysql.connection.commit()
        return render_template('index.html')


@app.route('/delete/<int:id>', methods=['GET'])
def delete1(id):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM covid2020 WHERE id=%s", (id,))
    mysql.connection.commit()
    return render_template('index.html')


@app.route('/update', methods=['POST', 'GET'])
def update1():
    if request.method == 'POST':
        # id_data = request.form['id']
        id = request.form['id']
        state = request.form['state']
        cases = request.form['cases']
        deaths = request.form['deaths']
        cur = mysql.connection.cursor()
        cur.execute(" UPDATE covid2021 SET id=%s, state=%s, cases=%s, deaths=%s WHERE id=%s",
                    (id, state, cases, deaths))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/update', methods=['POST', 'GET'])
def update2():
    if request.method == 'POST':
        # id_data = request.form['id']
        id = request.form['id']
        state = request.form['state']
        cases = request.form['cases']
        deaths = request.form['deaths']
        cur = mysql.connection.cursor()
        cur.execute(" UPDATE covid2021 SET id=%s, state=%s, cases=%s, deaths=%s WHERE id=%s",
                    (id, state, cases, deaths))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return render_template('index.html')
    else:
        return render_template('index.html')


# if __name__ == "__main__":
#     app.run(debug=True)
# #     if request.method == 'POST':
#         user_details = request.form
#         name = user_details['name']
#         email = user_details['email']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO users(users,email) VALUES(%s,%s)", (name, email))
#         mysql.connection.commit()
#         cur.close()
#         return render_template('/users')
#     return render_template('index.html')
#
#
# @app.route('/users')
# def users():
#     cur = mysql.connection.cursor()
#     value = cur.execute("SELECT * FROM users")
#     if value > 0:
#         users_details = cur.fetchall()
#         return render_template('users.html', details=users_details)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
