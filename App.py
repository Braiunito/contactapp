from flask import Flask


#Codio para iniciar el servidor
app=Flask(__name__)



if __name__ == '__main__':
	app.run(port= 3000, debug = True)