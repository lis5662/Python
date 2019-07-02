midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

# final_grades = {'dan': 98, 'ang': 91, 'kate': 78}

# final_grades = [max(pair) for pair in zip(midterms, finals)]

# final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}


final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)
print(final_grades)