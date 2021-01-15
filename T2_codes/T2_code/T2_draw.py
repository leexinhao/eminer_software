import datetime, os
import matplotlib.dates as mdate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import threading

rlock2 = threading.RLock()
T2drawcnt1=0
T2drawcnt2=0
def T2draw1(t1, t2):  # 地区和类型
    tt1=t1
    tt2=t2
    if (t1 == '成都市'):
        t1 = ['国网成都供电公司']
    elif(t1 == '天府新区'):
        t1 = ['国网天府新区供电公司']
    else:
        t1 = ['国网天府新区供电公司','国网成都供电公司']

    if(t2=='全部类型'):
        t2=['城镇居民生活用电','大工业用电','非工业','非居民照明','居民生活用电','农业排灌',\
            '农业生产用电','普通工业','商业用电','乡村居民生活用电','中小学教学用电']
    else:
        t2=[t2]
    x1 = []
    x2 = []
    y = []
    z = []

    t = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'T2_file', 'cons.csv'))
    cons = set()
    for index,i in t.iterrows():
        if (((i['NAME'] in t2) and (i['ORG_NAME']) in t1)):
            cons.add(i['CONS_NO'])
    cnt = 0
    a = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'T2_file', 'results1.csv'))
    for index,i in a.iterrows():
        if (i[0] in cons):
            cnt += 1
            tt=0
            cntt = datetime.datetime.strptime('2020-05-29', '%Y-%m-%d')
            if (cnt == 1):
                for j in i[1:]:
                    tt+=1
                    cntt += datetime.timedelta(seconds=900)
                    y.append(j)
                    #x1.append(tt*15)
                    x1.append(cntt)
            else:
                k = 0
                for j in i[1:]:
                    y[k] += j
                    k += 1
    cnt = 0
    b = pd.read_csv(os.path.join(os.path.dirname(
        os.path.dirname(__file__)), 'T2_file', 'results2.csv'))
    for index,i in b.iterrows():
        if (i[0] in cons):
            cnt += 1
            tt=0
            cntt = datetime.datetime.strptime('2020-05-29', '%Y-%m-%d')
            if (cnt == 1):
                for j in i[1:]:
                    tt+=1
                    cntt += datetime.timedelta(seconds=900)
                    z.append(j)
                    #x2.append(tt*15)
                    x2.append(cntt)
            else:
                k = 0
                for j in i[1:]:
                    z[k] += j
                    k += 1

    doc = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'T2_file', 'tmp1.csv'),'w')
    print('开始时间,结束时间,地区,用电类型,值类型',end='',file=doc)
    for i in range(95*3):
        print(',R',i+1,sep='',end='',file=doc)
    print(file=doc)
    print('20200529','20200531',tt1,tt2,'真实值',sep=',',end='',file=doc)
    for i in z:
        print(',',i,sep='',end='',file=doc)
    print(file=doc)
    print('20200529','20200531', tt1, tt2, '预测值', sep=',', end='', file=doc)
    for i in y:
        print(',', i, sep='', end='', file=doc)
    print(file=doc)

    with rlock2:
        fig1 = plt.figure(figsize=(10, 5))
        ax1 = fig1.add_subplot(1, 1, 1)
        ax1.xaxis.set_major_formatter(mdate.DateFormatter('%m-%d %H:00'))  # 设置时间标签显示格式
        ax = plt.gca()
        ax.spines['right'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        plt.tick_params(axis='x', colors='white')
        plt.tick_params(axis='y', colors='white')
        plt.xlabel('TIME', color='white')
        plt.ylabel('POWER CONSUMPTION', color='white')

        plt.plot(x2, z, label='true value', color='gold')
        plt.plot(x1,y, label='predicted value',color='cyan')
        plt.grid(True)
        plt.gcf().autofmt_xdate()
        plt.legend()
    
        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'T2_png','p1.png'), transparent=True)
        plt.cla()
        plt.clf()
        plt.close('all')


def T2draw2(cons):
    x1 = []
    x2 = []
    y = []
    z = []
    a = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'T2_file','results1.csv'))
    for index, i in a.iterrows():
        if (i[0] == cons):
            cnt=0
            cntt = datetime.datetime.strptime('2020-05-29', '%Y-%m-%d')
            for j in i[1:]:
                y.append(j)
                cnt+=1
                cntt += datetime.timedelta(seconds=900)
                x1.append(cntt)
                #x1.append(cnt*15)

    b = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                    'T2_file', 'results2.csv'))
    for index, i in b.iterrows():
        if (i[0] == cons):
            cnt=0
            cntt = datetime.datetime.strptime('2020-05-29', '%Y-%m-%d')
            for j in i[1:]:
                cnt+=1
                z.append(j)
                cntt += datetime.timedelta(seconds=900)
                x2.append(cntt)
                #x2.append(cnt*15)

    doc = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'T2_file', 'tmp2.csv'),'w')
    print('开始时间,结束时间,用户名称,值类型', end='', file=doc)
    for i in range(95 * 3):
        print(',R', i + 1, sep='', end='', file=doc)
    print(file=doc)
    print('20200529', '20200531', cons, '真实值', sep=',', end='', file=doc)
    for i in z:
        print(',', i, sep='', end='', file=doc)
    print(file=doc)
    print('20200529', '20200531', cons, '预测值', sep=',', end='', file=doc)
    for i in y:
        print(',', i, sep='', end='', file=doc)
    print(file=doc)

    with rlock2:
        fig1 = plt.figure(figsize=(10, 5))
        ax1 = fig1.add_subplot(1, 1, 1)
        ax1.xaxis.set_major_formatter(mdate.DateFormatter('%m-%d %H:00'))  # 设置时间标签显示格式
        ax = plt.gca()
        ax.spines['right'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        plt.tick_params(axis='x', colors='white')
        plt.tick_params(axis='y', colors='white')
        if (len(y) == 0):
            plt.title("Wrong CONS!!!",color='white')
        plt.xlabel('TIME', color='white')
        plt.ylabel('POWER CONSUMPTION', color='white')
        plt.plot(x2, z, label='true value', color='gold')
        plt.plot(x1,y, label='predicted value',color='cyan')

        # plt.savefig('123,png')
        plt.grid(True)
        plt.gcf().autofmt_xdate()

        plt.legend()

        plt.savefig(os.path.join(os.path.dirname(os.path.dirname(
            __file__)), 'T2_png', 'p2.png'), transparent=True)
        plt.cla()
        plt.clf()
        plt.close('all')


