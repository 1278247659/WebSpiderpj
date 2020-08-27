import time
import threading

'''
def sing():
    for x in range(1,6):
        print('唱歌')
        time.sleep(1)
def dance():
    for x in range(1, 6):
        print('跳舞')
        time.sleep(1)

def main():
    sing()
    dance()

if __name__ == '__main__':
    main()
'''
def sing(a):
    print('线程为%s,接收的参数为%s' % (threading.current_thread().name,a))
    for x in range(1, 6):
        print('i am singing')
        time.sleep(1)

def dance(a):
    print('线程为%s,接收的参数为%s' % (threading.current_thread().name, a))
    for x in range(1, 6):
        print('i am dancing')
        time.sleep(1)

def main():
    a='孙悟空'
    # sing thread
    tsing = threading.Thread(target = sing,name = "sing",args = (a, ))
    #dnace thread
    tdance = threading.Thread(target = dance,name = "dance",args = (a, ))
    # start thread
    tsing.start()
    tdance.start()
    # main thread wait son thread end
    tsing.join()
    tdance.join()

    print('this is main thread')


if __name__ == '__main__':
    main()