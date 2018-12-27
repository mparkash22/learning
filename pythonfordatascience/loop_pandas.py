import masterdata as md

brics = md.brics

#simple for loop
# for val in brics :
#     print(val)


#iterrows() for printing row and colum
# for lab,row in brics.iterrows() :
#     # print(lab)
#     # print(row)
#     # print(lab + " :" + row["capital"])
#     brics.loc[lab,"name_length"] = len(row["country"])
# print(brics)

# brics["name_length"] = brics["country"].apply(len)
# print(brics)


# Adapt for loop
# for lab, row in md.cars.iterrows() :
#     print(lab +": "+str(row["cars_per_cap"]))
cars=md.cars

# for lab,row in cars.iterrows():
#     cars.loc[lab,"COUNTRY"]= str.upper(row["country"])

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)