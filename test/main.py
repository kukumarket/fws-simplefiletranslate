import os
# files,dirs=[],[]
# print("os.getcwd        :{}".format(os.getcwd()))
# print("os.path.dirname  :{}".format(os.path.dirname(__file__)))
print("当前路径：{}".format(os.getcwd()))
print("Mode         Name  ")
for item in os.listdir():
    if os.path.isdir(item):
        print("--d-         {}".format(item))
    elif os.path.isfile(item):
        print("---f         {}".format(item))

    # if os.path.isfile(item):
    #     files.append(item)
    # elif os.path.isdir(item):
    #     dirs.append(item)
