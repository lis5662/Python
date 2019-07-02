# The following list of cities has come some duplicate data
cities = {'Los Angeles', 'Florence', 'Boulder', 'Oslo', 'Tokyo', 'Santiago', 'Kyoto', 'San Francisco', 'Shanghai'}
# To count unique cities:
print(len(set(cities)))

# convert from list -> set -> list to get a list of uniques
print(list(set(cities)))


# Suppose I teach two classes:
math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

# To generate a set with all my unique students
print(math_students | biology_students)

# To generate a set with students who  are in both courses
print(math_students & biology_students)