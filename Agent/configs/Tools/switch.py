#from configs.Agents.TypesAg import *

def switch_main_ag():
    from configs.Agents.TypesAg import main_Agent
    return main_Agent

def switch_change_ag():
    from configs.Agents.TypesAg import change_Agent
    return change_Agent

def switch_cancel_ag():
    from configs.Agents.TypesAg import cancel_Agent
    return cancel_Agent