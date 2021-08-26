import csv

with open('test.csv','w',newline='') as fp:
      a = csv.writer(fp,delimiter=',')
      data=[['stock','sales'],    
           ['100','24'],
           ['120','33'],
           ['23','5']]
      a.writerows(data)