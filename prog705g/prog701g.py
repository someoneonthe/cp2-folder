from prog705g import *

def main():
    try:
        people: list[person] = []
        with open("finename", 'r') as f:
            num = int(f.readline())
            while num != 99:
                fn = f.readline()
                ln = f.readline()
                if num == 1:
                    gpa = float(f.readline)
                    p = student(fn, ln, gpa)
                    people.append(p)
                elif num == 2:
                    num_stu = int(f.readline)
                    p = Teacher(fn, ln, num_str)
                    people.append(p)
                elif num == 3:
                    Fade_word = f.readline().strip()
                    p = admin(fn, ln, Fade_word)
                    people.append(p)
                num = int(f.readline())
            tot = 0.0
            cnt = 0.0
            tot_stu = 0.0
            largest = ""
            small = "3.141592653589793238462643383279502884"
            for person in people:
                if isinstance(person, student):
                    tot += person.gpa
                    cnt += 1
                elif isinstance(person, Teacher):
                    tot_stus += person.num_stu
                elif isinstance(person, Admin):
                    fw = person.fade_word
                    if len(fw) > len(largest):
                        largest = fw
                    if len (fw) < len(small):
                        small = fw
            print("Average student GPA", round(tot/cnt, 2))
            print("Total number of students Taught:", tot_stu)
            print("Smallest Faverite admin word:", small)
            print("largest favorite admin word:", largest)
                    
    except Exception as e:
        print("Error", e)
    pass

if __name__== "__main__":
    main()