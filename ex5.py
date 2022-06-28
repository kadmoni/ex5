import json
import os


def names_of_registered_students(input_json_path, course_name):
    with open(input_json_path, 'r') as f:
        loaded_dict = json.load(f)
        list_tz = loaded_dict.values()
        d = [(loaded_dict[elem])['student_name'] for elem in list_tz if course_name in ((loaded_dict[elem])['registered_courses'])]
    return d
    pass


def courses_for_lecturers(json_directory_path, output_json_path):
    path_list = [os.path.join(json_directory_path, name) for name in os.listdir(json_directory_path) if name.endswith('.json')]
    num_of_semesters = path_list.len()
    lecturers_dict = {}
    lecturers_list = []
    for path in path_list:
        with open(path, 'r') as f:
            loaded_dict = json.load(f)
            lecturers_semester_list = []
            for key in loaded_dict.keys():
                for name in loaded_dict[key]["lecturers"]:
                    if name not in lecturers_list:
                        lecturers_semester_list += [name]
                    if name in lecturers_dict:
                        lecturers_dict[name] += [loaded_dict[key]["course_name"]]
                    else:
                        lecturers_dict[name] = [loaded_dict[key]["course_name"]]
            lecturers_list += lecturers_semester_list
    for name in lecturers_dict.keys():
        if lecturers_list.count(name) < num_of_semesters:
            del lecturers_dict[name]
    with open(output_json_path, 'w') as output_file:
        json.dump(lecturers_dict,output_file, indent=4)


def enrollment_numbers(input_json_file, output_file_path):
    my_courses = {}
    with open(input_json_file, 'r') as input_dict:
        loaded_dict = json.load(input_dict)
        for course in loaded_dict.values()['registered_courses']:
            if course in my_courses:
                my_courses[course] += 1
            else:
                my_courses[course] = 1
    with open(output_file_path, 'w') as output_file:
        sorted_names = sorted(my_courses.keys())
        for name in sorted_names:
            output_file.write('"'+name+'"'+' ')
            output_file.write(str(my_courses[name])+'\n')



