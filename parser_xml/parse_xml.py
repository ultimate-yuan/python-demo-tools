import re
import sys
xml_name=sys.argv[1]
file_name="result.txt"
fd = open(xml_name, "r")
result = open(file_name, "w")
for line in fd:
    if "path" in line:
        path_name = re.findall(r'path="(.*?)"', line)
        commit_info = re.findall(r'revision="(.*?)"', line)
        upstream = re.findall(r'upstream="(.*?)"', line)
        #upstream = re.findall(r'upstream="refs/heads/(.*?)"', line)
    elif ( "name" in line ) and ( "revision" in line ):
        path_name = re.findall(r'name="(.*?)"', line)
        commit_info = re.findall(r'revision="(.*?)"', line)
        upstream = re.findall(r'upstream="(.*?)"', line)
        #upstream = re.findall(r'upstream="refs/heads/(.*?)"', line)
    else:
        continue
    #print(upstream)
    #result_line="path=" + path_name[0] + " revision=" + commit_info[0] + "\n"
    #result_line="cd -; cd " + path_name[0] + "; git push openlinux " + upstream[0] +"\n"
    result_line="cd -; cd " + path_name[0] + "; git checkout -t remotes/amlogic/" + upstream[0] + "; git push openlinux " + upstream[0] +"\n"
    result.write(result_line)

result = open(file_name, "r")
new=open("new.txt","w")
data=result.readlines()
data.sort()
for i in range(len(data)):
    new.write(data[i])

fd.close()
result.close()
new.close()



