import csv
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the path to your CSV file.
csv_file = r'deliveries.csv'

# Open the CSV file for reading.
with open(csv_file) as file:
    # Create a CSV reader object.       #here if we use csv_reader = csv.reader(file)  ---   then csv_reader is of list datatype
    csv_reader = csv.DictReader(file)      

    # will store total runs of teams
    total_runs = {}        

    # Iterate through the rows in the CSV file.
    for row in csv_reader :

        if row['batting_team'] in total_runs :
            total_runs[row['batting_team']] += int(row['total_runs'])
        else:
            total_runs[row['batting_team']] = int(row['total_runs'])
            
print(total_runs)

# Plotting the bar graph
plt.bar(total_runs.keys(),total_runs.values())
plt.xlabel('Team')
plt.xticks(rotation=90)
plt.ylabel('Runs')
plt.title('Runs scored by each team')
plt.show()