f = open("../Python_file_json/file.txt",'w')

f.write("테스트 입력")

f.close()


with open("../Python_file_json/file.txt",'a') as f:
    f.write("두번째 테스트")


with open("../Python_file_json/file.txt",'r') as f:
    print(f.readline())
