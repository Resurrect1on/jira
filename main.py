from jira import JIRA

# jira server + jira user + api TO CHANGE
#itsumivalorant@gmail.com
telegramAPI = '6300338104:AAFE1nbpqX2yU1plMt5B-_PBEGye-gIIzqY'
jira_server ='https://itsumivalorant.atlassian.net/'
jira_user = 'itsumivalorant@gmail.com'
key = 'SB123' 
AdminAPI = 'ATCTT3xFfGN0HJhpnEgZJN2rvpeAjy_1Z8f3U59aDMT_kGDgSqlNwHZbluXfu-OvY00S2oU3-KfveBQD_AT6muQnnadlld-my-gLrbWNmWL-yrc-u-nrk1owctmXSINvhTPCdq8GMLaG-bJL6CR4ntMSLcNQtbXCGPYo_blwpS1GbotojaZZ_Jc=C29E711E'
API = 'ATATT3xFfGF0B62RMV0rAU2DLp4J9tGOCZ_hNN0iwew7EH5F5Whw8Ygst4jh2se-NXRnfRvKxFQTz-v9N5nnoROiqY5gLTDH5j_ZA_bRXkHp_IY_i6TVOhJO1o4ka49jWR90KYcQPb_KDXyY0nzev70MjhVo8hgVLgparhnGeTwch5GsFdgk4zA=6B48D0B4'
jira = JIRA(server=jira_server, basic_auth=(jira_user, API))
jira_projects = [key]

#[for tests]
#new_issue = jira.create_issue(project=key, summary='+1',
#description='+1', issuetype={'name': 'Bug'})
#my_issue = jira.assign_issue(issue='SB123-1', assignee=None)
