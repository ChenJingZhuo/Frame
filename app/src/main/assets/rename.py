# # 遍历文件夹
# def walkFile(file):
#     for root, dirs, files in os.walk(file):

#         # root 表示当前正在访问的文件夹路径
#         # dirs 表示该文件夹下的子目录名list
#         # files 表示该文件夹下的文件list

#         # 遍历文件
#         for f in files:
#             print(os.path.join(root, f))

#         # 遍历所有的文件夹
#         for d in dirs:
#             print(os.path.join(root, d))


# def main():
#     walkFile(os.getcwd)


# if __name__ == '__main__':
#     main()



# -*- coding: utf-8 -*-
# @Time :2018/8/25   20:18
# @Author : ELEVEN
# @File : 011_批量重命名文件.py
# @Software: PyCharm
import os

# 1. 获取一个要重命名的文件夹的名字
# folder_name = input("请输入要重命名的文件夹:")

# 2. 获取那个文件夹中所有的文件名字
print(os.getcwd())
for name in os.listdir('C:\\Users\\Mi\\Desktop\\Frame\\app\\src\\main\\res\\drawable-xhdpi\\'):
    if ".jpg" in name:
        print("<item android:drawable=\"@drawable/%s\" android:duration=\"300\"></item>"%name.split(".jpg")[0])
        # print(name)
        # os.rename("./"+name, "./a"+name)
        # print(name)
# file_names = os.listdir(os.path)

# # 第1中方法
# # os.chdir(folder_name)

# # 3. 对获取的名字进行重命名即可
# # for name in file_names:
# #    print(name)
# #    os.rename(name,"[京东出品]-"+name)

# for name in file_names:
#     print(name)
#     # print(name.split('[京东出品]-')[-1])
#     # name1 = name.split('[京东出品]-')[-1]
#     # old_file_name = "./" + folder_name + "/" + name
#     # new_file_name = "./" + folder_name + "/" + str(i) + "[京东出品]-" + name1
#     old_file_name = "./"+name
#     new_file_name = "./a"+name
#     os.rename(old_file_name, new_file_name)