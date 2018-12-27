from pyson import PySON

#
# Create a new empty object
#
obj = PySON()

# Add a member
obj.addMember("Name", "Tony")

#Add a PySON class member
obj.addClass("items")
obj.items.addMember("wallet", "$100")

obj.dump()
print(obj.toJSON())
