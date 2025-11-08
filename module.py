import statistics

air_quality_table = [141, 53, 46, 142, 153, 136, 52, 55, 23, 73, 75, 50, 73, 9, 28, 13, 79, 73, 65, 157, 62, 139, 63, 18, 98, 19, 58, 68, 131, 148, 155, 153, 78, 111, 151, 117, 60, 159, 88, 40, 79, 14, 146, 74]

# function that returns the mean from any length list of numerical data
def mean_calculation(int: air_quality_table) -> int:
    mean = sum(air_quality_table) / len(air_quality_table)
    print(mean)

# A function that returns the median from any length list of numerical data.
def median_calculation(int: air_quality_table) -> int:
    median = statistics.median(air_quality_table)
    print(median)

# A function that when passed a list of locations: 

# a) asks the user to enter the current air quality for each location, 
# b) adds that numerical value to a list, and then 
# c) returns a list of those entered values.

def air_quality(locations):
    air_quality_values = []
    
    for location in locations:
        while True:
            try:
                current_air_quality = float(input(f"Enter the current air quality for {location}: "))
                air_quality_values.append(current_air_quality)
                break
            except ValueError:
                print("Enter a valid air quality number.")
                
    return air_quality_values


#A function that when passed a list of numbers and a parallel list of locations, returns a list of the names of the two locations with the worst (highest) values.



#A function that when passed a list of numbers, tallies the number of items that would qualify as ‘Good’ (i.e. <= 50) and returns that tally as a percentage of data locations.

