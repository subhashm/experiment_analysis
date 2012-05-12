import collections
import csv
import sys

data=collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: '')))
entr=collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: 0)))

print data['eee']['fff']['aaa']
print entr['eee']['fff']['aaa']
#reading the data row by row as a dictionary of elements(key:columnname, value: value for the row and column).
for row in csv.DictReader(open('C:\\Users\\subhash\\Documents\\subhash\\interests\\C_Study\Project\\whatdoyouknow\\grockit_all_data\\training.csv'),delimiter=','):
	entr[row['user_id']][row['track_name']]['numentries']=entr[row['user_id']][row['track_name']]['numentries']+1
	entr[row['user_id']][row['track_name']]['aveplayers']=entr[row['user_id']][row['track_name']]['aveplayers']+1
	entr[row['user_id']][row['track_name']]['aveplayers']=int(entr[row['user_id']][row['track_name']]['aveplayers']/entr[row['user_id']][row['track_name']]['numentries'])
	data[row['user_id']][row['track_name']]['qid']=data[row['user_id']][row['track_name']]['qid']+' '+row['question_set_id']
	data[row['user_id']][row['track_name']]['numentries']=str(entr[row['user_id']][row['track_name']]['numentries'])
	data[row['user_id']][row['track_name']]['aveplayers']=str(entr[row['user_id']][row['track_name']]['aveplayers'])



fields = data[data[data.keys()[0]].keys()[0]].keys()
print '---------------------------'
print fields
print '++++++++++++++++++++++++++++'
out = csv.DictWriter(sys.stdout, fields, lineterminator='\n')
out.writerow({'qid':'qid','numentries':'numentries','aveplayers':'aveplayers'})
print fields
for user in data:
	for track in data[user]:
		out.writerow(data[user][track])

print '------------end---------------'