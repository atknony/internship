# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).

r_time = int(input("enter total race time in seconds: "))
pitstops = int(input("enter how many pit stops were made: "))
average_ps_duration = int(input("enter the average pit stop duration: "))


# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.

total_pt = pitstops * average_ps_duration
percentage_pt = total_pt * 100 / r_time
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

print(f'total pit stop time in seconds: {total_pt}s')
print(f'percentage of race time spent in pits: {percentage_pt}%')
if percentage_pt >= 5 :
    print("You need a new pit crew. 🛠️")