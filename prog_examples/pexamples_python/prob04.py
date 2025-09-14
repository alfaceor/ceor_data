#!/usr/bin/env python
import statistics
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks.keys():
        value = statistics.mean(student_marks[query_name])
        print("{0:.2f}".format(value))
    # print(student_marks)
