from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core import utils
from rasa_core.agent import Agent
#from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter , RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy
from rasa_core.policies.fallback import FallbackPolicy

import warnings

def train_dialogue():
	utils.configure_colored_logging(loglevel='DEBUG')
	training_data_file = './horoscopeBot/data/stories.md'
	model_path = './horoscopeBot/models/dialogue'

	fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
		core_threshold=0.3,nlu_threshold=0.3)

	agent = Agent('./horoscopeBot/horoscope_domain.yml', policies = [MemoizationPolicy(),KerasPolicy(),SklearnPolicy(),fallback])
	training_data = agent.load_data(training_data_file)
	agent.train(
		training_data,
		augmentation_factor = 50,
		epoch = 500,
		batch_size =10,
		validation_split=0.2
		)

	agent.persist(model_path)
	return agent

def run_horoscope_bot(serve_foerver=True):
	#interpreter = RasaNLUInterpreter('./horoscopeBot/models/nlu/default/horoscopebot')
	interpreter = RasaNLUInterpreter('./models/nlu/default/horoscopebot')
	agent = Agent.load('./models/dialogue',interpreter=interpreter)

	#if serve_foerver:
	#	agent.handle_channel(ConsoleInputChannel())

	return agent

if __name__=='__main__':
	train_dialogue()
	run_horoscope_bot()
