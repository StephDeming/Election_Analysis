counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=="Denver":
    print(counties[1])
if counties[3]="Jefferson":
    print(counties[2])
for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters")      
#skill drill 3.2.10
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)










































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































