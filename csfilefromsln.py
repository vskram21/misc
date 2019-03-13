import os
import shutil
import re, configparser, csv, sys

def get_files_from_csproj(csproj_list,source_code_dir):
    files = []
    for csproj in csproj_list:
        csproj_file = open(source_code_dir+csproj,'r')
        path = source_code_dir+csproj
        directory_path = os.path.split(path)[0]+'\\'
        csproj_proj_dir = os.path.split(csproj)[0]+'\\'
        for line in csproj_file:
            if re.findall(r'<Compile Include=', line) == ['<Compile Include=']:
                file_name = line.split('"')[1]
                if (file_name.find('.cs')>=-1):
                    src_file = directory_path+file_name
                    files.append(src_file)
    return files

def get_project_from_sln(sln_file):
    opened_sln = open(sln_file,'r')
    proj = []
    for line in opened_sln:
        if re.findall(r'.csproj', line) == ['.csproj']:
            csproj =  re.sub(r'^"|"','',line.split(',')[1]).lstrip(' ')
            if csproj.find('Tests') == -1 :
                #get_files_from_csproj(csproj)
                #print (csproj)
                proj.append(csproj)
    return proj

def copy_files(src_file, dest_file):
    destfilename = dest_folder+dest_file
    xcopystring = 'xcopy ' + src_file + ' ' + destfilename+ '*'
    print(xcopystring)
    os.system(xcopystring)

#filecp = open("cs-files.txt",'r')
def list_of_cs_files():
    dest_folder = 'D:\\Tools\\Custom\\FileCopy4Checkmarx\\out\\'
    projects = get_project_from_sln(sln_file)
    return get_files_from_csproj(projects, source_code_dir)

def write_to_csv(file, content):
    with open(csv_file, 'w', newline='') as csvfile:
        csvwritter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwritter.writerow(['hello'])


config = configparser.ConfigParser()
config.read('config.conf')
#source_code_dir = sys.argv[1]
#source_sln_file = sys.argv[1]+"\\project.sln"
source_code_dir = config['default']['source_code_dir']
sln_file = config['default']['source_sln_file']
#csv_file = config['default']['csv_file']
excluded_webapis = config['default']['excluded_webapis']
#os.system ("python SQLScanner.py")
#files = get_filepaths(source_code_dir)
#copy_files(files,dest_folder)
