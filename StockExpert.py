import os
import sqlite3
from flask import Flask, jsonify, render_template, request, url_for, json

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'StockExpert.db')
))

def connect_db():
	"""Connects to the specific database."""
	connection = sqlite3.connect(app.config['DATABASE'])
	return connection
	
@app.route("/hello/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/home/")
def home():
	title = "Home"
	head = "At home"
	data = {'title':title,'head':head}
	return render_template('home.html', data = data)
	
#------------------------ DATATABLES START ------------------------#
class BaseDataTables:    
	def __init__(self, request, columns, collection):
		self.columns = columns
		self.collection = collection
		# values specified by the datatable for filtering, sorting, paging
		self.request_values = request.values
		# results from the db
		self.result_data = None
		# total in the table after filtering
		self.cardinality_filtered = 0
		# total in the table unfiltered
		self.cadinality = 0
		self.run_queries()

	def output_result(self):
		output = {}

		# output['sEcho'] = str(int(self.request_values['sEcho']))
		# output['iTotalRecords'] = str(self.cardinality)
		# output['iTotalDisplayRecords'] = str(self.cardinality_filtered)
		aaData_rows = []

		for row in self.result_data:
			aaData_row = []
			for i in range(len(self.columns)):
				print (row, self.columns, self.columns[i])
				aaData_row.append(str(row[ self.columns[i] ]).replace('"','\\"'))
			aaData_rows.append(aaData_row)

		output['aaData'] = aaData_rows
		return output

	def run_queries(self):

		self.result_data = self.collection
		self.cardinality_filtered = len(self.result_data)
		self.cardinality = len(self.result_data)

columns = [ '', 'Variable', 'Lower Bound', 'Upper Bound']

@app.route('/')
def index():
	return render_template('myEstimates.html', columns=columns)
	return 'Hello World!'

@app.route('/example1')
def example1():
	collection1 = [
					dict(zip(columns, [1,"Revenue Growth","",""])),
					dict(zip(columns, [2,"Gross Margin","",""])),
					dict(zip(columns, [3,"Operating Margin","",""])),
	]
	results = BaseDataTables(request, columns, collection1).output_result()
	return json.dumps(results)
	
@app.route('/example2')
def example2():
	collection2 = [
					dict(zip(columns, [1,"Revenue Growth",5,10])),
					dict(zip(columns, [2,"Gross Margin",23,65])),
					dict(zip(columns, [3,"Operating Margin",4,6.6]))
	]	
	results = BaseDataTables(request, columns, collection2).output_result()
	return json.dumps(results)
@app.route('/example3')
def example3():
	collection3 = [
					dict(zip(columns, [1,"Revenue Growth",6,10])),
					dict(zip(columns, [2,"Gross Margin",54,65]))
	]
	results = BaseDataTables(request, columns, collection3).output_result()
	# return the results as a string for the datatable
	return json.dumps(results)

#------------------------- DATATABLES END -------------------------#
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
