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
def index():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM contacts")
	data = cur.fetchall()
	return render_template('index.html', contacts = data)


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
		flash('Contact Added sauccesfully')
	return redirect(url_for('index'))

@app.route('/edit/<id>')
def edit_contact(id):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM contacts where id = %s", (id))
	x = cur.fetchall()
	data = x[0]
	print(data)
	return render_template("edition.html", data = data)

@app.route('/change/<id>', methods=['POST'])
def change_contact(id):
	if request.method == 'POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		cur = mysql.connection.cursor()
		cur.execute("UPDATE contacts SET fullname=%s, phone=%s, email=%s where id =%s", (fullname, phone, email, id))
		mysql.connection.commit()
		flash('Contact UPDATE sauccesfully')
		return redirect(url_for("index"))

@app.route('/delete/<string:id>')
def delete_contact(id):
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM contacts where id=%s", (id,))
	mysql.connection.commit()
	flash('Contact Deleted sauccesfully')
	return redirect(url_for('index'))


#Iniciar el servicio
if __name__ == '__main__':
	app.run(port= 3000, debug = True)