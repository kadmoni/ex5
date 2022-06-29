import json
import os


def names_of_registered_students(input_json_path, course_name):
    with open(input_json_path, 'r') as f:
        loaded_dict = json.load(f)
        students_id = loaded_dict.keys()
        d = [(loaded_dict[id])['student_name'] for id in students_id if course_name in ((loaded_dict[id])['registered_courses'])]
    return d
    pass


def courses_for_lecturers(json_directory_path, output_json_path):
    path_list = [os.path.join(json_directory_path, name) for name in os.listdir(json_directory_path) if name.endswith('.json')]
    lecturers_dict = {}
    for path in path_list:
        with open(path, 'r') as f:
            loaded_dict = json.load(f)
            lecturers_semester_list = []
            for key in loaded_dict.keys():
                for name in loaded_dict[key]["lecturers"]:
                    if name not in lecturers_semester_list:  #lecturers_semester_list?
                        lecturers_semester_list += [name]
                    if name in lecturers_dict:
                        if loaded_dict[key]["course_name"] not in lecturers_dict[name]:
                            lecturers_dict[name] += [loaded_dict[key]["course_name"]] #checks if already has current course
                    else:
                        lecturers_dict[name] = [loaded_dict[key]["course_name"]]
            # lecturers_list += lecturers_semester_list
    # for name in lecturers_dict.keys():
    #     if lecturers_list.count(name) < num_of_semesters:
    #         del lecturers_dict[name]

    # final_dict = {name: lecturers_dict[name] for name in lecturers_dict.keys() if lecturers_list.count(name) == num_of_semesters}
    with open(output_json_path, 'w') as output_file:
        json.dump(lecturers_dict,output_file, indent=4)
    pass


def enrollment_numbers(input_json_file, output_file_path):
    my_courses = {}
    with open(input_json_file, 'r') as input_dict:
        loaded_dict = json.load(input_dict)
        for student_courses in loaded_dict.values():
            for course in student_courses['registered_courses']:
                if course in my_courses:
                    my_courses[course] += 1
                else:
                    my_courses[course] = 1
    with open(output_file_path, 'w') as output_file:
        sorted_names = sorted(my_courses.keys())
        for name in sorted_names:
            output_file.write('"'+name+'"'+' ')
            output_file.write(str(my_courses[name])+'\n')
    pass



