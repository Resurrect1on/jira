from jira import JIRA

# jira server + jira user + api TO CHANGE
#itsumivalorant@gmail.com
telegramAPI = 'bot token'
jira_server ='jira url'
jira_user = 'username or email'
key = 'key' 
#AdminAPI = ''
API = 'user token'
jira = JIRA(server=jira_server, basic_auth=(jira_user, API))
jira_projects = [key]

#[for tests]
#new_issue = jira.create_issue(project=key, summary='+1',
#description='+1', issuetype={'name': 'Bug'})
#my_issue = jira.assign_issue(issue='name', assignee=None)
