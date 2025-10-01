from swarm import Agent
from Agent.configs.Agents.prompts import *
from Agent.configs.Agents.Data.context_variables import *
from Agent.configs.Agents.Data.BDAg import *
from Agent.configs.Tools.switch import *


main_Agent = Agent(
    name = "Principal Agent",
    instructions= principal_inst(context_variables),
    functions= [
        switch_change_ag,
        switch_cancel_ag,
        consultar_hoteles,
        consultar_restaurantes,
        consultar_atracciones,
        consultar_autos,
        consultar_transportes
     
    ]
    
)

change_Agent = Agent(
    name = "Change Agent",
    instructions= change_inst(context_variables),
    functions= [
        switch_main_ag,
        switch_cancel_ag
 
    ]
    
)

cancel_Agent = Agent(
    name = "Cancel Agent",
    instructions= Cancel_inst(context_variables),
    functions= [
        switch_main_ag,
        switch_change_ag,
    ]
    
)

triage_agent = Agent(
    name = "Main Agent",
    instructions= triage_inst(context_variables),
    functions= [
        switch_main_ag,
        switch_change_ag,
        switch_cancel_ag
    ]
)