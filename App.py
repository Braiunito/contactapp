from flask import Flask, render_template
from flask_mysqldb import MySQL

#Codio para iniciar el servidor
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='42922075'
app.config['MYSQL_DB']='flaskcontacts'
mysql= MySQL(app)

#Decoradores
@app.route('/')
def Index():
	return render_template('index.html')

@app.route('/add_contact')
def add_contact():
	return "Add contact"

@app.route('/edit')
def edit_contact():
	return "Edit contact"

@app.route('/delete')
def delete_contact():
	return "Delete contact"


#Iniciar el servicio
if __name__ == '__main__':
	app.run(port= 3000, debug = True)