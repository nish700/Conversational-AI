from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
import os


interpreter = RasaNLUInterpreter("./models/nlu/default/horoscopebot")
model_path = "./models/dialogue"
action_endpoint = EndpointConfig("https://horoscopebot007-actions.herokuapp.com/webhook")

agent = Agent.load(model_path,interpreter = interpreter)

input_channel = FacebookInput(
	fb_verify="",
	fb_secret ="",
	fb_access_token = "")

s = agent.handle_channels([input_channel],int(os.environ.get('PORT',5004)),serve_forever= True)