#import json

#def save_report_json(report, filename):
   # try:
        #with open(filename, "w") as file:
            #json.dump(report, file)
       # return "Report saved in JSON successfully."
    #except Exception as e:
        #return f"Error: {e}"

# Test
#report = {"Name": "Conix", "Average": 85.25, "Attendance": 85, "Status": "Eligible"}
#print(save_report_json(report, "student_report.json"))

#import json

#def load_report_json(filename):
    #try:
        #with open(filename, "r") as file:
            #report = json.load(file)
        #return report
    #except Exception as e:
        #return f"Error: {e}"

# Test
#print(load_report_json("student_report.json"))

#import json

#def save_class_reports_json(database, filename):
    #try:
        #with open(filename, "w") as file:
            #json.dump(database, file)
        #return "Class reports saved in JSON successfully."
    #except Exception as e:
        #return f"Error: {e}"

# Example usage
#database = [
    #{"Name": "Conix", "Average": 93, "Attendance": 92, "Status": "Honors"},
    #{"Name": "Leonald", "Average": 71.75, "Attendance": 75, "Status": "Probation"},
    #{"Name": "Alex", "Average": 62.25, "Attendance": 70, "Status": "Probation"}
]

#print(save_class_reports_json(database, "class_reports.json"))

import json

def load_class_reports_json(filename):
    try:
        with open(filename, "r") as file:
            database = json.load(file)
        return database
    except Exception as e:
        return f"Error: {e}"

# Test
reports = load_class_reports_json("class_reports.json")
print(reports)

