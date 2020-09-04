from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import requests

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class SubscribeUser(Action):

	def name(self):
		return 'action_subscribe_user'

	
	def run(self,dispatcher,tracker,domain):
		try:
			subscribe_slot = tracker.get_slot('subscribe')
			subscribe = (tracker.latest_message)['text']
			
			if subscribe=='True':
				response = 'You are successfully subscribed'
			else:
				response = 'You are not subscribed'
			# else:
			# 	response='not subscribed'
		except:
			response = 'subscribed'
			#subscribe = 'not working'

		dispatcher.utter_message(response)
		dispatcher.utter_message(subscribe_slot)
		return [SlotSet('subscribe',subscribe)]

class GetTodaysHoroscope(Action):

	def name(self):
		return 'action_get_todays_horoscope'

	def run(self,dispatcher,tracker,domain):

		try:
			user_horoscope_sign= tracker.get_slot('horoscope_sign')
			base_url = "http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}"
			url = base_url.format(**{'day':'today','sign':user_horoscope_sign})
			res = requests.get(url)
			todays_horoscope = res.json()['horoscope']
			if len(todays_horoscope)>1:
				response = 'Your today''s horoscope is:\n {}.'.format(todays_horoscope)
			else:
				response = 'no response coming'
			#user_horoscope_sign = url
		except:
			response = 'moved to catch block'
			user_horoscope_sign = 'method in catch'


		dispatcher.utter_message(response)
		return [SlotSet('horoscope_sign', user_horoscope_sign)]




class GetHoroscopeSign(Action):



	def get_horoscope_sign(day,month):

		#day = int(day)
		#month = int(month)
		error=''

		if (month == 3 and 21 <= day <= 31) or (month == 4 and 1<= day <=19):
			horoscope_sign='aries'
		elif (month == 4 and 20<= day >= 30) or (month==5 and 1<= day <= 20):
			horoscope_sign = 'taurus'
		elif (month == 5 and 21<= day >= 31) or (month == 6 and 1<= day <=20):
			horoscope_sign = 'gemini'
		elif (month == 6 and 21<= day >= 30) or (month == 7 and 1<= day <=22):
			horoscope_sign= 'cancer'
		elif (month == 7 and 23<= day >= 31) or (month==8 and 1<= day <= 22) :
			horoscope_sign = 'leo'
		elif (month == 8 and 23<= day >= 31) or (month == 9 and 1<= day <=22) :
			horoscope_sign ='virgo'
		elif (month == 9 and 23<= day >= 30) or (month == 10 and 1<= day<= 22):
			horoscope_sign = 'libra'
		elif (month == 10 and 23<= day >= 31) or (month == 11 and 1<= day <= 21):
			horoscope_sign = 'scorpio'
		elif (month == 11 and 22<= day >= 30) or (month == 12 and 1<= day <=21):
			horoscope_sign = 'sagittarius'
		elif (month == 12 and 22<= day >= 31) or (month == 1 and 1<= day <= 19):
			horoscope_sign ='capricorn'
		elif (month == 1 and 20<= day >= 31) or (month == 2 and 28<= day <=18):
			horoscope_sign = 'aquarius'
		elif (month == 2 and 19<= day >= 28) or (month == 3 and 1<= day <=20):
			horoscope_sign ='pisces'
		else:
			error = 'please enter dd-mm in correct calendar format'
			horoscope_sign=''
		
		return horoscope_sign, error


	def name(self):
		return 'action_get_horoscope_sign'

	def run(self,dispatcher,tracker,domain):
		try:			
			user_dob = tracker.get_slot('DOB')
			
		except:
			user_dob = '07-02'

		user_DD = user_dob.split('-')[0]
		user_MM = user_dob.split('-')[1]

		user_horoscope_sign, error = GetHoroscopeSign.get_horoscope_sign(int(user_DD),int(user_MM))

		if not error:
		## to check empty string in python
			dispatcher.utter_message(user_horoscope_sign)
			return [SlotSet('horoscope_sign',user_horoscope_sign)]
		else:
			dispatcher.utter_message(error)
			dispatcher.utter_message('error')