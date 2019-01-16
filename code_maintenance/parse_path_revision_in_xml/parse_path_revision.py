import re
import sys
xml_name=sys.argv[1]
file_name="temp/temp.txt"
fd = open(xml_name, "r")
result = open(file_name, "w")
for line in fd:
    if "path" in line:
        result_info = re.search(r'path="(.*?)".*?revision="(.*?)"', line)
        #path_name = re.findall(r'path="(.*?)"', line)
        #commit_info = re.findall(r'revision="(.*?)"', line)
    elif ( "name" in line ) and ( "revision" in line ):
        result_info = re.search(r'name="(.*?)".*?revision="(.*?)"', line)
        #path_name = re.findall(r'name="(.*?)"', line)
        #commit_info = re.findall(r'revision="(.*?)"', line)
    else:
        continue
    #result_line=path_name[0].ljust(50) + commit_info[0].ljust(30) + "\n"
    result_line=result_info.group(1).ljust(80) + result_info.group(2).ljust(30) + "\n"
    result.write(result_line)

result = open(file_name, "r")
new=open("path_revision.txt","w")
data=result.readlines()
data.sort()
for i in range(len(data)):
    new.write(data[i])

fd.close()
result.close()
new.close()



