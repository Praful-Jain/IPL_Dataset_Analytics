import csv
import matplotlib.pyplot as plt

csv_file = r'umpires.csv'

with open(csv_file) as file :
    umpire_reader = csv.DictReader(file)
    
    # Dictionary to store foreign umpires history
    umpire_origin = {}
    
    for row in umpire_reader :
        if row[' country'] != ' India' :
            umpire_origin[row[' country']] = umpire_origin.get(row[' country'] , 0) + 1
            
for i in umpire_origin:
    print(i," : ",umpire_origin[i])

# Plotting the bar graph
plt.bar(umpire_origin.keys(),umpire_origin.values())
plt.xlabel('Country')
plt.xticks(rotation=90)     #To print the labels vertically on the x-axis in Matplotlib,
plt.ylabel('Count')
plt.title('Empires origin')
plt.show()