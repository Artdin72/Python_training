# Средние баллы учеников
grades = [[5,3,3,5,4], [2,2,2,3],[4,5,5,2], [4,4,3],[5,5,5,4,5]] #оценки учеников
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'} #имена учеников
students_list = list(students) #преобразую множество в список
students_list.sort() #сортирую список по алфавиту
grades_mid = [round(sum(grades[0])/len(grades[0]),2), round(sum(grades[1])/len(grades[1]),2), round(sum(grades[2])/len(grades[2]),2), round(sum(grades[3])/len(grades[3]),2),round(sum(grades[4])/len(grades[4]),2)] #считаю средний бал
middle_grades = {} #создаю пустой словарь
middle_grades[students_list[0]] = grades_mid[0] #добавляю в словарь ученика с его средней оценкой
middle_grades[students_list[1]] = grades_mid[1] #добавляю в словарь ученика с его средней оценкой
middle_grades[students_list[2]] = grades_mid[2] #добавляю в словарь ученика с его средней оценкой
middle_grades[students_list[3]] = grades_mid[3] #добавляю в словарь ученика с его средней оценкой
middle_grades[students_list[4]] = grades_mid[4] #добавляю в словарь ученика с его средней оценкой
print(middle_grades) #вывожу итоговый результат
