from csv import reader, writer

with open('fighters.csv') as file:
    csv_reader = reader(file)
    num = 1

    with open('screaming_fighters.csv', "w") as file:
        csv_writer = writer(file)
        print(num)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])