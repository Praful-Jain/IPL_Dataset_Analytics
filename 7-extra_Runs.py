import csv
import matplotlib.pyplot as plt

csv_file = r'matches.csv'

with open(csv_file) as file :
    match_reader = csv.DictReader(file)
    
    extra_runs = {}
    
    for row in match_reader :
        if(row['season'] == '2016') :
            extra_runs[row['winner']] =  extra_runs.get(row['winner'] , 0) + int(row['win_by_runs'])
        
for i in extra_runs:
    print(i , " : " , extra_runs[i])

# Plotting the bar graph
plt.bar(extra_runs.keys(),extra_runs.values())
plt.xlabel('Team name')
plt.xticks(rotation=90)
plt.ylabel('Extra runs scored')
plt.title('Extra runs conceded per team in the year 2016')
plt.show()