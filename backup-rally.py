import sys
import time
from pyral import Rally, rallySettings
from jinja2 import Environment, FileSystemLoader
options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]
server, user, password, workspace, project = rallySettings(options)
rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('mypyral.log')
env = Environment(loader = FileSystemLoader('.'))
template = env.get_template('testCase.html')

if not args:
 queryCriteria = 'Project.Name contains "{0}"'.format(project)
else:
 queryCriteria = 'Project.Name contains "{0}"'.format(args[0])

# First we query once to get each Test Set for the given sprint
response = rally.get('TestFolder', fetch="TestCases,FormattedID,Name", query=queryCriteria)
if response.errors:
 sys.stdout.write("\n".join(response.errors))
 sys.exit(1)
# Now we loop over the test sets, and then the test cases
for testFolder in response:
 thisFolder = testFolder.FormattedID
 testCases = rally.get('TestCase', fetch="FormattedID,PreConditions,Name,Steps,ValidationInput,Type,PostConditions",query="FormattedID = {0}".format(thisFolder))
 for testCase in testCases:
  fileName = "{0}_{1}-{2}_{3}.html".format(thisFolder, testFolder.Name, testCase.FormattedID, testCase.Name)
  savedTC = open(fileName[:256], 'w') #truncate filename to 256 characters
  savedTC.write(template.render(tc_name=testCase.Name, steps=testCase.Steps, preconditions=testCase.PreConditions, validationInput=testCase.ValidationInput).encode('utf-8', 'ignore'))
  savedTC.close()
  print "{0} saved.".format(fileName)