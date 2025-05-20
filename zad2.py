def get_grades():
    return [5, 4, "3", 2, 1]

def calculate_average(grades):
    #{
    clean_grades = []
    for g in grades:
        try:
            clean_grades.append(int(g))
        except ValueError:
            continue    #} dodana część która zamienia inne typy na int
    return sum(clean_grades) / len(clean_grades)

def to_word_grade(avg):
    if avg >= 4.5:
        return "bardzo dobry"
    elif avg >= 3.5:
        return "dobry"
    elif avg >= 2.5:
        return "dostateczny"
    else:
        return "niedostateczny"

def show_result():
    grades = get_grades()
    avg = calculate_average(grades)
    word = to_word_grade(avg)
    print(f"Średnia: {avg:.2f}, Ocena: {word}")

show_result()