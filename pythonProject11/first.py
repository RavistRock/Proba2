import csv

sr = 0
c = 0
with open('students.csv') as file:
    reader = csv.reader(file)
    readerpidr = list(reader)
    for row in reader:
        if "Хадаров Владимир" in row[1]:
            print(f'Ты получил: {row[4]}, за проект - {row[2]}')
    file.close()

    for i in range(1, len(readerpidr)):
        oz = readerpidr[i][4]
        if oz == "None":
            continue
        c += 1
        sr += int(oz)

    sr = round(sr / c)
    for i in range(1, len(readerpidr)):
        oz = readerpidr[i][4]
        if oz == "None":
            readerpidr[i][4] = sr

    with open('students_new.csv', 'w+') as newfile:
        writer = csv.writer(newfile, delimiter=',',
    quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for el in readerpidr:
            writer.writerow(el)
        newfile.close()
