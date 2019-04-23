import re
import os
import sys

class parseXml:
    def parse_xml_hash(self, path):
        fd = open(path, 'r')
        file_name = os.path.basename(path)
        fd_temp = open( './' + file_name + '_1', 'w')
        for line in fd:
            if 'path' in line:
                result = re.search(r'path="(.*?)".*?revision="(.*?)"', line)
            elif ('name' in line) and ('revision' in line):
                result = re.search(r'name="(.*?)".*?revision="(.*?)"', line)
            else:
                continue
            result_line = result.group(1).ljust(80) + result.group(2).ljust(50) + '\n'
            fd_temp.write(result_line)
        fd_temp.close()
        fd.close()
        result = open(file_name + '_1', 'r')
        new = open(file_name + '_2', 'w')
        data = result.readlines()
        data.sort()
        for i in range(len(data)):
            new.write(data[i])
        result.close()
        new.close()
        return file_name + '_2'

    def compare_hash(self, path1, path2):
        fd1 = open(path1, 'r')
        fd2 = open(path2, 'r')
        fd3 = open('./result.txt', 'w')

        data1 = fd1.readlines()
        data2 = fd2.readlines()
        fd1.close()
        fd2.close()

        index1 = 0
        index2 = 0
        while True:
            if index1 == len(data1) or index2 == len(data2):
                break
            if data1[index1] == data2[index2]:
                index1 += 1
                index2 += 1
                continue
            else:
                result1 = data1[index1].split()
                result2 = data2[index2].split()
                if result1[0] == result2[0]:
                    result = result1[0].ljust(60) + result1[1].ljust(42) + result2[1].ljust(42) + '\n'
                    index1 += 1
                    index2 += 1
                    fd3.write(result)
                elif result1[0] > result2[0]:
                    result = result2[0].ljust(60) + "Null".ljust(42) + result2[1].ljust(42) + '\n'
                    index2 += 1
                    fd3.write(result)
                elif result1[0] < result2[0]:
                    result = result1[0].ljust(60) + result1[1].ljust(42) + "Null".ljust(42) + '\n'
                    index1 += 1
                    fd3.write(result)


        while index1 < len(data1):
            result1 = data1[index1].split()
            result = result1[0].ljust(60) + result1[1].ljust(42) + "Null".ljust(42) + '\n'
            fd3.write(result)
            index1 += 1

        while index2 < len(data2):
            result2 = data2[index2].split()
            result = result2[0].ljust(60) + "Null".ljust(42) + result2[1].ljust(42) + '\n'
            fd3.write(result)
            index2 += 1

        fd3.close()
        return 'result.txt'


