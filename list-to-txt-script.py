import os
from datetime import datetime


def date_time():
    now = datetime.now()
    global cur_datetime
    cur_datetime = now.strftime('%d/%m/%Y %H:%M:%S')
    return cur_datetime

def list_diretory():
    a = os.listdir()
    global list_dir
    list_dir = '\n'.join(a)
    return list_dir

def write_to_txt():

    try:
        with open('readmenew.txt', 'a+') as f:
            f.write('\n')
            f.write('\n')
            f.write(cur_datetime)
            f.write('\n')
            f.write('------------------- \n')
            f.write(list_dir)
            os.system('attrib +h readmenew.txt')
    except FileNotFoundError:
        print("The 'docs' directory does not exist")



def main():
    date_time()
    list_diretory()
    write_to_txt()

#if __name__ == '__main__':
#    main()