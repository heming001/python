#from multiprocessing import Process#
import os
#
## 子进程要执行的代码
#def run_proc(name):
#    print('Run child process %s (%s)...' % (name, os.getpid()))
#
#if __name__=='__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Process(target=run_proc, args=('test',))
#    print('Child process will start.')
#    p.start()
#    p.join()
#    print('Child process end.')

#from multiprocessing  import Pool
#import os ,time ,random
#
#def long_time_task(name):
#    print('Run task %s (%s)...' %(name,os.getpid()))
#    start = time.time()
#    time.sleep(random.random() * 3)
#    end = time.time()
#    print('Task %s run %0.2f seconds.' % (name,(end - start)))
#
#if __name__ == '__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Pool(4)
#    for i in range(5):
#        p.apply_async(long_time_task, args=(i,))
#    print('Waiting for all Subprocess done...')
#    p.close()
#    p.join()
#    print('All subprocess done.')


#if __name__ == '__main__':
#    print('Parent process %s.' % os.getpid())
#    p = Pool(13)
#    for i in range(16):
#        p.apply_async(long_time_task, agrs=(i,))
#        p.apply_async(long_time_task, args=(i,))
#    print('Waiting for all subprocesses done...')
#    p.close()
#    p.join()
#    print('All subprocesses done.')

#import subprocess

#print('$ nslookup')
#p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
#print(output.decode('utf-8'))
#print('Exit code :',p.returncode)


#print('$ nslookup')
#p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#output, err = p.communicate('set q=mx\npython.org\nexit\n')
#print(output)
#print('Exit code:', p.returncode)

from multiprocessing  import Process ,Queue
import os,time,random

# 写数据执行的代码
def write(q):
    print('Process to write :%s' % os.getpid())
    for value in (['A','B','C']):
        print('Put %s to queue ...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据执行的代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各自子进程
    q = Queue()
    pw = Process(target=write , args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入
    pr.start()
    # 启动子进程pr,读取
    pw.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法等待结束，只能强制终止
    pr.terminate()