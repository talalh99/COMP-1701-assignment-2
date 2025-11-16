import statistics

air_quality_table = [141, 53, 46, 142, 153, 136, 52, 55, 23, 73]

# function that returns the mean from any length list of numerical data
def mean_calculation(air_quality_table) -> float:
    mean = sum(air_quality_table) / len(air_quality_table)
    print(f"The Mean value is: {mean}")
    
mean_calculation(air_quality_table)

# A function that returns the median from any length list of numerical data.
def median_calculation(air_quality_table) -> int:
    median = statistics.median(air_quality_table)
    print(f"The Median value is: {median}")
    
median_calculation(air_quality_table)

# A function that when passed a list of locations: 

# a) asks the user to enter the current air quality for each location, 
# b) adds that numerical value to a list, and then 
# c) returns a list of those entered values.

def air_quality(locations):
    air_quality_values = []
           
    for location in locations:
        while True:
            current_air_quality = int(input(f"Enter the current air quality for {location}: ")) 
            if current_air_quality > 0:
                air_quality_values.append(current_air_quality)
                break
            else:
                print("Enter a valid air quality number.")
                    
    return air_quality_values

locations = ["Airdrie", "Ardrossan", "Banff South of Bow River", "Brooks Meadowplace", "Calgary Varsity", "Caroline", "Cold Lake South", "Conklin Community", "Cougar Point Road, Canmore", "Drayton Valley"]
 
#A function that when passed a list of numbers and a parallel list of locations, returns a list of the names of the two locations with the worst (highest) values.

def worst_two(locations, values) -> None:
    worst_index = 0
    second_worst_index = 1

    if values[0] < values[1]:
        worst_index = 1
        second_worst_index = 0

    i = 0
    while i < len(values):
        if values[i] > values[worst_index]:
            worst_index = i

        elif values[i] > values[second_worst_index]:
            second_worst_index = i
        
        i+=1

    return(locations[worst_index], locations[second_worst_index])

#A function that when passed a list of numbers, tallies the number of items that would qualify as ‘Good’ (i.e. <= 50) and returns that tally as a percentage of data locations.

def good_locations(values) -> None:
    good_counter = 0
    i = 0
    while i < len(values):
        if values[i] <= 50:
            good_counter +=1
        i+=1
    good_percentage = (good_counter/len(values))*100
    return good_percentage
    
    