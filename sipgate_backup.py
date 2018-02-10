import csv, json, requests, os, wget, urllib

user="w0" # can be retrieved from sipgate URL, i.e. last two letters of https://secure.live.sipgate.de/settings/phone/index/webuser/1234567w0
limit=100 # max. items per call, max. 1000 (limited by sipgate api)
fileloc='/home/gauner/Downloads/any_prefix '+user+' any_suffix/' # local filepath, for windows use "c:\\users\\whatever\\" form
username='...' # Sipgate username
password='...'# Sipgate password

url = 'https://api.sipgate.com/v1/'+user+'/history'
data=[]
header={}

i=0
j=0
while True:
	response = requests.request("GET", url, params={"offset":i*limit,"limit":limit}, auth=(username, password))
	datarow=json.loads(response.text)["items"]
	if not datarow:
		break
	else:
		print(datarow[0])
		print ("retrieving list from entry",i*limit)
		for row in datarow:
			header.update(dict.fromkeys(set(row.keys()).difference(header), ''))
			print ("processing item",str(j)+":",row["id"])
			j=j+1
		data.extend(datarow)
		i+=1

print("Retrieved "+str(j)+" items.")
		
if not os.path.exists(fileloc):
    os.makedirs(fileloc)

with open(fileloc+user+'.csv', 'w') as csvfile:
	output = csv.DictWriter(csvfile, header.keys(), lineterminator="\n")
	output.writeheader()

	i=0    
	for row in data:
		row.update(dict.fromkeys(set(header.keys()).difference(row), ''))
		print('writing csv line for item',str(i)+":",row)
		output.writerow(row)
		for item in {k: v for k, v in header.items() if "url" in k.lower()}.keys():
			filename=os.path.basename(urllib.parse.urlparse(row[item]).path)
			if row[item]:
				filepath=fileloc+user+'_'+row["id"]+'_'+item.lower().replace('url','')+'_'+filename
				if not os.path.isfile(filepath):
					print ("retrieving file for item",str(i)+":",row[item])
					wget.download(row[item], filepath) 
				else:
					print ('file for item',str(i)+" exists:",filepath)
		i+=1
