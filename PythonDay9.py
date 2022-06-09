# PythonDay9
# Dictionary  key=value
# {key:value}

programing_dictionary = {
    "bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again"
}

print(programing_dictionary["bug"])
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])

# Student grades List and dictionaries
student_scores = {
    "Raghu": 88,
    "Mounika": 78,
    "Shiny": 99
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)


# Nesting
Capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in dictionary
traval_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"citites_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visited": 34},
}

# Nesting a dictionary in a list
traval_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visited": 12},
    {"country": "Germany",
     "citites_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visited": 34},
]


def add_new_country(country_visited, cities_visited, times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visited"] = times_visited
    traval_log.append(new_country)


add_new_country("Russia", ["london", "Saint", "Petersburg"], 2)
print(traval_log)
