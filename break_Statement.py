roll = ["hi","bye"]
name = ["mun", 'mahi', 'mukta', 'sumu']

for item in roll:
    for names in name:
        print(item, names)
        if item == 'hi' and names == "mun":
            break
        elif item == "bye" and names == "mun":
            break


