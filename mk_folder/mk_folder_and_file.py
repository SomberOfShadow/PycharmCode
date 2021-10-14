import datetime
import os

# abpath = os.path.abspath('.')
# print(abpath)

solution_time = datetime.datetime.now()
year = solution_time.year
month = solution_time.month
day = solution_time.day

year_str = str(year)
month_str = str(month)
day_str = str(day)

# path = os.path.join("C:\MySoftWare\PycharmTest\mk_folder", "\\test_data")
# os.mkdir(path)  # 建立单层目录
# os.makedirs(path)  # 建立多层目录
print(os.path.abspath("."))

'''
# os.path.isfile("test-data")
time_path = year_str + "_" + month_str + "_" + day_str
file_path = "C:\MySoftWare\PycharmTest\mk_folder\\" + time_path + "\\" + time_path + ".txt"
folder_path = os.path.join("C:\MySoftWare\PycharmTest\mk_folder\\", time_path)

folder = os.path.exists(folder_path)
if folder:
    print("Floder already exist!")
    file = os.path.isfile(file_path)
    if file:
        print("File already exist!")
    else:
        print("File not exist, now to create file!")
        open(file_path, 'w')
        isHere =  file = os.path.isfile(file_path)
        if isHere:
            print("Create file success!")
        else:
            print("Create file failure!")
else:
    print("Folder not exist, now to create folder!")
    os.mkdir(folder_path)
    is_folder = os.path.exists(folder_path)
    if is_folder:
        print("Create folder success!")
    else:
        print("Create folder failure, please recreate it !")
'''

