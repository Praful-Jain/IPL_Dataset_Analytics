import csv
import matplotlib.pyplot as plt

csv_file = r'matches.csv'

with open(csv_file) as file :
    match_reader = csv.DictReader(file)
    
    # Will store the number of matches played each season
    matches_count = {}
    
    for row in match_reader :
        matches_count[row['season']] = matches_count.get(row['season'] , 0) + 1
        
for i in matches_count :
    print(i ," : ",matches_count[i])   
    
# Plotting the bar graph
plt.bar(matches_count.keys(),matches_count.values())
plt.xlabel('Year')
plt.xticks(rotation = 90)
plt.ylabel('No. of matches')
plt.title('Number of matches played per year for all the years in IPL.')
plt.show() 