## story_001
* greeting
	- utter_greet
* get_horoscope
	- utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign":"Capricorn"}
	- slot{"horoscope_sign":"Aries"}
	- action_get_todays_horoscope
	- utter_subscribe
	[comment]:<> (property names to be enclosed within double quotes)

## story_002
* greeting
	- utter_greet
* get_horoscope{"horoscope_sign":"Capricorn"}
	- slot{"horoscope_sign":"Aries"}
	- action_get_todays_horoscope
	- utter_subscribe
* subscription
	- slot{"subscribe":"True"}
	- action_subscribe_user

## Horoscope query with horoscope sign
* greeting
	- utter_greet
* get_horoscope
	- utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign":"capricorn"}
	- slot{"horoscope_sign":"aries"}
	- action_get_todays_horoscope
	- slot{"horoscope_sign":"capricorn"}
	- utter_subscribe
* subscription{"subscribe":"True"}
	- slot{"subscribe":"True"}
	- action_subscribe_user
	- slot{"subscribe":"true"}

## Horoscope with sign provided
* greeting
	- utter_greet
* get_horoscope{"horoscope_sign":"leo"}
	- slot{"horoscope_sign":"leo"}
	- action_get_todays_horoscope
	- slot{"horoscope_sign":"leo"}
	- utter_subscribe
* subscription{"subscribe":"True"}
	- slot{"subscribe":"True"}
	- action_subscribe_user
	- slot{"subscribe":"true"}
	[comment]:<> (slot{to be included within double quotes and not single quotes})

## When user direclty asks for subscription
* greeting
	- utter_greet
* subscription{"subscribe":"True"}
	- slot{"subscribe":"True"}
	- action_subscribe_user
	- slot{"subscribe":"true"}

## When user does not know horoscope sign
* greeting
	- utter_greet
* get_horoscope
	- utter_ask_horoscope_sign
	- slot{"DOB":"07-02"}
    - slot{"DD":"07"}
    - slot{"MM":"02"}
* get_horoscope_sign
	- utter_ask_dob
	- slot{"DOB":"07-02"}
	- slot{"DD":"07"}
	- slot{"MM":"02"}
	- action_get_horoscope_sign
	- slot{"horoscope_sign":"aries"}
	[comment]:<> (slot("horoscope_sign":"aries"))
* get_horoscope{"horoscope_sign":"aries"}
	- slot{"horoscope_sign":"aries"}
	- action_get_todays_horoscope
	- slot{"horoscope_sign":"aries"}
	- utter_subscribe
* subscription{"subscribe":"True"}
	- slot{"subscribe":"True"}
	- action_subscribe_user
	- slot{"subscribe":"True"}

## Generated Story -5109906386645565592
* greeting
    - utter_greet
* get_horoscope
    - utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign": "aries"}
    - slot{"horoscope_sign": "aries"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aries"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story 8001011182166438865
* dob_intent
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "aquarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aquarius"}
    - utter_subscribe
* subscription
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye


## Generated Story 7034530185890658337
* subscription
    - action_subscribe_user
    - slot{"subscribe": true}

## Generated Story -221160294571154248
* greeting
    - utter_greet
* get_horoscope{"horoscope_sign": "aries"}
    - slot{"horoscope_sign": "aries"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aries"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": true}
* goodbye
    - utter_subscribe

## Generated Story -8067098937009334662
* greeting
    - utter_greet
