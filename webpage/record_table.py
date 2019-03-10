# import things
from flask_table import Table, Col
import retrieve_record

user_id="de946eab-7f5a-4323-9867-7f1190fb1f5a"
record=retrieve_record.retrieve_record(user_id)

# Declare your table
class ItemTable(Table):
    date = Col('Date')
    symptoms=Col('Symptom')
    diagnosis=Col('Diagnosis')
    prescription=Col('Prescription')
    

# Get some objects
class Item(object):
    def __init__(self,date,symptom,diagnosis,prescription):
        self.date = date
        self.symptom = symptom
        self.diagnosis = diagnosis
        self.prescription = prescription


items=[]

for i in range(len(record)):
	if bool(record[i]):
		items.append(record[i])

		


print(items)


# Populate the table
table = ItemTable(items)

# Print the html
print(table.__html__())
# or just {{ table }} from within a Jinja template