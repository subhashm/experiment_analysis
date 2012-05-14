import collections
import csv
import sys

data=collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: '')))
entr=collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: 0)))
strdata=collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: '')))
count=0
#reading the data row by row as a dictionary of elements(key:columnname, value: value for the row and column).
for row in csv.DictReader(open('C:\\Users\\subhash\\Documents\\subhash\\interests\\C_Study\Project\\whatdoyouknow\\grockit_all_data\\valid_test.csv'),delimiter=','):
	count=count+1
	if count<=20000:
		entr[row['user_id']][row['track_name']]['numentries_track']=entr[row['user_id']][row['track_name']]['numentries_track']+1
		entr[row['user_id']][row['track_name']]['aveplayers_track']=entr[row['user_id']][row['track_name']]['aveplayers_track']+int(row['num_players'])
		entr[row['user_id']][row['track_name']]['aveplayers_track']=int(entr[row['user_id']][row['track_name']]['aveplayers_track']/entr[row['user_id']][row['track_name']]['numentries_track'])
		strdata[row['user_id']][row['track_name']]['qsid']=strdata[row['user_id']][row['track_name']]['qsid']+' '+row['question_set_id']
	else:
		break
count=0
#reading the data row by row as a dictionary of elements(key:columnname, value: value for the row and column).
for row in csv.DictReader(open('C:\\Users\\subhash\\Documents\\subhash\\interests\\C_Study\Project\\whatdoyouknow\\grockit_all_data\\training.csv'),delimiter=','):
	count=count+1
	if count<=20000:		
		#data[row['user_id']][row['question_id']]['user_id']=str(row['user_id'])
		#data[row['user_id']][row['question_id']]['question_id']=str(row['question_id'])
		data[row['user_id']][row['question_id']]['qsid_track']=strdata[row['user_id']][row['track_name']]['qsid']
		data[row['user_id']][row['question_id']]['numentr_track']=str(entr[row['user_id']][row['track_name']]['numentries_track'])
		data[row['user_id']][row['question_id']]['aveplayers_track']=str(entr[row['user_id']][row['track_name']]['aveplayers_track'])
		data[row['user_id']][row['question_id']]['track_name']=str(row['track_name'])
		data[row['user_id']][row['question_id']]['game_type']=str(row['game_type'])
		data[row['user_id']][row['question_id']]['subtrack_name']=str(row['subtrack_name'])
		data[row['user_id']][row['question_id']]['correct']=str(row['correct'])

	else:
		break

#Opens a csv file to write the contents by reading from the dictionary. The structure of the dictionary needs to be specified to read from it. Also the line terminator is specified as it differs from one implementation to other
out = csv.DictWriter(open('C:\\Users\\subhash\\Documents\\subhash\\interests\\C_Study\Project\\whatdoyouknow\\grockit_all_data\\testdata.csv','w'),{'qsid_track':'qsid_track','numentr_track':'numentr_track','aveplayers_track':'aveplayers_track','track_name':'track_name','game_type':'game_type','subtrack_name':'subtrack_name','correct':'correct'}, lineterminator='\n')
out.writerow({'qsid_track':'qsid_track','numentr_track':'numentr_track','aveplayers_track':'aveplayers_track','track_name':'track_name','game_type':'game_type','subtrack_name':'subtrack_name','correct':'correct'})

for user in data:
	for qid in data[user]:
		out.writerow(data[user][qid])

print '------------end---------------'