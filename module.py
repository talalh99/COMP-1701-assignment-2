import statistics

air_quality_table = [141, 53, 46, 142, 153, 136, 52, 55, 23, 73]

# function that returns the mean from any length list of numerical data
def mean_calculation(air_quality_table) -> int:
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
get_air_quality = air_quality(locations)
print(f"The air quality values are: {get_air_quality}")
 

#A function that when passed a list of numbers and a parallel list of locations, returns a list of the names of the two locations with the worst (highest) values.



#A function that when passed a list of numbers, tallies the number of items that would qualify as ‘Good’ (i.e. <= 50) and returns that tally as a percentage of data locations.

