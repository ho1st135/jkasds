import csv
sp =['9т', '9г', '8х', '11и', '11в']
summ = [0] * 5
kol = [0] * 5
with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
    print(answer)
    for id, name, title, clas, score in answer:
        if 'Хадаров Владимир' in name:
            print('Ты получил:', score, 'за проект -', title)

    for id, name, title, clas, score in answer:
        if score == 'None':
            print(clas)

    if score != 'None' and (clas in sp):
        i = sp.index(clas)
        summ[i] = summ[i] + int(score)
        kol[i] = kol[i] + 1

    with open('student_new.csv', 'w', newline = '') as file2:
        writer = csv.writer(file2)
        for id, name, title, clas, score:
            if score == 'None':
                i = sp.index(clas)[:-13]
                score = str(summ[i] / kol[i])
            writer.writerow([id, name, title, clas, score])




