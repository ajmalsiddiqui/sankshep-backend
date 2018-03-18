'''
The translation API, using another translation API xD
'''

import requests
import json

base_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
yandex_key = 'trnsl.1.1.20180317T192045Z.366bb2591fccbee9.a9f835d48c27d733810b23a42f50792373badf2a'

def translateSummary(toLang, text):
	params = {
		'text': text,
		'lang': 'en-' + toLang,
		'key': yandex_key
	}
	res = requests.get(base_url, params=params)
	# print(json.loads(res.text)['text'][0])
	return json.loads(res.text)['text'][0]

if __name__ == "__main__":
	text = '''
	I have also used Raspberry Pis as home security cameras, server monitoring devices, cheap headless machines (basically running low-weight scripts 24/7 with a low cost-to-me)... others have used them for media centers and even for voice-enabled IoT devices. The possibilities are endless, but first we need to get acquainted!

	If you do not already have a Raspberry Pi, you can buy one here, or in a variety of other locations.

	Beyond the Raspberry Pi, it can be wise, but not required, to get a case. Make sure that, if you do get a case, it has openings for the GPIO pins to be connected, otherwise you're ruining all of the fun. You will also need a 1000mA+ mini usb power supply and at least an 8GB micro SD card, but I would suggest a 16 GB micro SD card or greater.

	You will also want to have a spare monitor (HDMI), keyboard, and mouse handy to make things easier when first setting up. You wont will eventually be able to control your Pi remotely, so you wont always need a separate keyboard, mouse, and monitor. If you don't have a monitor with HDMI input, you can buy something like an HDMI to DVI converter.

	This is all assuming you're going to be using a Raspberry Pi 3 Model B. If you're using an older version board, please see what you might need to change, for example, the older Rasbperry Pis take a full-sized SD card, but the latest model requires a micro SD card. Also, the Raspberry Pi 3 Model B has built-in wifi, where the older models will require a wifi dongle.
	'''
	translate('hi', text)