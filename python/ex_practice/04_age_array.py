people = [
    {"name": "noah","age":19},
    {"name": "liam","age":23},
    {"name": "jacob","age":9},
    {"name": "mason","age":21},
]
people_chan=sorted(people,key=lambda person: person["age"])

print(people_chan)
