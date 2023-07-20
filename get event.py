import requests
from requests.auth import HTTPBasicAuth
import json
import main
import telebot
import time
# URL to change
def get_json() -> str:
    url = 'http://ur website url/rest/api/2/search?jql=assignee=712020:f8ca08c6-395e-4be8-9fdd-cd3b808986ee'

    auth = HTTPBasicAuth(main.jira_user, main.API)

    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
    )
    return response.text

json_str = get_json()
data = json.loads(json_str)
total = data['total']
issues = data['issues']
array = []
old_array = []
new_array = []

def issueArray():
    for i in range(0, len(issues)):
        if issues[i]['key'] not in array:
            array.append(issues[i]['key'])

def printing():
    print(total)
    for i in range(0, len(array)):
        print(i, array[i])
        
def deleteOld():
    for i in range(90, 101):
        new_array.append(array[i])

bot = telebot.TeleBot(main.telegramAPI)
boolean = True
while boolean == True:
    get_json()
    json_str = get_json()
    data = json.loads(json_str)
    total = data['total']
    issues = data['issues']
    issueArray()
    for i in array:
        if i not in old_array:
            bot.send_message(chat_id='858756643',text=('new ticket, ' + str(i) + ' and total are ' + str(total)))
            old_array.append(i)
    if len(array) >= 101:
        deleteOld()
        array = new_array
        old_array = new_array
        new_array = []
    time.sleep(30)