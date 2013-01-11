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

for i in range(3, int(args[0])):
 query_criteria = 'FormattedID = "%s"' % i
 response = rally.get('TestCase', fetch=True, query=query_criteria)
 if response.errors:
  sys.stdout.write("\n".join(errors))
  sys.exit(1)
 for testCase in response:  # there should only be one qualifying TestCase  
  outString = template.render(tc_name=testCase.Name, steps=testCase.Steps, preconditions=testCase.PreConditions)
  print outString.encode('ascii', 'ignore')
  #fileName = "C:\dev\TC%s" %i
  #savedTC = open(fileName, 'w')
  #savedTC.write(template.render(tc_name=testCase.Name, steps=testCase.Steps, preconditions=testCase.PreConditions))
  #savedTC.close()