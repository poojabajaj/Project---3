import csv
import os
from datetime import datetime


def PyBoss(inputfilepath, outputfilepath):

    #open the input file to read from
    with open(inputfilepath, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            next(csvreader, None)
            # Specify the file to write to
            output_path = os.path.join('output', outputfilepath)
            # Open the file using "write" mode. Specify the variable to hold the contents
            with open(output_path, 'w', newline='') as csvfileout:

                # Initialize csv.writer
                csvwriter = csv.writer(csvfileout, delimiter=',')
                # Write the first row (column headers)
                csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

                newdata = []
                date = []
                us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
                # Write the second row
                for row in csvreader:
                    newdata.append(row[0])
                    newdata.append(row[1].split()[0])
                    newdata.append(row[1].split()[1])
                    old_date= row[2]
                    date_str = datetime.strptime(old_date, "%Y-%m-%d").strftime("%m/%d/%Y")
                    newdata.append(date_str)
        
                    newdata.append("***-**-"+ row[3].split("-")[2])
                    for key,value in us_state_abbrev.items():
                        if (row[4] ==key):
                            newdata.append(value)
                    #newdata.append(row[2].split("-")[2]
                    print("newdata" + str(newdata))                                           
                    csvwriter.writerow(newdata)
                    newdata=[]
        


 #   with open('resources1/employee_data2.csv', 'r') as csvfile1:
 #       csvreader2 = csv.reader(csvfile1, delimiter=',')
 #       next(csvreader2, None)
    
PyBoss('resources1/employee_data1.csv', 'output_emp_data1.csv')
PyBoss('resources1/employee_data2.csv', 'output_emp_data2.csv')



           

    




    
    
 
