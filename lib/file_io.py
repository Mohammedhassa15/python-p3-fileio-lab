def write_file(file_name, file_content):
    employee_file=open(file_name.with_suffix(".txt"), "w")
    employee_file.write(file_content)

    employee_file.close()

def append_file(file_name, append_content):
    employee_file=open(file_name.with_suffix(".txt"), "a")
    employee_file.write(append_content)

    employee_file.close()

def read_file(file_name):
    employee_file=open(file_name.with_suffix(".txt"), "r")
    content=employee_file.read()
    return content 


    employee_file.close()