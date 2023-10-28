def get_states_set(states: list) -> set:
    states_needed = set()
    for stations in radio_stations.values():
        for state in stations:
            states_needed.add(state)
    return states_needed


radio_stations = {
    'kone':['ID','NV','UT'],
    'ktwo':['WA','ID','MT'],
    'kthree':['OR','NV','CA'],
    'kfour':['NV','UT'],
    'kfive':['CA','AZ']
}
final_stations_list = []
states_needed = get_states_set(radio_stations)
max_coverage = 0
station_candidate = ''
while len(states_needed) > 0:
    for station, coverage in radio_stations.items():
        if len(coverage) >= max_coverage and station not in final_stations_list:
            max_coverage = len(coverage)
            station_candidate = station
    final_stations_list.append(station_candidate)
    for station in radio_stations.get(station_candidate):
        states_needed.discard(station)
    max_coverage = 0
    station_candidate = ''
print(final_stations_list)
   

