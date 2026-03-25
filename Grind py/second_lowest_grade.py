def main():
    students = []

    # number of students
    n = int(input("Enter number of students: "))

    # input name and score
    for _ in range(n):
        name = input("Enter name: ")
        score = float(input("Enter score: "))
        students.append([name, score])

    # collect all scores
    scores = []
    for st in students:
        scores.append(st[1])

    # remove duplicates and sort
    unique_scores = sorted(set(scores))

    # check if second lowest exists
    if len(unique_scores) < 2:
        print("Second lowest score does not exist")
        return

    second_lowest = unique_scores[1]

    # find students with second lowest score
    result = []
    for st in students:
        if st[1] == second_lowest:
            result.append(st[0])

    # sort names alphabetically
    result.sort()

    # print output
    print("\nStudents with second lowest score:")
    for name in result:
        print(name)


# program start
if __name__ == '__main__':
    main()
