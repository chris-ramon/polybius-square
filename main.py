from flask import Flask, render_template, request, session
import polybios

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		which_matrix = str(request.form["matrix"])
		session["text"] = str(request.form["plain-text"])
		session["matrix_selected"] = which_matrix
		action = str(request.form["action"])
		_result = polybios.polybios_cypher(request.form["plain-text"], which_matrix) \
					if action == 'cipher' else polybios.polybios_decypher(request.form["plain-text"], which_matrix)
		return render_template("index.html", result = _result)
	else:
  		return render_template("index.html", result = None)

app.secret_key = 'polybiossecretkey:D'	

if __name__ == '__main__':
  app.run(debug=True)
