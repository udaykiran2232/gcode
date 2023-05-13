import subprocess
from datetime import datetime
import os
time =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e.output}")
def execute_command1(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(result)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e.output}")
        return result
new = r"C:\\Users\\UX503010\\Documents\\gcode"
os.chdir(new)
command = "dir /b >> ZZZZZ_uday.txt" 
execute_command(command)
filee = open("C:\\Users\\UX503010\\Documents\\gcode\\ZZZZZ_uday.txt", "r")
file1 = open('C:\\Users\\UX503010\\Documents\\GcodeSuccessFile1.txt', 'a')
file1.write('\n')
file1.write(''+time+'--->process started <---')
file1.write('\n')
file1.write('\n')
a = []
for line in filee:
    line = line.rstrip('\n')
    a.append(line)
filee.close()
x = len(a)
for i in range (x):
    if 'json' in a[i]:
        a1 = 'curl -u gcodeuser:gcodeuser -X POST -F file=@'
        b1 = ' http://author-ins-1a.prod.refinitiv.com:4502/content/dam/myrefinitiv/gcode.createasset.html'
        z = a1 + a[i] + b1
        command = z
        result = execute_command1(command)
        print(""+a[i]+ ' --->**Modified Complted**')
        if 'Modified Resource' in result:
            file1.write(''+time+ '---' + a[i]+ ' --->**Modified Complted**')
            file1.write('\n')
file1.close()
print("&&___Press 1 to close and delete the files____&&")
print("*****---------->Press any KEY to close this Application<---------------*****")
u = input(int(print("enter any number")))
if u == 1:
    folder_path = "C:\\Users\\UX503010\\Documents\\gcode\\"
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            print(os.path.isfile(file_path))
            ax = input(int(print("2")))
            os.remove(file_path)