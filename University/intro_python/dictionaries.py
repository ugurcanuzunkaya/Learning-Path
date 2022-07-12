monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'} 
print('The third month is ' + monthNumbers[3])
dist = monthNumbers['Apr'] - monthNumbers['Jan'] 
print('Apr and Jan are', dist, 'months apart')
