from swarm import Agent
from Agent2.configs.prompts import *
from Agent2.configs.Data.context_variables import *
from Agent2.configs.tools.switchers import *

availability_agent = Agent(
    name="Availability Agent",
    instructions=availability_instructions(context_variables),
    functions=[
        switch_to_cancellation_agent,
        switch_to_reviews_agent,
    ]
)

cancellation_agent = Agent(
    name="Cancellation Agent",
    instructions=cancellation_instructions(context_variables),
    functions=[
        switch_to_availability_agent,
        switch_to_reviews_agent,
    ]
)

reviews_agent = Agent(
    name="Reviews Agent",
    instructions=reviews_instructions(context_variables),
    functions=[]
)

triage_agent = Agent(
    name="Triage Agent",
    instructions=triage_instructions(context_variables),
    functions=[
        switch_to_availability_agent,
        switch_to_cancellation_agent,
        switch_to_reviews_agent,
    ]
)