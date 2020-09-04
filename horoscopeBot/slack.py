from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
import os

interpreter = RasaNLUInterpreter("./models/nlu/default/horoscopebot")
model_path = "./models/dialogue"
action_endpoint = EndpointConfig(url="https://horoscopebot007-actions.herokuapp.com/webhook")
agent = Agent.load(model_path,interpreter=interpreter,action_endpoint=action_endpoint)

input_channel= SlackInput(
	slack_token = "",
	slack_channel="")

s = agent.handle_channels([input_channel],int(os.environ.get('PORT',5004)),serve_forever=True)