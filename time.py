import time as t

class Mytimer():
    def __init__(self):
        self.unit = ['年', '月', '日', '时', '分', '秒']
        self.prmpt = "未开始计时"
        self.lasted = []
        self.begin = 0
        self.end = 0
    def __str__(self):
        return self.prmpt
    __repr__ = __str__
    #a= class_name()
    #a
    #操作后，执行此代码
    #开始计时
    def start(self):
        self.begin = t.localtime()
        print('计时开始')

    #停止计时
    def stop(self):
        if not self.begin:
            print("提示，请先调用start()进行计时")
        else:
            self.end = t.localtime()
            self._calc()
            print('计时开始')

    def __add__(self, other):
        #此方法计算两次计时结果的和
        prmpt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
        #给result list添加数值
            if result[index]:
                prmpt += (str(result[index])+self.unit[index])
        return prmpt
    #内部方法，计算运行时间
    def _calc(self):
        self.prmpt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prmpt += (str(self.lasted[index])+self.unit[index])

        self.begin = 0
        self.end = 0




