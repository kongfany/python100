"""
----------------------------------------
    File Name: chengji
    Author: Kong
    Date: 2021/7/12
    Description:
    录入5个学生三门课程的成绩
    计算每门课程的平均分和学生的平均分
    思路：
    三个列表：names，courses，scores（嵌套）

    录入成绩scores:[[1,2,3],[4,5,6]]
    scores[i][j]
    每个人的平均成绩：sum(scores[index])/len(courses)

    每门的平均成绩：创建新列表：curr_courses_scores[score[index] for score in scores]

----------------------------------------
"""
names = ["kong","hhh"]
courses = ["语文","数学","英语"]
scores = [[0]*len(courses) for _ in range(len(names))]

for i,name in enumerate(names):
    print(f"请输入{name}的成绩===>")
    for j,course in enumerate(courses):
        scores[i][j] = float(input(f"{course}: "))
print(scores)
print()
print("每人的平均成绩为：")
for index,name in enumerate(names):
    avg_score = sum(scores[index])/len(courses)
    print(f"{name}的平均成绩为：{avg_score:.1f}")
print()
print("每门的平均成绩为：")
for index,course in enumerate(courses):
    print(index,course)
    curr_courses_scores = [score[index] for score in scores]

    print(curr_courses_scores)
    avg_score = sum(curr_courses_scores)/len(names)
    print(f"{course}的平均成绩为:{avg_score:.1f}")


