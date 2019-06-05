agenda_items = {
"Office Supplies":5,
"Order deadlines":5,
"Conference proposal":20
}

for item, time in agenda_items():
    print("Can we address " + str(item) + " in " + str(time) + " minutes?")
