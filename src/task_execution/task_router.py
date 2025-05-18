from .weather_task import get_weather
from .time_task import get_time
from .date_task import get_date
from .name_task import get_name
from .created_task import get_created
from .general_task import get_general_response

def route_task(intent, user_input):
    if intent == 'weather':
        return get_weather(user_input)
    elif intent == 'time':
        return get_time()
    elif intent == 'date':
        return get_date()
    elif intent == 'name':
        return get_name()
    elif intent == 'created':
        return get_created()
    else:
        return get_general_response(user_input)
