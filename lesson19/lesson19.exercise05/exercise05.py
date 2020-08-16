from teachers import Teachers
from pupils import Pupils
from lessons import Lessons


def main():

    pupils = Pupils()
    teachers = Teachers()
    lessons = Lessons()

    while True:
        print("\n===============")
        print("     MENU ")

        print("1 - Manage Pupils")
        print("2 - Manage Teachers")
        print("3 - Manage Lessons")
        print("4 - Exit")
        choice = int(input("Pick one: "))

        if choice == 1:
            print("\n===============")
            print(" PUPILS MENU ")

            print("1 - Create Pupil")
            print("2 - Print Pupil(s)")
            print("3 - Update Pupil")
            print("4 - Delete Pupil")
            pupils_choice = int(input("Pick one: "))

            if pupils_choice == 1:
                print("NEW PUPIL")
                print("===========")
                pupil = pupils.create_pupil()
                if pupil is None:
                    continue
                else:
                    print("NEW PUPIL")
                    print(pupil)

            elif pupils_choice == 2:
                print("\n===============")
                print("     SUB-MENU (PRINT) ")
                print("1 - Print Pupil")
                print("2 - Print all pupils (details)")
                print("3 - Print all pupils (just the names)")
                print_choice = input("Give your choice: ")
                if print_choice.strip().isdigit():
                    print_choice = int(print_choice)
                else:
                    print("Wrong input!")
                    continue

                if print_choice == 1:
                    pupil_id = int(input("Give id: "))
                    pupil = pupils.search_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("Pupil does not exist (with this id)")
                    else:
                        print("   PUPIL   ")
                        print(pupil)

                elif print_choice == 2:
                    print(pupils)
                elif print_choice == 3:
                    pupils.print_pupils_names()
                else:
                    print("Wrong input! ")
                    continue

            elif pupils_choice == 3:
                print("\n===============")
                print("     SUB-MENU (UPDATE) ")
                print("1 - Update Pupil (search by id)")
                print("2 - Update Pupil (search by surname)")
                update_choice = input("Give your choice: ")
                if update_choice.strip().isdigit():
                    update_choice = int(update_choice)
                else:
                    print("Wrong input!")
                    continue

                if update_choice == 1:
                    pupil_id = int(input("Give id: "))
                    pupil = pupils.search_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("Error! There is no pupil with this id!")
                        continue
                elif update_choice == 2:
                    surname = input("Give surname: ")
                    matching_pupils = pupils.search_pupil_by_surname(surname)
                    if not matching_pupils:
                        print("No matching pupils with this surname!")
                        continue
                    elif len(matching_pupils) == 1:
                        pupil = matching_pupils[0]
                    else:
                        for p in matching_pupils:
                            print(p)
                            print(f"id = {p['id']}")
                            print("-" * 15)
                        pupil_id = int(input("Give id: "))
                        pupil = pupils.search_pupil_by_id(pupil_id)

                # pupil: update
                pupils.pupil_update(pupil)

            elif pupils_choice  == 4:
                print("\n===============")
                print("     SUB-MENU (DELETE) ")
                print("1 - Delete Pupil (search by id)")
                print("2 - Delete Pupil (search by surname)")
                delete_choice = input("Give your choice: ")
                if delete_choice.strip().isdigit():
                    delete_choice = int(delete_choice)
                else:
                    print("Wrong input!")
                    continue

                if delete_choice == 1:
                    pupil_id = int(input("Give id: "))
                    pupil = pupils.search_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("Error! There is no pupil with this id!")
                        continue
                elif delete_choice == 2:
                    surname = input("Give surname: ")
                    matching_pupils = pupils.search_pupil_by_surname(surname)
                    if not matching_pupils:
                        print("No matching pupils with this surname!")
                        continue
                    elif len(matching_pupils) == 1:
                        pupil = matching_pupils[0]
                    else:
                        for p in matching_pupils:
                            print(p)
                            print(f"id = {p['id']}")
                            print("-" * 15)
                        pupil_id = int(input("Give id: "))
                        pupil = pupils.search_pupil_by_id(pupil_id)

                # pupil: delete
                pupils.delete_pupil_by_id(pupil.pupil_id)

        elif choice == 2:
            print("\n===============")
            print(" TEACHERS MENU ")

            print("1 - Create Teacher")
            print("2 - Print Teacher(s)")
            print("3 - Update Teacher")
            print("4 - Delete Teacher")
            teacher_choice = int(input("Pick one: "))

            if teacher_choice == 1:
                first_name = input("Give name: ")
                surname = input("Give surname: ")
                teachers.create_teacher(first_name, surname)
            elif teacher_choice == 2:
                teacher_id = int(input("Give id: "))
                teacher = teachers.read_teacher(teacher_id)
                if teacher is None:
                    print("No such teacher exists!")
                else:
                    print(teacher)
            elif teacher_choice == 3:
                teacher_id = int(input("Give id: "))
                teachers.update_teacher(teacher_id)
            elif teacher_choice == 4:
                teacher_id = int(input("Give id: "))
                teachers.delete_teacher(teacher_id)

        elif choice == 3:
            print("\n===============")
            print(" LESSONS MENU ")

            print("1 - Create Lesson")
            print("2 - Print Lesson")
            print("3 - Update Lesson")
            print("4 - Delete Lesson")
            lesson_choice = int(input("Pick one: "))

            if lesson_choice == 1:
                lesson_name = input("Give lesson name: ")
                lessons.create_lesson(lesson_name)
            elif lesson_choice == 2:
                lesson_id = int(input("Give id: "))
                lesson = lessons.read_lesson(lesson_id)
                if lesson is None:
                    print("No such lesson exists!")
                else:
                    lesson.print_lesson_details(teachers, pupils)
            elif lesson_choice == 3:
                lesson_id = int(input("Give id: "))
                lessons.update_lesson(lesson_id, teachers, pupils)
            elif lesson_choice == 4:
                lesson_id = int(input("Give id: "))
                lessons.delete_lesson(lesson_id)



        elif choice == 4:
            print("Bye bye!")
            pupils.save_pupils_data()
            teachers.save_teachers_data()
            lessons.save_lessons_data()
            break


main()