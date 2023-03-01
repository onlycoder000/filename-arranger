import csv
import os
import shutil




d=[]
with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        d.append(row[0])




dir_path = './data'

# list file and directories
res = os.listdir(dir_path)

# res=res.sort()

for i in res:
    p=d[int(i.replace('Bank - Google Maps (','').replace(').csv',''))]
    shutil.copyfile('./data/'+i,'./output/'+p+'_'+str(int(i.replace('Bank - Google Maps (','').replace(').csv','')))+'.csv')



print(d)