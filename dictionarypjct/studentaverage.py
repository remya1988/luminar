if __name__ == '__main__':
    n = int(input(" "))
    student_marks = {}
    for _ in range(n):
        name, *line = input(" ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input(" ")
    avg = 0.0
    for i in range(len(student_marks[query_name])):
        avg = avg + float(student_marks[query_name][i])
    avg_s = avg/3
    print('%.2f' %avg_s)
    # if query_name in student_marks:
    #     x = float(student_marks[query_name][0])+float(student_marks[query_name][1])+float(student_marks[query_name][2])
        #print('%.2f' % x/3)