import threading
import  time

# 把线程封装成类

class SingThread(threading.Thread):
    def __init__(self,name,a):
        super().__init__()
        self.a=a
        self.name=name

    def run(self):
        print('线程为%s,接收的参数为%s' % (self.name, self.a))
        for i in range(1,6):
            print('i am sing')
            time.sleep(1)

class DanceThread(threading.Thread):
    def __init__(self,name,a):
        super().__init__()
        self.a=a
        self.name=name

    def run(self):
        print('线程为%s,接收的参数为%s' % (self.name, self.a))
        for i in range(1,6):
            print('i am dance')
            time.sleep(1)



def main():
    tsing=SingThread('sing','唐僧')
    tdance=DanceThread('dance','沙和尚')
    tsing.start()
    tdance.start()
    tsing.join()
    tdance.join()
    print('i love you, my girl friend')
if __name__ == '__main__':
    main()