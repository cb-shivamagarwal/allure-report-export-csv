import json
import csv

def jsonFileToDict(filename):
  f = open(filename)
  obj = json.load(f)
  f.close()
  return obj
  

f = jsonFileToDict('suites.json')

suites = f['children']

rows = []
for s in suites:
  suiteName = s['name']
  testRunners = s['children']
  for tR in testRunners:
    testRunnerName = tR['name']
    testClasses = tR['children']
    for tC in testClasses:
      testClassName = tC['name']
      tests = tC['children']
      for t in tests:
        uid = t['uid']
        status = t['status']
        testDetails = jsonFileToDict("test-cases/"+uid+".json")
        
        methodName = testDetails['fullName']
        statusMessage = testDetails['statusMessage'].encode('utf-8') if status != "passed" else ""
        statusTrace = testDetails['statusTrace'].encode('utf-8') if status != "passed" else ""
        row = [uid, status, methodName, statusMessage, statusTrace, testClassName, testRunnerName, suiteName]
        rows.append(row)

fields = ['uid', 'status', 'methodName', 'statusMessage', 'statusTrace', 'testClassName', 'testRunnerName', 'suiteName']

with open("final.csv", 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)
