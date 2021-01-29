import os


# we can create another file for each project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating directory for now ' + directory)
        os.makedirs(directory)


# create queue and final crawled files (by some if) :)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    FinalCrawled = os.path.join(project_name,"FinalCrawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(FinalCrawled):
        write_file(FinalCrawled, '')


# create a new file :)
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)



# add data onto my file by append method
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# delete the contents of a file by write mode
def delete_file_contents(path):
    open(path, 'w').close()


# Top the best solution every files are convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# through a set, convert set to file by iterative 
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")
