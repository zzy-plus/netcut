import os

def isCutExist(cutName):
    if cutName is None:
        return False
    files = os.listdir('./cuts')
    filename = cutName + '.json'
    if filename in files:
        return True
    return False




if __name__ == '__main__':
    isCutExist('test')