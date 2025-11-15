import module

def main():
    locations = ["Airdrie", "Ardrossan", "Banff South of Bow River", "Brooks Meadowplace", "Calgary Varsity", "Caroline", "Cold Lake South", "Conklin Community", "Cougar Point Road, Canmore", "Drayton Valley"]
    old_aq_values = [141, 53, 46, 142, 153, 136, 52, 55, 23, 73]
    new_aq_values = module.air_quality(locations)

    old_mean = module.mean_calculation(old_aq_values)
    new_mean = module.mean_calculation(new_aq_values)

    old_median = module.median_calculation(old_aq_values)
    new_median = module.median_calculation(new_aq_values)

    print(f'The worst locations from the old data are: {module.worst_two(locations, old_aq_values)}')
    print(f'The worst locations from the new data are: {module.worst_two(locations, new_aq_values)}')

    print(f'The percentage for locations with good air quality with the old data is {module.good_locations(old_aq_values)}')
    print(f'The percentage for locations with good air quality with the new data is {module.good_locations(new_aq_values)}')
    
    

main()
