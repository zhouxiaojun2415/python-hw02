import os

def copydirs(oldpath, newpath):
    print('oldpath:', oldpath)
    print('newpath', newpath)

    os.mkdir(newpath)

    for i in os.listdir(oldpath):
        sourcepath = (oldpath + '/' + i)
        targetpath = (newpath + '/' + i)
        if os.path.isdir(sourcepath):
            copydirs(sourcepath, targetpath)
        else:
            copyfiles(sourcepath, targetpath)

def copyfiles(oldpath, newpath):
    with open(oldpath, 'rb') as f:
        sourcefile = f.read()
    with open(newpath, 'wb') as f:
        f.write(sourcefile)

if __name__ == "__main__":
    copydirs(r'C:/Users/Administrator/PycharmProjects/python-dev', r'D:/python-dev')