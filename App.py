from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Codio para iniciar el servidor
app=Flask(__name__)

#MySql Connection
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='42922075'
app.config['MYSQL_DB']='flaskcontacts'
mysql= MySQL(app)

#Decoradores
@app.route('/')
def Index():
	return render_template('index.html')


#Sessions/Settings
app.secret_key = 'mysecretkey'

@app.route('/add_contact', methods=['POST'])
def add_contact():
	if request.method == 'POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']

		cur = mysql.connection.cursor()
		cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',(fullname, phone, email))
		mysql.connection.commit()
		flash('Contact Added syccesfully')
	return redirect(url_for('index'))

@app.route('/edit')
def edit_contact():
	return "Edit contact"

@app.route('/delete')
def delete_contact():
	return "Delete contact"


#Iniciar el servicio
if __name__ == '__main__':
	app.run(port= 3000, debug = True)