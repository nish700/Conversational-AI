import os
from rasa_core.channels.rasa_chat import RasaChatInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

interpreter = RasaNLUInterpreter("./models/nlu/default/horoscopebot")

model_path = "./models/dialogue"
action_endpoint = EndpointConfig(url="https://horoscopebot007-actions.herokuapp.com/webhook")
agent = Agent.load(model_path,interpreter=interpreter,action_endpoint=action_endpoint)

class MyNewInput(RasaChatInput):
	"""docstring for MyNewInput"""
	#def __init__(self, arg):
	#	super(MyNewInput, self).__init__()
	#	self.arg = arg

	def _check_token(self,token):
		if token=="mysecret1234":
			return {"username" :7007}
		else:
			print("failed to check token:{}".format(token))
			return None

input_channel = MyNewInput(url="https://horoscopebot007.herokuapp.com")

s = agent.handle_channels([input_channel],int(os.environ.get('PORT',5004)),serve_forever=True)