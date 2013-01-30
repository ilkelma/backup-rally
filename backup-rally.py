import sys
from pyral import Rally, rallySettings
from jinja2 import Environment, FileSystemLoader
options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]
server, user, password, workspace, project = rallySettings(options)
rally = Rally(server, user, password, workspace=workspace, project=project)
rally.enableLogging('mypyral.log')
env = Environment(loader = FileSystemLoader('.'))
template = env.get_template('testCase.html')

# First we query once to get all Test Cases
response = rally.get('TestCase', fetch=True, query='')
if response.errors:
 sys.stdout.write("\n".join(errors))
 sys.exit(1)
# Now we loop over the test cases
for testCase in response:
 outString = template.render(tc_name=testCase.Name, steps=testCase.Steps, preconditions=testCase.PreConditions)
 fileName = "%s.html" %testCase.FormattedID
 savedTC = open(fileName, 'w')
 savedTC.write(template.render(tc_name=testCase.Name, steps=testCase.Steps, preconditions=testCase.PreConditions).encode('utf-8', 'ignore'))
 savedTC.close()
 print "%s saved." %fileName