programming_dict = {
    "Name": "Uchechukwu Ezeibe",
    "Job": "Software Engineer",
}

# retrieve items using the key
# print(programming_dict["Name"])

#Add new items to the dictionary
programming_dict["State"] = "Anambra State"
# print(programming_dict)

#loop through a dctionary
for key in programming_dict:
    print(key)
    print(programming_dict[key])