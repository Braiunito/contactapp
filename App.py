from flask import Flask


#Codio para iniciar el servidor
app=Flask(__name__)


#Decoradores
@app.route('/')
def Index():
	return "Hola mundo!"

@app.route('/add_contact')
def add_contact():
	return "Add contact"

@app.route('/edit')
def edit_contact():
	return "Edit contact"

@app.route('/delete')
def delete_contact():
	return "Delete contact"

if __name__ == '__main__':
	app.run(port= 3000, debug = True)