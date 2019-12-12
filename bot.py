import requests 
import misc
import json
token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'



def getUpdates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()


def get_massage():
	data = getUpdates()
	chat_id = data['result'][-1]['message']['chat']["id"]
	message_text = data['result'][-1]['message']['text']	
	update_id = data['result'][-1]['update_id'] 
	return chat_id, message_text, update_id


def sendMessage(id):
	if id == 2:
		message_text1 = 'Now you see thats work ' + get_massage()[1].title() + ', how are you?'
	else:
		message_text1 = 'Hi ' + get_massage()[1].title() + ', how are you?'
	url1 = URL + 'sendmessage' + '?chat_id=' + str(get_massage()[0]) + '&text=' + str(message_text1) 
	requests.get(url1)


def main():
	update_id2 = 0
	booll  = True
	while booll:
		get_massage()
		if  get_massage()[2] != update_id2:
			update_id2 = get_massage()[2]
			sendMessage(1)
			if get_massage()[1] == 'End':
				booll = False
			elif get_massage()[1] == '/stats':
				id = 2
				sendMessage(id)
		






if __name__ == '__main__':
	main()