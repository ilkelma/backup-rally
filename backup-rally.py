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

if args[0] is not None:
 queryCriteria = 'Iteration.Name contains "{0}"'.format(args[0])

# First we query once to get each Test Set for the given sprint
response = rally.get('TestSet', fetch="TestCases,FormattedID", query=queryCriteria)
if response.errors:
 sys.stdout.write("\n".join(errors))
 sys.exit(1)
# Now we loop over the test sets, and then the test cases
for testSet in response:
 thisSet = testSet.FormattedID
 testCases = rally.get('TestCase', fetch="FormattedID,PreConditions,Name,Steps",query="FormattedID = {0}".format(thisSet))
 for testCase in testCases:
  fileName = "{0}-{1}.html".format(thisSet, testCase.FormattedID)
  savedTC = open(fileName, 'w')
  savedTC.write(template.render(tc_name=testCase.Name, steps=testCase.Steps, preconditions=testCase.PreConditions).encode('utf-8', 'ignore'))
  savedTC.close()
  print "{0} saved.".format(fileName)