from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter

def train_horoscopebot(data_json, config_file,model_dir):
	training_data = load_data(data_json)
	trainer = Trainer(config.load(config_file))
	trainer.train(training_data)
	model_directory= trainer.persist(model_dir,fixed_model_name='horoscopebot')


def predict_intent(text):
	interpreter = Interpreter.load('models/nlu/default/horoscopebot')
	print(interpreter.parse(text))


train_horoscopebot('data/data.json','./config.json','C:/python3.6_64/chatbot/horoscopeBot/models/nlu')
## ( path of data.json --> relative to run directory)
##( path of config.json --> relative to run directory)
##( path of models --> relative to c drive , so complete path to be mentioned)
predict_intent('I am looking for my horoscope for today. I am wondering if you can tell me that.')
predict_intent('my birth day is 07-02-1983 , what is my horoscope for today?')
predict_intent('My sign is Scorpio , how will be my day?')
predict_intent('Hello , how are you?')
predict_intent('Please subscribe me')
predict_intent('my sign is aries')
predict_intent('what is my horoscope today')
predict_intent('goodbye')
predict_intent('07-02')
predict_intent('02-12')
predict_intent('12-01')
predict_intent('aries')