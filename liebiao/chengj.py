"""
----------------------------------------
    File Name: chengj
    Author: Kong
    Date: 2021/7/11
    Description: 录入5个学生3门课程的考试成绩
    计算每个学生的平均分和每门课的平均分
----------------------------------------
"""
names = ["关羽","张飞","赵云","马超","黄忠"]
courses = ["语文","数学","英语"]
scores = [[0]*len(courses) for _ in range(len(names))]

for i,name in enumerate(names):
    print(f"请输入{name}的成绩 ===>")
    for j,course in enumerate(courses):
        scores[i][j] = float(input(f"{course}:"))
print()
print(scores)
print("-"*5,"学生平均成绩","-"*5)

for index,name in enumerate(names):
    avg_score = sum(scores[index])/len(courses)
    print(f"{name}的平均成绩为：{avg_score:.1f}分")
print()

print("-"*5,"课程平均成绩","-"*5)
for index,course in enumerate(courses):
    curr_course_scores = [score[index] for score in scores]
    print(curr_course_scores)
    avg_score = sum(curr_course_scores)/len(names)
    print(f"{course}的平均成绩为：{avg_score:.1f}分")