* get_horoscope
    - utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign": "scorpio"}
    - slot{"horoscope_sign": "scorpio"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "scorpio"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": null}

## Generated Story -7703620037940469203
* greeting
    - utter_greet
* dob_intent{"DOB": "07-12"}
    - slot{"DOB": "07-12"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "sagittarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "sagittarius"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": null}
    - utter_goodbye

## Generated Story 5641578713244641342
* dob_intent{"DOB": "07-05"}
    - slot{"DOB": "07-05"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "taurus"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "taurus"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story 8157035652049757174
* subscription
    - utter_subscribe
* subscription
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story -2247809303288700297
* dob_intent{"DOB": "07-12"}
    - slot{"DOB": "07-12"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "sagittarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "sagittarius"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": "False"}
    - utter_goodbye

## Generated Story -5677472435161207794
* dob_intent{"DOB": "12-07"}
    - slot{"DOB": "12-07"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "cancer"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "cancer"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": "True"}
* dob_intent{"DOB": "07-12"}
    - slot{"DOB": "07-12"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "sagittarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "sagittarius"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": "True"}

## Generated Story -7938761920373494610
* dob_intent{"DOB": "31-4"}
    - slot{"DOB": "31-4"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "taurus"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "taurus"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": "False"}
* dob_intent{"DOB": "40-2"}
    - slot{"DOB": "40-2"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "pisces"}

## Generated Story 6178764177099250937
* dob_intent{"DOB": "32-3"}
    - slot{"DOB": "32-3"}
    - action_get_horoscope_sign
* dob_intent{"DOB": "31-3"}
    - slot{"DOB": "31-3"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "aries"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aries"}
    - utter_subscribe
* None
    - action_subscribe_user
    - slot{"subscribe": "False"}

## Generated Story -403595487787163988
* greeting
    - utter_greet
* get_horoscope{"horoscope_sign": "aries"}
    - slot{"horoscope_sign": "aries"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aries"}
    - utter_subscribe
* subscription{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}

## Generated Story 2201080384494501451
* greeting{"DOB": "hi"}
    - slot{"DOB": "hi"}
    - utter_greet
* subscription
    - utter_subscribe
* subscription{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story -5669772545678379837
* greeting
    - utter_greet
* get_horoscope
    - utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign": "scorpio"}
    - slot{"horoscope_sign": "scorpio"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "scorpio"}
    - utter_subscribe
* None{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story 821485095902072346
* greeting{"DOB": "hi"}
    - slot{"DOB": "hi"}
    - utter_greet
* dob_intent{"DOB": "07-12"}
    - slot{"DOB": "07-12"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "sagittarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "sagittarius"}
    - utter_subscribe
* None{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story 2580670916580720760
* dob_intent{"DOB": "07-03"}
    - slot{"DOB": "07-03"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "pisces"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "pisces"}
    - utter_subscribe
* None{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}

## Generated Story 2218777027071830305
* greeting{"DOB": "hi"}
    - slot{"DOB": "hi"}
    - utter_greet
* dob_intent{"DOB": "07-02"}
    - slot{"DOB": "07-02"}
    - action_get_horoscope_sign
* dob_intent{"DOB": "07-03"}
    - slot{"DOB": "07-03"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "pisces"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "pisces"}
    - utter_subscribe
* None{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}

## Generated Story 5520919882585737447
* dob_intent{"DOB": "07-02"}
    - slot{"DOB": "07-02"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "aquarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aquarius"}
    - utter_subscribe
* None{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story 4804247990371695099
* greeting{"DOB": "hi"}
    - slot{"DOB": "hi"}
    - utter_greet
* dob_intent{"DOB": "07-02"}
    - slot{"DOB": "07-02"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "aquarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aquarius"}
    - utter_subscribe
* None{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story -8507388989584221724
* greeting{"DOB": "hi"}
    - slot{"DOB": "hi"}
    - utter_greet
* get_horoscope
    - utter_ask_horoscope_sign
* dob_intent{"DOB": "07-02"}
    - slot{"DOB": "07-02"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "aquarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aquarius"}
    - utter_subscribe
* None{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story 3578744223947593548
* greeting{"DOB": "hi"}
    - slot{"DOB": "hi"}
    - utter_greet
* dob_intent{"DOB": "07-02"}
    - slot{"DOB": "07-02"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "aquarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aquarius"}
    - utter_subscribe
* None{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}
* goodbye
    - utter_goodbye

## Generated Story 5467351937375270137
* greeting{"DOB": "hi"}
    - slot{"DOB": "hi"}
    - utter_greet
* dob_intent{"DOB": "07-02"}
    - slot{"DOB": "07-02"}
    - action_get_horoscope_sign
    - slot{"horoscope_sign": "aquarius"}
    - action_get_todays_horoscope
    - slot{"horoscope_sign": "aquarius"}
    - utter_subscribe
* None{"DOB": "True"}
    - slot{"DOB": "True"}
    - action_subscribe_user
    - slot{"subscribe": "True"}

