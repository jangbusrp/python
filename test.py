#print("hello")
a = [1, 2, 4, {"one":[5,6, {"two":{"address": "Kathmandu"}}]}]

print(a[3].get("one")[2].get("two").get("address"))

b = {"student": 
		[
			{
			"id":1,
			"name" : "Hari", 
			"parents":
					[
						{"relation": "father", "name": "Ram"}, 
						{"relation": "mother", "name": "Sita"},
					],
			},
		]
	}

print(b.get("student")[0].get("parents")[0].get("name"))
print(b.get("student")[0].get("parents")[1].get("name"))


# for n in b:
#     	print(n.get("student","parents")[0])

# fetch name of father and mother

