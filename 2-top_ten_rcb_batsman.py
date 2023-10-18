import csv 
import matplotlib.pyplot as plt

csv_file = r'deliveries.csv'

with open(csv_file) as file:
    csv_reader = csv.DictReader(file)
    
    # Dictionary to store runs of players of rcb
    runs_scored={}
    
    for row in csv_reader:
        if row['batting_team'] == 'Royal Challengers Bangalore' :
            if row['batsman'] in runs_scored :
                runs_scored[row['batsman']] += int(row['total_runs']) 
            else :
                runs_scored[row['batsman']] = int(row['total_runs']) 
          
    # Sorting in descending order      
    runs_scored = dict(sorted(runs_scored.items(),key = lambda x:x[1], reverse=True))
    
    # Dictionary to store top 10 RCB batsman
    top_ten={}
    count=0
    for i in runs_scored :
        top_ten[i]=runs_scored[i]
        count+=1
        if count==10 :
            break
        
for i in top_ten:
    print(i , " : " , top_ten[i])

# Plotting the bar graph
plt.bar(top_ten.keys(),top_ten.values())
plt.xlabel('Player Name')
plt.xticks(rotation=90)     #To print the labels vertically on the x-axis in Matplotlib,
plt.ylabel('Total Runs Scored')
plt.title('Top 10 batsmen of RCB')
plt.show()