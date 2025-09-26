from Agent2.configs.agents.types import *

def switch_to_availability_agent():
    from Agent2.configs.agents.types import availability_agent
    return availability_agent

def switch_to_cancellation_agent():
    from Agent2.configs.agents.types import cancellation_agent
    return cancellation_agent

def switch_to_reviews_agent():
    from Agent2.configs.agents.types import reviews_agent
    return reviews_agent