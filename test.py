from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# res=tavily_search("Best Hotels in Europe for Solo Travelers")
# print(res)

# res=search_flights("Plan a 7 days Japan trip from Bangladesh")
# print(res)

res=run_travel_agent("Plan a 7 days Japan trip from Bangladesh")
print(res)