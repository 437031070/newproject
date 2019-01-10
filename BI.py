# coding=gbk
import json
import numpy as np
import pandas as pd
from pandas import DataFrame
import re
from urllib.parse import quote
from urllib import request, parse
import datetime
import calendar
import sklearn.cluster as sc
import sklearn.preprocessing as sp  # 预处理包
import sklearn.pipeline as si  # 管线
import sklearn.linear_model as sl  # 线性模型包
import sklearn.model_selection as ms  # 新版本  划分训练和测试
import sklearn.metrics as sm  # 评估包
import pickle

np.set_printoptions(suppress=True)
# 数据清洗指数还原
def Exponential_reduction_inside(data, Choice):
    data = data.reshape((data.size, 1))
    models = []
    # 0
    model = pickle.load(open("models/转化率指数还原模型","rb"))
    models.append(model)
    # 1
    model = pickle.load(open("models/6000以下交易指数模型", "rb"))
    models.append(model)
    # 2
    model = pickle.load(open("models/6000~20000交易指数模型", "rb"))
    models.append(model)
    # 3
    model = pickle.load(open("models/交易指数还原模型", "rb"))
    models.append(model)
    # 4
    model = pickle.load(open("models/3600以下其他指数模型", "rb"))
    models.append(model)
    # 5
    model = pickle.load(open("models/3600~9000流量指数模型", "rb"))
    models.append(model)
    # 6
    model = pickle.load(open("models/9000~48000流量指数模型", "rb"))
    models.append(model)
    # 7
    model = pickle.load(open("models/48000以上流量指数模型", "rb"))
    models.append(model)
    # print(models)
    mat = []
    if Choice == "交易指数":
        for x in data:
            x = np.array([[int(float(x[0]))]])
            if x <= 6000 and x > 37:
                text = models[1].predict(x)[0][0]
                mat.append(int(text))
            elif x > 6000 and x <= 20000:
                text = models[2].predict(x)[0][0]
                mat.append(int(text))
            elif x > 20000:
                text = models[3].predict(x)[0][0]
                mat.append(int(text))
            else:
                mat.append(0)
    elif Choice == "其他指数":
        for x in data:
            x = np.array([[int(float(x[0]))]])
            if x <= 3600:
                text = models[4].predict(x)[0][0]
                mat.append(int(text))
            elif x > 3600 and x <= 9000:
                text = models[5].predict(x)[0][0]
                mat.append(int(text))
            elif x > 9000 and x <= 48000:
                text = models[6].predict(x)[0][0]
                mat.append(int(text))
            elif x > 48000:
                text = models[7].predict(x)[0][0]
                mat.append(int(text))
    elif Choice == "转化率指数":
        for x in data:
            x = np.array([[int(float(x[0]))]])
            text = models[0].predict(x)[0][0]
            mat.append(np.round(text, 4))
    mat = np.array(mat)
    mat = mat.reshape((mat.size, 1))
    return mat
    # 指数还原
def Exponential_reduction(data, Choice):
    print(data)
    print(Choice)
    data = data.split("\n")
    mat = []
    for x in data:
        if x != "":
            mat.append(x)
    data = np.array(mat)
    data = data.reshape((data.size, 1))
    meson = data
    meson = meson.reshape((meson.size, 1))
    models = []
    # 0
    model = pickle.load(open("models/转化率指数还原模型","rb"))
    models.append(model)
    # 1
    model = pickle.load(open("models/6000以下交易指数模型", "rb"))
    models.append(model)
    # 2
    model = pickle.load(open("models/6000~20000交易指数模型", "rb"))
    models.append(model)
    # 3
    model = pickle.load(open("models/交易指数还原模型", "rb"))
    models.append(model)
    # 4
    model = pickle.load(open("models/3600以下其他指数模型", "rb"))
    models.append(model)
    # 5
    model = pickle.load(open("models/3600~9000流量指数模型", "rb"))
    models.append(model)
    # 6
    model = pickle.load(open("models/9000~48000流量指数模型", "rb"))
    models.append(model)
    # 7
    model = pickle.load(open("models/48000以上流量指数模型", "rb"))
    models.append(model)
    # print(models)
    mat = []
    if Choice == "交易指数":
        for x in data:
            x = np.array([[int(x[0])]])
            if x <= 6000:
                text = models[1].predict(x)[0][0]
                mat.append(int(text))
            elif x > 6000 and x <= 20000:
                text = models[2].predict(x)[0][0]
                mat.append(int(text))
            elif x > 20000:
                text = models[3].predict(x)[0][0]
                mat.append(int(text))
    elif Choice == "其他指数":
        for x in data:
            x = np.array([[int(x[0])]])
            if x <= 3600:
                text = models[4].predict(x)[0][0]
                mat.append(int(text))
            elif x > 3600 and x <= 9000:
                text = models[5].predict(x)[0][0]
                mat.append(int(text))
            elif x > 9000 and x <= 48000:
                text = models[6].predict(x)[0][0]
                mat.append(int(text))
            elif x > 48000:
                text = models[7].predict(x)[0][0]
                mat.append(int(text))
    elif Choice == "转化率指数":
        for x in data:
            x = np.array([[x[0]]])
            text = models[0].predict(x)[0][0]
            mat.append(np.round(text, 4))
    mat = np.array(mat)
    mat = mat.reshape((mat.size, 1))
    meson = np.hstack((meson,mat))
    return meson
# 时间转换器("2018-9"这样的时间转换为第一天后最后一天的日期)
def Month_DayAndLastDay(year,month):
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year

    if month:
        month = int(month)
    else:
        month = datetime.date.today().month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)

    # 获取当月的第一天
    firstDay = datetime.date(year=year, month=month, day=1).strftime("%Y-%m-%d")
    lastDay = datetime.date(year=year, month=month, day=monthRange).strftime("%Y-%m-%d")

    return firstDay, lastDay
    """1、市场排行 """
    # 高交易店铺链接
# 时间生成器
def Time_enerator(dateType,date):
    if dateType == "month":
        dates = date.split("-")
        year = dates[0]
        month = dates[1]
        date1, date2 = Month_DayAndLastDay(year, month)
        date = [date1,date2]
        return date
    elif dateType == "recent30":
        date = datetime.date.today()
        date1 = date - datetime.timedelta(days=1)
        date1 = date1.strftime("%Y-%m-%d")
        date2 = date - datetime.timedelta(days=30)
        date2 = date2.strftime("%Y-%m-%d")
        date = [date2,date1]
        return date
    elif dateType == "day":
        date = [date, date]
        return date
# 一年的月份时间生成器
def one_year_enerator():
    dateType = "month"
    date = datetime.date.today()
    dates = []
    for x in range(12):
        date = (date - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        date = Time_enerator(dateType, date)
        dates.append(date)
        date = datetime.datetime.strptime(date[0], "%Y-%m-%d")
    dates = np.array(dates)
    return dates
# 运营视窗
def Aop_window(sheet):
    Annual_operation_window = sheet
    # 设置清洗第一行的正则匹配器
    regex = re.compile("较+")
    newstring = " 较"
    # 设置清洗数据部分的正则匹配器
    regex1 = re.compile("\++")
    newstring1 = " "
    regex2 = re.compile("-+")
    newstring2 = " -"
    # 得到清晰完的首行
    Title = []
    for x in Annual_operation_window[0]:
        try:
            result, numbs = re.subn(regex, newstring, x)
        except TypeError as e:
            x = str(x) + " 0.00%"
        result = result.split(" ")
        Title += result
    Title = np.array(Title)
    # 得到清洗完的数据
    data = []
    for x in Annual_operation_window[1:].ravel():
        try:
            result, numbs = re.subn(regex1, newstring1, x)
        except TypeError as e:
            print("有没有上升的0.00%值请找到它将它修改下")
            x = str(x*10) + '+0.00%'
            print(x)
            result, numbs = re.subn(regex1, newstring1, x)
            # continue
        result, numbs = re.subn(regex2, newstring2, result)
        result = result.split(" ")
        data += result
    data = np.array(data)
    cow = int(data.size / Title.size)
    data = data.reshape((cow, Title.size))
    # 得到数据里的绝对值
    abs_value = data.ravel()[::2]
    abs_values = []
    for x in abs_value:
        if ',' in x:
            x = x.translate(str.maketrans('', '', ','))
        elif '%' in x:
            x = round(float(x.translate(str.maketrans('', '', '%'))) / 100, 4)
        try:
            abs_values.append(float(x))
        except ValueError as e:
            abs_values.append(0)
    abs_values = np.array(abs_values)
    abs_values = abs_values.reshape((17, abs_values.size // 17))
    new_form = abs_values[0:4]
    new_form = np.vstack((new_form, abs_values[3] - abs_values[4]))
    new_form = np.vstack((new_form, abs_values[4]))
    new_form = np.vstack((new_form, abs_values[4] / abs_values[3]))
    new_form = np.vstack((new_form, abs_values[5]))
    new_form = np.vstack((new_form, abs_values[5] / abs_values[0]))
    new_form = np.vstack((new_form, abs_values[5] / abs_values[4]))
    new_form = np.vstack((new_form, abs_values[6]))
    new_form = np.vstack((new_form, abs_values[7]))
    new_form = np.vstack((new_form, abs_values[8]))
    new_form = np.vstack((new_form, abs_values[9]))
    new_form = np.vstack((new_form, abs_values[9] / abs_values[8]))
    new_form = np.vstack((new_form, abs_values[10]))
    new_form = np.vstack((new_form, abs_values[10] / new_form[12]))
    new_form = np.vstack((new_form, abs_values[11]))
    new_form = np.vstack((new_form, abs_values[12]))
    new_form = np.vstack((new_form, abs_values[12] / abs_values[8]))
    new_form = np.vstack((new_form, abs_values[13]))
    new_form = np.vstack((new_form, abs_values[14]))
    new_form = np.vstack((new_form, abs_values[15]))
    new_form = np.vstack((new_form, (abs_values[13] + abs_values[14] + abs_values[15]) / abs_values[0]))
    new_form = np.vstack((new_form, abs_values[16]))
    form = new_form
    form = DataFrame(new_form)
    return form

""" 4、市场大盘 """
# Industry_type = "transaction"行业交易构成 "seller" 卖家分布
def Industry_market(cateID,Industry_type):
    if Industry_type == "行业交易构成":
        Industry_type = "transaction"
    elif Industry_type == "卖家分布":
        Industry_type = "seller"
    cateID = str(cateID)
    dates = one_year_enerator()
    IPS = {}
    for x in dates:
        date = x[0] + "%7C" + x[1]
        if Industry_type == "transaction":
            IP = "https://sycm.taobao.com/mc/mq/supply/deal/list.json?dateRange=" + date + "&dateType=month&pageSize=10&page=1&order=desc&orderBy=tradeIndex&cateId="+ cateID +"&device=0&sellerType=-1&indexCode=tradeIndex%2CtradeGrowthRange%2CpayAmtParentCateRate%2CpayCntParentCateRate&_=1540178532790&token="
            IPS[x[0]] = IP
        elif Industry_type == "seller":
            IP = "https://sycm.taobao.com/mc/mq/supply/mkt/childCate.json?dateRange=" + date + "&dateType=month&pageSize=5&page=1&order=desc&orderBy=slrCnt&cateId=" + cateID + "&device=0&sellerType=-1&indexCode=slrCnt%2CparentCateSlrRate%2CtradeSlrCnt%2CparentCateTradeSlrCntRate&_=1540178534572&token="
            IPS[x[0]] = IP
    return IPS
# 行业构成解码
def Industry_composition_Decode(date,data,cateID):
    data = json.loads(data)["data"]
    form = []
    for cow in data:
        text = []
        text.append(cateID)
        text.append("行业构成")
        text.append(date)
        text.append(cow['cateBo']['cateName'])
        text.append(cow['tradeIndex']['value'])
        try:
            text.append(np.round(cow['tradeGrowthRange']['value'], 4))
        except KeyError:
            text.append(0)
        try:
            text.append(np.round(cow['payAmtParentCateRate']['value'], 4))
        except KeyError:
            text.append(0)
        try:
            text.append(np.round(cow['payCntParentCateRate']['value'], 4))
        except KeyError:
            text.append(0)
        form.append(text)
    form = np.array(form)
    Payment_amount = form[::, 4]
    Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
    form = np.hstack((form, Payment_amount))
    print(form[0])
    return form
# 卖家分布解码
def seller_composition_Decode(date,data,cateID):
    if data != 0:
        str = json.loads(data)["data"]
    else:
        f = open('子行业分布数据.txt')
        str = f.read()
        str = json.loads(str)["data"]
    form = []
    for cow in str:
        text = []
        text.append(cateID)
        text.append("子行业分布")
        text.append(date)
        text.append(cow['cateBo']['cateName'])
        try:
            text.append(cow['slrCnt']['value'])
        except KeyError:
            text.append(0)
        try:
            text.append(np.round(cow['parentCateSlrRate']['value'], 4))
        except KeyError:
            text.append(0)
        try:
            text.append(cow['tradeSlrCnt']['value'])
        except KeyError:
            text.append(0)
        try:
            text.append(np.round(cow['parentCateTradeSlrCntRate']['value'], 4))
        except KeyError:
            text.append(0)
        form.append(text)
    form = np.array(form)
    return form

"""1、市场排行"""
# 店铺排行 # 交易店shop_type="hotsale",流量店shop_type="hotsearch" , 高意向hotpurpose返回IP字典
def Store_ranking(cateID,one_type,tow_type):
    dates = one_year_enerator()
    IPS = []
    for x in dates:
        text = []
        date = x[0] + "%7C" + x[1]
        IP = "https://sycm.taobao.com/mc/mq/mkt/rank/"+tow_type+"/"+ one_type +".json?dateRange="+\
            date + '&dateType=month' + "&pageSize=" + "10&page=1&cateId="\
            + str(cateID) + "&device=0&sellerType=-1&_=1540178532790&token="
        text.append(x[0])
        text.append(IP)
        IPS.append(text)
    IPS = np.array(IPS)
    mat = {}
    for IP in IPS:
        mat[IP[0]] = IP[1]
    return mat
# 市场排行解码
# 市场排行 # 交易店shop_type="hotsale",流量店shop_type="hotsearch" , 高意向hotpurpose返回IP字典
# 市场排行解码
def Industry_ranking_Data_decoding(date,cateID,data,one_type,tow_type):
    # coding=gbk
    # with open('data.txt', "rb") as f:  # 设置文件对象
    #     data = f.read()
    # print(type(str))
    str = json.loads(data)["data"]
    # print(str[0])
    # 店铺
    if one_type == "shop":
        # 高流量
        if tow_type == "hotsearch":
            form = []
            for cow in str:
                text = []
                text.append(cateID)
                text.append("店铺排行")
                text.append("高流量")
                text.append(date)
                try:
                    text.append(cow['shop']['title'])
                except KeyError:
                    continue
                text.append(cow['cateRankId']['value'])
                text.append(cow['shop']['userId'])
                text.append(cow['shop']['shopUrl'])
                if cow['shop']['b2CShop']:
                    text.append(1)
                else:
                    text.append(0)
                text.append(cow['uvIndex']['value'])
                text.append(cow['seIpvUvHits']['value'])
                text.append(cow['tradeIndex']['value'])
                form.append(text)
            form = np.array(form)
            Search = form[::,10]
            Search = Exponential_reduction_inside(Search, "其他指数")
            Payment_amount = form[::, 11]
            Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
            Visitor = form[::, 9]
            Visitor = Exponential_reduction_inside(Visitor, "其他指数")
            form = np.hstack((form, Visitor))
            form = np.hstack((form, Search))
            form = np.hstack((form, Payment_amount))
            form = np.hstack((form, Search/Visitor))
            return form
        elif tow_type == "hotsale":
            form = []
            for cow in str:
                text = []
                text.append(cateID)
                text.append("店铺排行")
                text.append("高交易")
                text.append(date)
                try:
                    text.append(cow['shop']['title'])
                except KeyError:
                    continue
                text.append(cow['cateRankId']['value'])
                text.append(cow['shop']['userId'])
                text.append(cow['shop']['shopUrl'])
                if cow['shop']['b2CShop']:
                    text.append(1)
                else:
                    text.append(0)
                text.append(cow['tradeIndex']['value'])
                text.append(cow['payRateIndex']['value'])
                form.append(text)
            form = np.array(form)
            Conversion_rate = form[::,9]
            Conversion_rate = Exponential_reduction_inside(Conversion_rate, "转化率指数")
            Payment_amount = form[::, 8]
            Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
            form = np.hstack((form, Conversion_rate))
            form = np.hstack((form, Payment_amount))
            return form
    elif one_type == "item":
        # 商品高流量
        if tow_type == "hotsearch":
            form = []
            for cow in str:
                text = []
                text.append(cateID)
                text.append("商品排行")
                text.append("高流量")
                text.append(date)
                try:
                    text.append(cow['item']['title'])
                except KeyError:
                    continue
                text.append(cow['item']['itemId'])
                text.append(cow['item']['detailUrl'])

                text.append(cow['cateRankId']['value'])
                try:
                    text.append(cow['shop']['title'])
                except KeyError:
                    text.append("未知店铺")
                text.append(cow['shop']['userId'])
                try:
                    text.append(cow['shop']['shopUrl'])
                except KeyError:
                    text.append("未知地址")
                text.append(cow['uvIndex']['value'])
                text.append(cow['seIpvUvHits']['value'])
                text.append(cow['tradeIndex']['value'])
                form.append(text)
            form = np.array(form)
            Search = form[::,12]
            Search = Exponential_reduction_inside(Search, "其他指数")
            Payment_amount = form[::, 13]
            Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
            Visitor = form[::, 11]
            Visitor = Exponential_reduction_inside(Visitor, "其他指数")
            form = np.hstack((form, Visitor))
            form = np.hstack((form, Search))
            form = np.hstack((form, Payment_amount))
            form = np.hstack((form, Search/Visitor))
            return form
        # 商品高交易
        elif tow_type == "hotsale":
            form = []
            for cow in str:
                text = []
                text.append(cateID)
                text.append("商品排行")
                text.append("高交易")
                text.append(date)
                try:
                    text.append(cow['item']['title'])
                except KeyError:
                    continue
                text.append(cow['item']['itemId'])
                text.append(cow['item']['detailUrl'])
                text.append(cow['cateRankId']['value'])
                try:
                    text.append(cow['shop']['title'])
                except KeyError:
                    text.append("未知店铺")
                text.append(cow['shop']['userId'])
                try:
                    text.append(cow['shop']['shopUrl'])
                except KeyError:
                    text.append("未知地址")
                text.append(cow['payRateIndex']['value'])
                text.append(cow['tradeIndex']['value'])

                form.append(text)
            form = np.array(form)
            Conversion_rate = form[::,11]
            Conversion_rate = Exponential_reduction_inside(Conversion_rate, "转化率指数")
            Payment_amount = form[::, 12]
            Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
            form = np.hstack((form, Conversion_rate))
            form = np.hstack((form, Payment_amount))
            return form
        # 商品高意向
        elif tow_type == "hotpurpose":
            form = []
            for cow in str:
                text = []
                text.append(cateID)
                text.append("商品排行")
                text.append("高意向")
                text.append(date)
                try:
                    text.append(cow['item']['title'])
                except KeyError:
                    continue
                text.append(cow['item']['itemId'])
                text.append(cow['item']['detailUrl'])
                text.append(cow['cateRankId']['value'])
                try:
                    text.append(cow['shop']['title'])
                except KeyError:
                    text.append("未知店铺")
                text.append(cow['shop']['userId'])
                try:
                    text.append(cow['shop']['shopUrl'])
                except KeyError:
                    text.append("未知地址")
                text.append(cow['cltHits']['value'])
                text.append(cow['cartHits']['value'])
                text.append(cow['tradeIndex']['value'])
                form.append(text)
            form = np.array(form)
            Collection = form[::,11]
            Collection = Exponential_reduction_inside(Collection, "其他指数")
            Shopping_Cart = form[::, 12]
            Shopping_Cart = Exponential_reduction_inside(Shopping_Cart, "其他指数")
            Payment_amount = form[::, 13]
            Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
            form = np.hstack((form, Collection))
            form = np.hstack((form, Shopping_Cart))
            form = np.hstack((form, Payment_amount))
            return form
    elif one_type == "brand":
        if tow_type == "hotsearch":
            form = []
            for cow in str:
                text = []
                text.append(cateID)
                text.append("品牌排行")
                text.append("高流量")
                text.append(date)
                try:
                    text.append(cow['brandModel']['brandName'])
                except KeyError:
                    continue
                text.append(cow['brandModel']['brandId'])
                text.append(cow['cateRankId']['value'])
                text.append(cow['uvIndex']['value'])
                text.append(cow['seIpvUvHits']['value'])
                text.append(cow['tradeIndex']['value'])
                form.append(text)
            form = np.array(form)
            # print(form[0])
            Visitor = form[::, 7]
            Visitor = Exponential_reduction_inside(Visitor, "其他指数")
            Search = form[::,8]
            Search = Exponential_reduction_inside(Search, "其他指数")
            Payment_amount = form[::, 9]
            Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
            form = np.hstack((form, Visitor))
            form = np.hstack((form, Search))
            form = np.hstack((form, Payment_amount))
            form = np.hstack((form, Search/Visitor))

            return form
        elif tow_type == "hotsale":
            form = []
            for cow in str:
                text = []
                text.append(cateID)
                text.append("品牌排行")
                text.append("高交易")
                text.append(date)
                try:
                    text.append(cow['brandModel']['brandName'])
                except KeyError:
                    continue
                text.append(cow['brandModel']['brandId'])
                text.append(cow["cateRankId"]['value'])
                if cow['payRateIndex']['value'] != "-":
                    text.append(cow['payRateIndex']['value'])
                else:
                    text.append(0)
                try:
                    text.append(cow['tradeIndex']['value'])
                except KeyError:
                    text.append(0)

                form.append(text)
            form = np.array(form)
            Conversion_rate = form[::,7]
            Conversion_rate = Exponential_reduction_inside(Conversion_rate, "转化率指数")
            Payment_amount = form[::, 8]
            Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
            form = np.hstack((form, Conversion_rate))
            form = np.hstack((form, Payment_amount))
            # print(form[:20])
            return form

# 热门属性
def Hot_attributes(data, attribute_ip):
    print(data)
    result = parse.urlparse(attribute_ip)
    text = result.query.split("&")
    for x in text:
        x = x.split("=")
        if x[0] == "cateId":
            cateID = x[1]

    date = Time_enerator("recent30", " ")
    text = data.split(" ")
    # print(text)
    type_ = []
    indexs = []
    # 得到属性种类
    for x in text:
        if len(type_) == 2:
            break
        elif x == '热销属性热销属性组合':
            type_.append(text.index(x) + 1)
        elif x == '请输入属性值名称关键字':
            type_.append(text.index(x))
    type_ = text[type_[0]: type_[1]][0]

    for x in text:
        if x == '属性值\t交易指数\t支付件数\t操作':
            indexs.append(text.index(x) + 1)
        elif x == '每页显示':
            indexs.append(text.index(x))
    data = text[indexs[0]: indexs[1]]
    form = []
    fn = []
    # print(data)
    for x in data:
        if x != "属性分析":
            if "\t" in x:
                text = x.split("\t")
                fn.append(text[0])
                fn.append(text[1])
            else:
                fn.append(x)
        else:
            form.append(fn)
            fn = []
    mat = []
    # print(form)
    for cow in form:
        if len(cow) > 3:
            a = ""
            text = []
            for x in cow[:-2]:
                a += x
            # print(cow)
            # print(a)
            text.append(a)
            text.append(cow[-2:][0])
            text.append(cow[-2:][1])
            # print(text)
            mat.append(text)
        else:
            mat.append(cow)
    mat = np.array(mat)
    form = []
    for x in mat:
        text = []
        text.append(cateID)
        text.append("热销属性")
        text.append(type_)
        text.append(date[0] + "~" + date[1])
        for y in x:
            text.append(y)
        form.append(text)
    form = np.array(form)
    Sale = form[::, 5]
    Sale = Exponential_reduction_inside(Sale, "交易指数")
    form = np.hstack((form, Sale))
    # print(form)
    return form


""" 2、搜索排行 """
# 搜索词链接
def Search_terms(cateID):
    dateType = "recent30"
    date = Time_enerator(dateType, date="")
    IP1 = "https://sycm.taobao.com/mc/industry/searchWord.json?dateRange="+ date[0] + "%7C" + date[1] + "&dateType=recent30&pageSize=10&page=1&order=desc&cateId=" + str(cateID) + "&device=0&_=1536737824729&token="
    IP2 = "https://sycm.taobao.com/mc/industry/brandWord.json?dateRange=" + date[0] + "%7C" + date[
        1] + "&dateType=recent30&pageSize=10&page=1&order=desc&cateId=" + str(
        cateID) + "&device=0&_=1536737824729&token="
    IP3 = "https://sycm.taobao.com/mc/industry/coreWord.json?dateRange=" + date[0] + "%7C" + date[
        1] + "&dateType=recent30&pageSize=10&page=1&order=desc&cateId=" + str(
        cateID) + "&device=0&_=1536737824729&token="
    IP4 = "https://sycm.taobao.com/mc/industry/attrWord.json?dateRange=" + date[0] + "%7C" + date[
        1] + "&dateType=recent30&pageSize=10&page=1&order=desc&cateId=" + str(
        cateID) + "&device=0&_=1536737824729&token="
    IPS = {"搜索词":IP1,"品牌词":IP2,"核心词":IP3,"修饰词":IP4}
    return IPS
# 搜索词解码
def Search_terms_Decode(cateID,data):
    date = datetime.date.today()
    date1 = date - datetime.timedelta(days=1)
    date2 = date - datetime.timedelta(days=30)
    if data != 0:
        data = str(data)
        data = json.loads(data, strict=False)['data']
    data = data['hotList']

    date1 = date1.strftime('%Y-%m-%d')
    form = []
    for cow in data:
        text = []
        text.append(cateID)
        text.append("搜索排行")
        text.append("搜索词")
        text.append(date1)
        try:
            text.append(cow['searchWord'])
        except KeyError as a:
            continue


        text.append(cow['hotSearchRank'])
        try:
            # 搜索人气
            text.append(cow['seIpvUvHits'])
        except KeyError as a:
            text.append(0)
        try:
            # 点击人气
            text.append(cow['clickHits'])
        except KeyError as a:
            text.append(0)
        try:
            #点击率
            text.append(cow['clickRate'])
        except KeyError as a:
            text.append(0)
        try:
            # 支付转化率
            text.append(cow['payRate'])
        except KeyError as a:
            text.append(0)
        try:
            # 直通车参考价
            text.append(cow['p4pRefPrice'])
        except KeyError as a:
            text.append(0)
        try:
            # 商城点击占比
            text.append(cow['tmClickRate'])
        except KeyError as a:
            text.append(0)
        form.append(text)
    form = np.array(form)
    search = form[::, 6]
    search = Exponential_reduction_inside(search, "其他指数")
    click = form[::, 7]
    click = Exponential_reduction_inside(click, "其他指数")
    form = np.hstack((form, search))
    form = np.hstack((form, click))
    return form
# 品牌词解码
def brand_Word_Decode(cateID,data):
    date = datetime.date.today()
    date1 = date - datetime.timedelta(days=1)
    date2 = date - datetime.timedelta(days=30)
    if data != 0:
        data = str(data)
        data = json.loads(data, strict=False)['data']

    data = data['hotList']

    date1 = date1.strftime('%Y-%m-%d')
    form = []
    for cow in data:
        #
        text = []
        text.append(cateID)
        text.append("搜索排行")
        text.append("品牌词")
        text.append(date1)
        try:
            text.append(cow['searchWord'])
        except KeyError as a:
            text.append(0)
        text.append(cow['hotSearchRank'])
        try:
            text.append(cow['relSeWordCnt'])
        except KeyError as a:
            text.append(0)
        try:
            text.append(cow['avgWordSeIpvUvHits'])
        except KeyError as a:
            text.append(0)
        try:
            text.append(cow['avgWordClickHits'])
        except KeyError as a:
            text.append(0)
        try:
            text.append(cow['p4pRefPrice'])
        except KeyError as a:
            text.append(0)
        form.append(text)
    form = np.array(form)
    search = form[::, 7]
    search = Exponential_reduction_inside(search, "其他指数")
    click = form[::, 8]
    click = Exponential_reduction_inside(click, "其他指数")
    form = np.hstack((form, search))
    form = np.hstack((form, click))

    return form
# 修饰词解码
def Modifiers_Decode(cateID,data):
    date = datetime.date.today()
    date1 = date - datetime.timedelta(days=1)
    date2 = date - datetime.timedelta(days=30)
    if data != 0:
        data = str(data)
        data = json.loads(data, strict=False)['data']
    # 得到飙升词
    Soar_str = data['soarList']
    data = data['hotList']
    date1 = date1.strftime('%Y-%m-%d')
    form = []
    for cow in data:
        #
        text = []
        text.append(cateID)
        text.append("搜索排行")
        text.append("修饰词")
        text.append(date1)
        try:
            text.append(cow['searchWord'])
        except KeyError as a:
            text.append(0)
        text.append(cow['hotSearchRank'])
        try:
            text.append(cow['relSeWordCnt'])
        except KeyError as a:
            text.append(0)
        try:
            text.append(cow['avgWordSeIpvUvHits'])
        except KeyError as a:
            text.append(0)
        try:
            text.append(cow['avgWordClickHits'])
        except KeyError as a:
            text.append(0)
        try:
            text.append(cow['p4pRefPrice'])
        except KeyError as a:
            text.append(0)
        form.append(text)
    form = np.array(form)
    search = form[::, 7]
    search = Exponential_reduction_inside(search, "其他指数")
    click = form[::, 8]
    click = Exponential_reduction_inside(click, "其他指数")
    form = np.hstack((form, search))
    form = np.hstack((form, click))

    return form
# 核心词解码
def Core_word_Decode(cateID, data):
    date = datetime.date.today()
    date1 = date - datetime.timedelta(days=1)
    if data != 0:
        data = str(data)
        data = json.loads(data, strict=False)['data']
    # 得到飙升词
    Soar_str = data['soarList']
    data = data['hotList']
    date1 = date1.strftime('%Y-%m-%d')
    form = []
    for cow in data:
        #
        text = []
        text.append(cateID)
        text.append("搜索排行")
        text.append("核心词")
        text.append(date1)
        try:
            text.append(cow['searchWord'])
        except KeyError as a:
            text.append(0)
        text.append(cow['hotSearchRank'])
        try:
            text.append(cow['relSeWordCnt'])
        except KeyError as a:
            text.append(0)
        try:
            text.append(cow['avgWordSeIpvUvHits'])
        except KeyError as a:
            text.append(0)
        try:
            text.append(cow['avgWordClickHits'])
        except KeyError as a:
            text.append(0)
        try:
            text.append(cow['p4pRefPrice'])
        except KeyError as a:
            text.append(0)
        form.append(text)
    form = np.array(form)
    search = form[::, 7]
    search = Exponential_reduction_inside(search, "其他指数")
    click = form[::, 8]
    click = Exponential_reduction_inside(click, "其他指数")
    form = np.hstack((form, search))
    form = np.hstack((form, click))

    return form

""" 3、搜索分析 """
# 搜索分析链接
def Search_analysis30(key_word):
    key_word = quote(key_word, 'utf-8')
    date = datetime.date.today()
    date1 = date - datetime.timedelta(days=1)
    date1 = date1.strftime("%Y-%m-%d")
    date2 = date - datetime.timedelta(days=30)
    date2 = date2.strftime("%Y-%m-%d")
    IP = "https://sycm.taobao.com/mc/searchword/relatedWord.json?dateRange=" + date2 + "%7C" + date1 + "&dateType=recent30&pageSize=10&page=1&order=desc&orderBy=seIpvUvHits&keyword=" + key_word + "&device=0&indexCode=seIpvUvHits%2CsePvIndex%2CclickRate%2CclickHits%2CclickHot&_=1536024635284&token="
    return IP
# 搜索分析解码
def Search_analysis30_Decode(word,data):
    data = json.loads(data, strict=False)['data']
    date = datetime.date.today()
    date1 = date - datetime.timedelta(days=1)
    date1 = date1.strftime("%Y-%m-%d")
    form = []
    print(data[0])
    for cow in data:
        text = []
        text.append("相关搜索词")
        text.append(date1)
        text.append(word)

        try:
            text.append(cow["keyword"])
        except KeyError:
            continue
        try:
            text.append(cow['seIpvUvHits'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['spvRatio'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['sePvIndex'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['clickRate'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['clickHits'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['clickHot'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['tradeIndex'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['payConvRate'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['onlineGoodsCnt'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['tmClickRatio'])
        except KeyError:
            text.append(0)
        try:
            text.append(cow['p4pAmt'])
        except KeyError:
            text.append(0)
        form.append(text)
    form = np.array(form)
    Search_frequency = form[::, 6]
    Search_frequency = Exponential_reduction_inside(Search_frequency, "其他指数")
    click_Popularity = form[::, 8]
    click_Popularity = Exponential_reduction_inside(click_Popularity, "其他指数")
    click_Number = form[::, 9]
    click_Number = Exponential_reduction_inside(click_Number, "其他指数")
    click_Popularity = form[::, 10]
    click_Popularity = Exponential_reduction_inside(click_Popularity, "其他指数")
    Payment_amount = form[::, 12]
    Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
    form = np.hstack((form, Search_frequency))
    form = np.hstack((form, click_Popularity))
    form = np.hstack((form, click_Number))
    form = np.hstack((form, click_Popularity))
    form = np.hstack((form, Payment_amount))
    return form


# 地域分布
# 获取最近一个月的地域分布
def geographical_distribution(cateID):
    date = datetime.date.today()
    date = (date - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    cateID = str(cateID)
    dateType = "month"
    date = Time_enerator(dateType, date)
    IP = "https://sycm.taobao.com/mc/mq/supply/mkt/area/province.json?dateRange="+ date[0] +"%7C" + date[1] +"&dateType=month&pageSize=5&page=1&order=desc&orderBy=slrCnt&cateId="+ cateID +"&device=0&sellerType=-1&indexCode=slrCnt%2CparentCateSlrRate%2CtradeSlrCnt%2CparentCateTradeSlrCntRate&_=1540178535370&token="
    return IP
# 地域分布解码
def geographical_distribution_Decode(data,cateID):
    data = json.loads(data)["data"]
    date = datetime.date.today()
    date = (date - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    dateType = "month"
    date = Time_enerator(dateType, date)
    form = []
    for cow in data:
        text = []
        text.append(cateID)
        text.append("地域分布")
        text.append(date[0]+"~"+date[1])
        text.append(cow['areaName']['value'])
        text.append(cow['slrCnt']['value'])
        text.append(cow['parentCateSlrRate']['value'])
        text.append(cow['tradeSlrCnt']['value'])
        text.append(cow['parentCateTradeSlrCntRate']['value'])
        form.append(text)
    form = np.array(form)
    return form
"""
    商品、品牌、竞店30天内趋势分析
"""
# 商品趋势链接
def Commodity_trend(itemID,cateID, date):
    if date == 0:
        date = datetime.date.today()
        date = date - datetime.timedelta(days=2)
        date = date.strftime("%Y-%m-%d")
        cateID = str(cateID)
        IP = "https://sycm.taobao.com/mc/ci/item/trend.json?dateType=day&dateRange=" + date + "%7C" + date + "&cateId=" + cateID + "&itemId=" + itemID + "&device=0&sellerType=-1&indexCode=uvIndex%2CpayRateIndex%2CtradeIndex%2CpayByrCntIndex&_=1536291133214&token="
        return IP
    else:
        itemID = str(itemID)
        year = date[:4]
        Month = date[5:]
        date1, date2 = Month_DayAndLastDay(year,Month)
        cateID = str(cateID)
        M_IP = date1 + "数据链接：https://sycm.taobao.com/mc/ci/item/trend.json?dateType=month&dateRange=" + date1 +"%7C"+ date2+"&cateId="+cateID+"&itemId="+itemID+"&device=0&selleType=-1&indexCode=uvIndex%2CpayRateIndex%2CtradeIndex%2CpayByrCntIndex&_=1536291133214&token="
        return M_IP, date1
# 店铺趋势链接
def Trend_of_competition(cateID, shop_ip, date):
    year = date[:4]
    Month = date[5:]
    date1, date2 = Month_DayAndLastDay(year,Month)
    date = datetime.date.today()
    date = date - datetime.timedelta(days=2)
    date = date.strftime("%Y-%m-%d")
    cateID = str(cateID)
    result = re.findall(".*=(.*)&.*",shop_ip)
    for x in result:
        UserId = str(x)
    IP = "最近30天数据链接：https://sycm.taobao.com/mc/ci/shop/trend.json?dateType=day&dateRange="+date+"%7C"+date+"&cateId="+cateID+"&userId="+ UserId +"&device=0&sellerType=-1&indexCode=uvIndex%2CpayRateIndex%2CtradeIndex%2CpayByrCntIndex&_=1536291133214&token="
    M_IP = date1 + "数据链接：https://sycm.taobao.com/mc/ci/shop/trend.json?dateType=month&dateRange=" + date1 + "%7C" + date2 + "&cateId=" + cateID + "&userId=" + UserId + "&device=0&sellerType=-1&indexCode=uvIndex%2CpayRateIndex%2CtradeIndex%2CpayByrCntIndex&_=1536291133214&token="
    return IP, M_IP
# 品牌趋势链接
def Brand_trend(cateID, Brand_ip, date):
    date = date
    year = date[:4]
    Month = date[5:]
    date1, date2 = Month_DayAndLastDay(year,Month)
    date = datetime.date.today()
    date = date - datetime.timedelta(days=2)
    date = date.strftime("%Y-%m-%d")
    cateID = str(cateID)
    result = re.findall(".*Brand1Id=(.*).*",Brand_ip)
    for x in result:
        brandId = str(x)
    IP = "最近30天数据链接：https://sycm.taobao.com/mc/ci/brand/trend.json?dateType=day&dateRange="+date+"%7C"+date+"&cateId="+cateID+"&brandId="+ brandId +"&device=0&sellerType=-1&indexCode=uvIndex%2CpayRateIndex%2CtradeIndex%2CpayByrCntIndex&_=1536291133214&token="
    M_IP = date1 + "数据链接：https://sycm.taobao.com/mc/ci/brand/trend.json?dateType=month&dateRange=" + date1 + "%7C" + date2 + "&cateId=" + cateID + "&brandId="+ brandId +"&device=0&sellerType=-1&indexCode=uvIndex%2CpayRateIndex%2CtradeIndex%2CpayByrCntIndex&_=1536291133214&token="
    return IP, M_IP
# 商品趋势数据解码
def Commodity_trend_Decode(data,date,itemID):
    if data != 0:
        str = data
    else:
        f = open('商品30天趋势数据.txt')
        str = f.read()
        str = json.loads(str)["data"]
    # 生成30个时间戳
    dates = [date]
    for x in range(1,30):
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        date = date - datetime.timedelta(days=1)
        date = date.strftime("%Y-%m-%d")
        dates.append(date)
    dates = np.array(dates).reshape((30, 1))[::-1]
    # print(dates)
    # 生成30个'30天商品趋势'
    titles = []
    for x in range(1,31):
        titles.append("30天商品趋势")
    titles = np.array(titles).reshape((30, 1))
    # 生成30个'ID'
    IDS = []
    for x in range(1,31):
        IDS.append(itemID)
    IDS = np.array(IDS).reshape((30, 1))
    form = np.hstack((titles, IDS))
    form = np.hstack((form, dates))
    text = np.array(str['tradeIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['uvIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['payRateIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['payByrCntIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['seIpvUvHits']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['cltHits']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['cartHits']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['payItemCnt']).reshape((30, 1))
    form = np.hstack((form, text))
    return form
# 店铺趋势数据解码
def Trend_of_competition_Decode(data,date,shop_ID):
    if data != 0:
        str = data
    else:
        f = open('店铺30天趋势数据.txt')
        str = f.read()
        str = json.loads(str)["data"]
    # 生成30个时间戳
    dates = [date]
    for x in range(1,30):
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        date = date - datetime.timedelta(days=1)
        date = date.strftime("%Y-%m-%d")
        dates.append(date)
    dates = np.array(dates).reshape((30, 1))[::-1]
    # print(dates)
    # 生成30个'30天商品趋势'
    titles = []
    for x in range(1,31):
        titles.append("30天店铺趋势")
    titles = np.array(titles).reshape((30, 1))
    # 生成30个'ID'
    IDS = []
    for x in range(1,31):
        IDS.append(shop_ID)
    IDS = np.array(IDS).reshape((30, 1))
    form = np.hstack((titles, IDS))
    form = np.hstack((form, dates))
    text = np.array(str['tradeIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['uvIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['payByrCntIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['payRateIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    return form
# 品牌趋势数据解码
def Brand_trend_Decode(data,date,Brand_ID):
    if data != 0:
        str = data
    else:
        f = open('品牌30天趋势数据.txt')
        str = f.read()
        str = json.loads(str)["data"]
    # 生成30个时间戳
    dates = [date]
    for x in range(1,30):
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        date = date - datetime.timedelta(days=1)
        date = date.strftime("%Y-%m-%d")
        dates.append(date)
    dates = np.array(dates).reshape((30, 1))[::-1]
    # print(dates)
    # 生成30个'30天商品趋势'
    titles = []
    for x in range(1,31):
        titles.append("30天品牌趋势")
    titles = np.array(titles).reshape((30, 1))
    # 生成30个'ID'
    IDS = []
    for x in range(1,31):
        IDS.append(Brand_ID)
    IDS = np.array(IDS).reshape((30, 1))
    # print(str)
    form = np.hstack((titles, IDS))
    form = np.hstack((form, dates))
    text = np.array(str['tradeIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['uvIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['payByrCntIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    text = np.array(str['payRateIndex']).reshape((30, 1))
    form = np.hstack((form, text))
    return form
"""
    竞争板块
"""
# 竞品部分
# 竞品入店来源1、日2、最近30天3、某月
def Source_of_entry_product(item_ip):
    # item_ip = "https://sycm.taobao.com/mc/ci/item/analysis?cateFlag=1&cateId=50002766&dateRange=2019-01-01%7C2019-01-01&dateType=today&parentCateId=0&spm=a21ag.11815280.LeftMenu.d1494.6b8c50a57cIZ0t&rivalItem1Id=527976528448&rivalItem2Id=&selfItemId=42066957401"
    result = parse.urlparse(item_ip)
    text = result.query.split("&")
    for x in text:
        x = x.split("=")
        if x[0] == "cateId":
            cateID = x[1]
        elif x[0] == 'rivalItem1Id':
            itemID = x[1]
# 最近30天与月份型
    IPS = []
    date = datetime.date.today()
    date1 = date - datetime.timedelta(days=1)
    date1 = date1.strftime("%Y-%m-%d")
    date2 = date - datetime.timedelta(days=30)
    date2 = date2.strftime("%Y-%m-%d")
    IP = "http://sycm.taobao.com/mc/rivalItem/analysis/getFlowSource.json?dateRange="+date2+"%7C"+date1+"&dateType=recent30&indexCode=uv&orderBy=uv&order=desc&cateId="+cateID+"&device=2&rivalItem1Id="+itemID+"&_=1540178535370&token="
    datess = ["最近30天"]
    IPS = [IP]
    dates = one_year_enerator()
    for date in dates:
        datess.append(date[0])
        IP = "http://sycm.taobao.com/mc/rivalItem/analysis/getFlowSource.json?dateRange=" + date[0] + "%7C" + date[1] + "&dateType=month&indexCode=uv&orderBy=uv&order=desc&cateId=" + cateID + "&device=2&rivalItem1Id=" + itemID + "&_=1540178535370&token="
        IPS.append(IP)
    form = []
    for IP,date in zip(IPS,datess):
        form.append({date:IP})
    return form,cateID,itemID
#  竞品入店来源解码
def Source_of_entry_product_Decode(cateID,itemID, data, date):
    data = json.loads(data)["data"]
    form = []
    for x in data:
        text = []
        text.append(cateID)
        text.append("竞品入店来源")
        text.append(date)
        text.append(itemID)
        text.append(x['pageName']['value'])
        text.append(x['rivalItem1PayByrCntIndex']['value'])
        text.append(x['uv']['value'])
        text.append(x['rivalItem1PayRateIndex']['value'])
        text.append(x['rivalItem1TradeIndex']['value'])
        form.append(text)
    form = np.array(form)
    return form
# 竞品关键词采集链接
def Keyword_competition(item_ip):
    result = parse.urlparse(item_ip)
    text = result.query.split("&")
    for x in text:
        x = x.split("=")
        if x[0] == "cateId":
            cateID = x[1]
        elif x[0] == 'rivalItem1Id':
            itemID = x[1]

    date = datetime.date.today()
    date = date - datetime.timedelta(days=1)
    date = date.strftime("%Y-%m-%d")
    dates = [date]
    for x in range(1,30):
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        date = date - datetime.timedelta(days=1)
        date = date.strftime("%Y-%m-%d")
        dates.append(date)
    IPS = []
    for x in dates:
        IP = "https://sycm.taobao.com/mc/rivalItem/analysis/getKeywords.json?dateRange="+x+"%7C"+x+"&dateType=day&pageSize=20&page=1&topType=flow&indexCode=uv&cateId="+str(cateID)+"&itemId="+str(itemID)+"&device=2&sellerType=0&_=1540178532790&token="
        IP1 = "https://sycm.taobao.com/mc/rivalItem/analysis/getKeywords.json?dateRange="+x+"%7C"+x+"&dateType=day&pageSize=20&page=1&topType=trade&indexCode=tradeIndex&cateId="+str(cateID)+"&itemId="+str(itemID)+"&device=2&sellerType=0&_=1540178532790&token="
        IPS.append(x)
        IPS.append("引流词")
        IPS.append(IP)
        IPS.append("成交词")
        IPS.append(IP1)
    IPS = np.array(IPS)
    IPS = IPS.reshape((30, 5))
    return IPS, cateID, itemID
# 竞品关键词解码 # 成交件数指数待还原
def Keyword_competition_Decode(data,cateID,item_ID):
    data = json.loads(data)["data"]
    form = []
    if data != []:
        if "uv" in data[0].keys():
            for x in data:
                text = []
                text.append(cateID)
                text.append("访客数")
                text.append(item_ID)
                text.append(x["keyword"]['value'])
                text.append(x['uv']['value'])
                text.append(0)
                form.append(text)
            form = np.array(form)
            return form
        else:
            for x in data:
                text = []
                text.append(cateID)
                text.append("成交件数")
                text.append(item_ID)
                text.append(x["keyword"]['value'])
                # 待还原指数
                text.append(x['tradeIndex']['value'])
                form.append(text)
            form = np.array(form)
            payment_piece = form[::, 4]
            payment_piece = Exponential_reduction_inside(payment_piece, "其他指数")
            form = np.hstack((form, payment_piece))
            return form

# 竞店构成采集链接生成
def shop_Commodity_composition(shop_ip, date, dateType):
    result = parse.urlparse(shop_ip)
    text = result.query.split("&")
    for x in text:
        x = x.split("=")
        if x[0] == "cateId":
            cateID = x[1]
        elif x[0] == 'rivalUser1Id':
            shop_ID = x[1]
    IPS = []
    IPS.append("热销商品构成:")
    IP = "https://sycm.taobao.com/mc/rivalShop/analysis/getTopItems.json?dateRange="+date[0]+"%7C"+date[1]+"&dateType="+dateType+"+&cateId="+cateID+"&device=0&userId="+shop_ID+"&indexCode=tradeIndex&topType=trade&_=1540178532790&token="
    IPS.append(IP)
    IPS.append("流量商品构成:")
    IP = "https://sycm.taobao.com/mc/rivalShop/analysis/getTopItems.json?dateRange="+date[0]+"%7C"+date[1]+"&dateType="+dateType+"+&cateId="+cateID+"&device=0&userId="+shop_ID+"&indexCode=uvIndex&topType=flow&_=1540178532790&token="
    IPS.append(IP)
    IPS.append("类目构成:")
    IP = "https://sycm.taobao.com/mc/rivalShop/analysis/getCateConstitute.json?dateRange="+date[0]+"%7C"+date[1]+"&dateType="+dateType+"+&cateId="+cateID+"&device=0&userId="+shop_ID+"&indexCode=uvIndex&topType=flow&_=1540178532790&token="
    IPS.append(IP)
    IPS.append("价格带构成:")
    IP = "https://sycm.taobao.com/mc/rivalShop/analysis/getPriceSegConstitute.json?device=2&userId="+shop_ID+"&cateId="+cateID+"&dateType="+dateType+"&dateRange="+date[0]+"%7C"+date[1]+"&_=1544597636600&token="
    IPS.append(IP)
    IPS.append("入店来源:")
    IP = "https://sycm.taobao.com/mc/rivalShop/analysis/getFlowSource.json?dateRange="+date[0]+"%7C"+date[1]+"&dateType="+dateType+"&cateId="+cateID+"&device=2&selfUserId=&rivalUser1Id="+shop_ID+"&rivalUser2Id=&indexCode=uvIndex&orderBy=uvIndex&order=desc&_=1540178532790&token="
    IPS.append(IP)
    IPS = np.array(IPS).reshape((5,2))
    return IPS,cateID,shop_ID


# 竞店热销商品构成数据解码
def Commodity_composition_Decode(cateID,shop_ID,data,date):
    data = json.loads(data)["data"]
    mat = []
    for x in data:
        form = []
        form.append(cateID)
        form.append("竞店热销商品")
        form.append(date[0] + "~" + date[1])
        form.append(shop_ID)
        form.append(x['item']['title'])
        form.append("http:" + x['item']['detailUrl'])
        try:
            form.append(x['item']['discountPrice'])
        except KeyError:
            form.append(x['item']["-"])
        form.append(x['tradeIndex']['value'])
        form.append(x['tradeIndex']['cycleCrc'])
        mat.append(form)
    form = np.array(mat)
    Payment_amount = form[::, 7]
    Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
    form = np.hstack((form, Payment_amount))
    return form

# 竞店流量商品构成数据解码
def Flow_Commodity_Decode(cateID,shop_ID,data,date):
    data = json.loads(data)["data"]
    mat = []
    for x in data:
        form = []
        form.append(cateID)
        form.append("竞店流量商品")
        form.append(date[0] + "~" + date[1])
        form.append(shop_ID)
        form.append(x['item']['title'])
        form.append("http:" + x['item']['detailUrl'])
        try:
            form.append(x['item']['discountPrice'])
        except KeyError:
            form.append(x['item']["-"])
        form.append(x['uv']['value'])
        form.append(x['uv']['cycleCrc'])
        mat.append(form)
    form = np.array(mat)
    Visitor = form[::, 7]
    Visitor = Exponential_reduction_inside(Visitor, "其他指数")
    form = np.hstack((form, Visitor))
    return form

# 竞店类目构成数据解码
def Category_of_competition_Decode(cateID,shop_ID,data,date):
    data = json.loads(data)["data"]
    mat = []
    print(data[:-1])
    for x in data[:-1]:
        form = []
        form.append(cateID)
        form.append("竞店类目构成")
        form.append(date[0] + "~" + date[1])
        form.append(shop_ID)
        form.append(x['cateLevel1Name']['value'])
        form.append(x['cateId']['value'])
        form.append(x['cateName']['value'])
        form.append(x['cateLevel1Id']['value'])
        form.append(x['payAmtRatio']['ratio'])
        mat.append(form)
    x = data[-1]
    form = []
    form.append("类目构成")
    form.append(date[0] + "~" + date[1])
    form.append("未知分类")
    form.append("0")
    form.append(x['cateName']['value'])
    form.append("未知")
    form.append(x['payAmtRatio']['ratio'])
    mat.append(form)
    mat = np.array(mat)
    print(mat[0])
    return mat

# 竞店价格带构成数据解码
def Price_band_Decode(cateID,shop_ID,data,date):
    data = json.loads(data)["data"]
    mat = []
    for x in data[:-1]:
        form = []
        form.append(cateID)
        form.append("竞店价格带构成")
        form.append(date[0] + "~" + date[1])
        form.append(shop_ID)
        form.append(x['priceSegName']['value'])
        form.append(x['payAmtRatio']['ratio'])
        mat.append(form)
    mat = np.array(mat)
    return mat

# 竞店入店来源解码
def Trend_of_competition_product_Decode(cateID,shop_ID,data,date):
    data = json.loads(data)["data"]
    form = []
    for count in range(5):
        for x in data[count]['children']:
            if x['rivalShop1UvIndex']['value'] == 0.0:
                continue
                text = []
                form.append(cateID)
                form.append("竞店入店来源")
                form.append(date[0] + "~" + date[1])
                form.append(shop_ID)
                text.append(x['pageName']['value'])
                text.append(x['rivalShop1TradeIndex']['value'])
                text.append(x['rivalShop1UvIndex']['value'])
                text.append(x['rivalShop1PayByrCntIndex']['value'])
                text.append(x['rivalShop1PayRateIndex']['value'])
                form.append(text)
    form = np.array(form)
    Payment_amount = form[::, 5]
    Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
    Visitor = form[::, 6]
    Visitor = Exponential_reduction_inside(Visitor, "其他指数")
    payments_Number = form[::, 7]
    payments_Number = Exponential_reduction_inside(payments_Number, "其他指数")
    Paymen_Conversion_Rate = form[::, 8]
    Paymen_Conversion_Rate = Exponential_reduction_inside(Paymen_Conversion_Rate, "转化率指数")

    form = np.hstack((form, Payment_amount))
    form = np.hstack((form, Visitor))
    form = np.hstack((form, payments_Number))
    form = np.hstack((form, Paymen_Conversion_Rate))
    form = np.hstack((form, Payment_amount/payments_Number))
    print(form[0])
    return form

""" 竞争品牌分析"""

# 竞争品牌链接生成
def Competitive_brand(Brand_ip, date, dateType):
    date = Time_enerator(dateType, date)
    # print(Brand_ip)
    result = parse.urlparse(Brand_ip)
    text = result.query.split("&")
    for x in text:
        x = x.split("=")
        if x[0] == "cateId":
            cateID = x[1]
        elif x[0] == 'rivalBrand1Id':
            Brand_ID = x[1]
    data = []
    IPS = []
    IPS.append("热销TOP店铺榜:")
    IP = "https://sycm.taobao.com/mc/rivalBrand/analysis/getTopShops.json?dateRange=" + date[0] + "%7C" + date[1] + "&dateType="+ dateType+"&pageSize=10&page=1&order=desc&brandId="+Brand_ID+"&topType=trade&device=0&sellerType=-1&cateId=" + cateID +"&indexCode=tradeIndex%2CtradeGrowthRange%2CpayRateIndex&_=1544757054113&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("流量TOP店铺榜:")
    IP = "https://sycm.taobao.com/mc/rivalBrand/analysis/getTopShops.json?dateRange=" + date[0] + "%7C" + date[1] + "&dateType="+ dateType+"&pageSize=10&page=1&order=desc&brandId="+Brand_ID+"&topType=flow&device=0&sellerType=-1&cateId=" + cateID +"&indexCode=uvIndex%2CseIpvUvHits%2CtradeIndex&_=1544757054113&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("热销TOP商品榜:")
    IP = "https://sycm.taobao.com/mc/rivalBrand/analysis/getTopItems.json?dateRange=" + date[0] + "%7C" + date[1] + "&dateType="+ dateType+"&pageSize=100&page=1&order=desc&brandId="+Brand_ID+"&topType=trade&device=0&sellerType=-1&cateId=" + cateID +"&indexCode=tradeIndex%2CtradeGrowthRange%2CpayRateIndex&_=1544757811881&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("流量TOP商品榜:")
    IP = "https://sycm.taobao.com/mc/rivalBrand/analysis/getTopItems.json?dateRange=" + date[0] + "%7C" + date[1] + "&dateType="+ dateType+"&dateType=month&pageSize=100&page=1&order=desc&brandId="+Brand_ID+"&topType=flow&device=0&sellerType=-1&cateId=" + cateID +"&indexCode=uvIndex%2CseIpvUvHits%2CtradeIndex&_=1544757811881&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("类目构成:")
    IP = "https://sycm.taobao.com/mc/rivalBrand/analysis/getCateConstitute.json?dateRange=" + date[0] + "%7C" + date[1] + "&dateType="+ dateType+"&pageSize=10&page=1&order=desc&orderBy=payAmt&brandId="+Brand_ID+"&device=0&sellerType=-1&cateId=" + cateID +"&indexCode=payAmt%2Cuv%2CpayItemCnt%2CpaySlrCnt&_=1544757054860&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("年龄客群构成:")
    IP = "https://sycm.taobao.com/mc/ci/brand/crowd.json?cateId=" + cateID +"&diffBrandIds="+Brand_ID+",,&device=0&sellerType=-1&indexCode=payByrCntIndex&attrType=age&dateType=month&dateRange=" + date[0] + "%7C" + date[1] + "&_=1544763544426&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("年龄客群占比构成:")
    IP = "https://sycm.taobao.com/mc/ci/brand/crowd.json?cateId=" + cateID +"&diffBrandIds="+Brand_ID+",,&device=0&sellerType=-1&indexCode=payByrCntRate&attrType=age&dateType=month&dateRange=" + date[0] + "%7C" + date[1] + "&_=1544763544426&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("年龄交易指数构成:")
    IP = "https://sycm.taobao.com/mc/ci/brand/crowd.json?cateId=" + cateID +"&diffBrandIds="+Brand_ID+",,&device=0&sellerType=-1&indexCode=tradeIndex&attrType=age&dateType=month&dateRange=" + date[0] + "%7C" + date[1] + "&_=1544763544426&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("年龄支付转化率指数构成:")
    IP = "https://sycm.taobao.com/mc/ci/brand/crowd.json?cateId=" + cateID +"&diffBrandIds="+Brand_ID+",,&device=0&sellerType=-1&indexCode=payRateIndex&attrType=age&dateType=month&dateRange=" + date[0] + "%7C" + date[1] + "&_=1544763544426&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("性别客群构成:")
    IP = "https://sycm.taobao.com/mc/ci/brand/crowd.json?cateId=" + cateID +"&diffBrandIds="+Brand_ID+",,&device=0&sellerType=-1&indexCode=payByrCntIndex&attrType=gender&dateType=month&dateRange=" + date[0] + "%7C" + date[1] + "&_=1544763544426&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("性别客群占比构成:")
    IP = "https://sycm.taobao.com/mc/ci/brand/crowd.json?cateId=" + cateID +"&diffBrandIds="+Brand_ID+",,&device=0&sellerType=-1&indexCode=payByrCntRate&attrType=gender&dateType=month&dateRange=" + date[0] + "%7C" + date[1] + "&_=1544763544426&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("性别交易指数构成:")
    IP = "https://sycm.taobao.com/mc/ci/brand/crowd.json?cateId=" + cateID +"&diffBrandIds="+Brand_ID+",,&device=0&sellerType=-1&indexCode=tradeIndex&attrType=gender&dateType=month&dateRange=" + date[0] + "%7C" + date[1] + "&_=1544763544426&token="
    IPS.append(IP)
    data.append(IPS)
    IPS = []
    IPS.append("性别支付转化率指数构成:")
    IP = "https://sycm.taobao.com/mc/ci/brand/crowd.json?cateId=" + cateID +"&diffBrandIds="+Brand_ID+",,&device=0&sellerType=-1&indexCode=payRateIndex&attrType=gender&dateType=month&dateRange=" + date[0] + "%7C" + date[1] + "&_=1544763544426&token="
    IPS.append(IP)
    data.append(IPS)
    data = np.array(data)
    return data, Brand_ID,cateID

# 竞争品牌热销店铺解码
def compete_Brand_Tradeshop_top(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    for cow in data:
        try:
            mat = []
            mat.append(cateID)
            mat.append("竞品牌热销店铺排行")
            mat.append(date)
            mat.append(brand_id)
            mat.append(cow['shop']['title'])
            mat.append("https://" + cow['shop']['shopUrl'])
            mat.append(cow['shop']['userId'])
            mat.append(cow['tradeIndex']['value'])
            mat.append(cow['payRateIndex']['value'])
            mat.append(cow['tradeGrowthRange']['value'])
        except KeyError:
            print(cow)
            continue
        form.append(mat)
    form = np.array(form)
    Payment_amount = form[::, 8]
    Conversion_rate = form[::, 9]
    Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
    Conversion_rate = Exponential_reduction_inside(Conversion_rate, "转化率指数")
    form = np.hstack((form, Conversion_rate))
    form = np.hstack((form, Payment_amount))
    return form
# 竞争品牌流量店铺解码
def compete_Brand_flowshop_top(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    print(data[0])
    form = []
    for cow in data:
        try:
            mat = []
            mat.append(cateID)
            mat.append("竞品牌流量店铺排行")
            mat.append(date)
            mat.append(brand_id)
            mat.append(cow['shop']['title'])
            mat.append("https://" + cow['shop']['shopUrl'])
            mat.append(cow['shop']['userId'])
            mat.append(cow['seIpvUvHits']['value'])
            mat.append(cow['uvIndex']['value'])
            mat.append(cow['tradeIndex']['value'])
        except KeyError:
            continue
        form.append(mat)
    form = np.array(form)
    Search_number = form[::, 7]
    Visitor = form[::, 8]
    Sale = form[::, 9]
    Search_number = Exponential_reduction_inside(Search_number, "其他指数")
    Visitor = Exponential_reduction_inside(Visitor, "其他指数")
    Sale = Exponential_reduction_inside(Sale, "交易指数")
    form = np.hstack((form, Search_number))
    form = np.hstack((form, Visitor))
    form = np.hstack((form, Sale))

    return form
# 竞争品牌热销商品解码
def Competitive_Brand_Tradeshop_Commodities(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    print(data[0])
    form = []
    for cow in data:
        try:
            mat = []
            mat.append(cateID)
            mat.append("竞争品牌热销商品排行")
            mat.append(date)
            mat.append(brand_id)
            mat.append(cow['item']['title'])
            mat.append(cow['shop']['title'])
            mat.append(cow['shop']['userId'])
            mat.append("https://" + cow['item']['detailUrl'])
            mat.append(cow['item']['itemId'])
            mat.append(cow['tradeIndex']['value'])
            mat.append(cow['payRateIndex']['value'])
            mat.append(cow['tradeGrowthRange']['value'])
        except KeyError:
            print(cow)
            continue
        form.append(mat)
    form = np.array(form)
    form = np.array(form)
    Payment_amount = form[::, 9]
    Conversion_rate = form[::, 10]
    Payment_amount = Exponential_reduction_inside(Payment_amount, "交易指数")
    Conversion_rate = Exponential_reduction_inside(Conversion_rate, "转化率指数")
    form = np.hstack((form, Conversion_rate))
    form = np.hstack((form, Payment_amount))
    return form

# 竞争品牌流量商品解码
def Competitive_Brand_Flow_Commodities(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    for cow in data:
        try:
            mat = []
            mat.append(cateID)
            mat.append("竞争品牌流量商品排行")
            mat.append(date)
            mat.append(brand_id)
            mat.append(cow['item']['title'])
            mat.append(cow['shop']['title'])
            mat.append(cow['shop']['userId'])
            mat.append("https://" + cow['item']['detailUrl'])
            mat.append(cow['item']['itemId'])
            mat.append(cow['uvIndex']['value'])
            mat.append(cow['seIpvUvHits']['value'])
            mat.append(cow['tradeIndex']['value'])
        except KeyError:
            print(cow)
            continue
        form.append(mat)
    form = np.array(form)
    Search_number = form[::, 9]
    Visitor = form[::, 10]
    Sale = form[::, 11]
    Search_number = Exponential_reduction_inside(Search_number, "其他指数")
    Visitor = Exponential_reduction_inside(Visitor, "其他指数")
    Sale = Exponential_reduction_inside(Sale, "交易指数")
    form = np.hstack((form, Search_number))
    form = np.hstack((form, Visitor))
    form = np.hstack((form, Sale))
    # print(form)
    return form

# 竞争品牌类目构成
def Competitive_Brand_Category_Composition(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    print(data)
    for cow in data:
        try:
            mat = []
            mat.append(cateID)
            mat.append("竞争品牌类目构成")
            mat.append(date)
            mat.append(brand_id)

            mat.append(cow['brandId']['value'])
            mat.append(cow['payAmt']['ratio'])
            mat.append(cow['cateName'])
            mat.append(cow['uv']['ratio'])
            mat.append(cow['payItemCnt']['ratio'])
            mat.append(cow['paySlrCnt']['ratio'])
        except KeyError:
            print(cow)
            continue
        form.append(mat)
    form = np.array(form)
    return form

# 品牌年龄客群
def Brand_Age_Clients(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    names = ["18~24","25~29","30~34","35~39","40~49",">=50"]
    for x in data:
        for cow,name in zip(data[x], names):
            text = []
            text.append(cateID)
            text.append("品牌人群年龄构成")
            text.append("客群指数")
            text.append(date)
            text.append(brand_id)
            text.append(x)
            text.append(name)
            text.append(cow['value'])
            form.append(text)
    form = np.array(form)
    payments = form[::, 7]
    payments = Exponential_reduction_inside(payments, "其他指数")
    form = np.hstack((form, payments))
    return form
# 品牌年龄客群占比
def Brand_Age_Clients_Proportion(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    names = ["18~24","25~29","30~34","35~39","40~49",">=50"]
    for x in data:
        for cow,name in zip(data[x], names):
            text = []
            text.append(cateID)
            text.append("品牌人群年龄构成")
            text.append("客群占比")
            text.append(date)
            text.append(brand_id)
            text.append(x)
            text.append(name)

            text.append(cow['value'])
            form.append(text)
    form = np.array(form)

    return form

# 品牌年龄交易指数
def Brand_Age_Trading_index(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    names = ["18~24","25~29","30~34","35~39","40~49",">=50"]
    for x in data:
        for cow,name in zip(data[x], names):
            text = []
            text.append(cateID)
            text.append("品牌人群年龄构成")
            text.append("交易指数")
            text.append(date)
            text.append(brand_id)
            text.append(x)
            text.append(name)

            text.append(cow['value'])
            form.append(text)
    form = np.array(form)
    transaction = form[::, 7]
    transaction = Exponential_reduction_inside(transaction, "交易指数")
    form = np.hstack((form, transaction))
    print(form)
    return form
# 品牌年龄支付转化率
def Brand_Age_Payment_Conversion_Rate(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    names = ["18~24","25~29","30~34","35~39","40~49",">=50"]
    for x in data:
        for cow,name in zip(data[x], names):
            text = []
            text.append(cateID)
            text.append("品牌人群年龄构成")
            text.append("支付转化率")
            text.append(date)
            text.append(brand_id)
            text.append(x)
            text.append(name)

            text.append(cow['value'])
            form.append(text)
    form = np.array(form)
    Conversion_Rate = form[::, 7]
    Conversion_Rate = Exponential_reduction_inside(Conversion_Rate, "转化率指数")
    form = np.hstack((form, Conversion_Rate))
    return form
# 品牌性别客群指数
def Brand_Gender_Clients(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    names = ["男","女","未知"]
    for x in data:
        for cow,name in zip(data[x], names):
            text = []
            text.append(cateID)
            text.append("品牌人群年龄构成")
            text.append("客群指数")
            text.append(date)
            text.append(brand_id)
            text.append(x)
            text.append(name)
            text.append(cow['value'])
            form.append(text)
    form = np.array(form)
    payments = form[::, 7]
    payments = Exponential_reduction_inside(payments, "其他指数")
    form = np.hstack((form, payments))
    print(form)
    return form
# 品牌性别客群占比
def Brand_Gender_Clients_Proportion(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    names = ["男","女","未知"]
    for x in data:
        for cow,name in zip(data[x], names):
            text = []
            text.append(cateID)
            text.append("品牌人群年龄构成")
            text.append("客群占比")
            text.append(date)
            text.append(brand_id)
            text.append(x)
            text.append(name)

            text.append(cow['value'])
            form.append(text)
    form = np.array(form)
    return form
# 品牌性别交易指数
def Brand_Gender_Trading_index(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    names = ["男","女","未知"]
    for x in data:
        for cow,name in zip(data[x], names):
            text = []
            text.append(cateID)
            text.append("品牌人群年龄构成")
            text.append("交易指数")
            text.append(date)
            text.append(brand_id)
            text.append(x)
            text.append(name)

            text.append(cow['value'])
            form.append(text)
    form = np.array(form)
    transaction = form[::, 7]
    transaction = Exponential_reduction_inside(transaction, "交易指数")
    form = np.hstack((form, transaction))
    return form
# 品牌性别支付转化率
def Payment_Conversion_Rate(cateID,data,date,brand_id):
    data = json.loads(data)["data"]
    form = []
    names = ["男","女","未知"]
    for x in data:
        for cow,name in zip(data[x], names):
            text = []
            text.append(cateID)
            text.append("品牌人群年龄构成")
            text.append(date)
            text.append(brand_id)
            text.append(x)
            text.append(name)
            text.append("支付转化率")
            text.append(cow['value'])
            form.append(text)
    form = np.array(form)
    Conversion_Rate = form[::, 7]
    Conversion_Rate = Exponential_reduction_inside(Conversion_Rate, "转化率指数")
    form = np.hstack((form, Conversion_Rate))
    return form
"""
    采集类目器
    OneCateID = [["尿片/洗护/喂哺/推车床",50014812],["住宅家具",50014813]]
    Select_category = "尿片/洗护/喂哺/推车床"
    类目获取链接
    https://sycm.taobao.com/mc/common/getShopCate.json?leaf=true&edition=std,pro,vip&_=1544781219715&token=
"""

#获取所有的类目秘钥
# def Category_collection(data,mat):
#     data = json.loads(data)["data"]
#     form = mat
#     mat = []
#     cateid_bag = {}
#     for cow in str1:
#         for x in form:
#             if cow[0] == int(x[1]):
#                 # 接收cate_name
#                 text = []
#                 text.append(cow[7])
#                 text.append(x[0])
#                 text.append(cow[2])
#                 # 接收cateid
#                 cateid_bag[cow[7]] = cow[6]
#                 cateid_bag[x[0]] = cow[0]
#                 cateid_bag[cow[2]] = cow[1]
#         mat.append(text)
#     cateId_bag = []
#     for x in cateid_bag:
#         cateId_bag.append([x,cateid_bag[x]])
#     cateId_bag = np.array(cateId_bag)
#     ii = []
#     for x in mat:
#         if len(x) == 3:
#             ii.append(x)
#     mat = np.array(ii)
#     return mat,cateId_bag
# 获取一级类目秘钥
# def Collection_category_ID1(data):
#     if data != 0:
#         data = json.loads(data)["data"]
#         cateIDs = []
#         for cow in strs:
#             print(cow['cateId']['value'])
#             cateid = str(cow['cateId']['value'])
#             IP = "https://sycm.taobao.com/mc/mq/supply/deal/list.json?dateRange=2018-11-01%7C2018-11-30&dateType" \
#                  "=month&pageSize=10&page=1&order=desc&orderBy=tradeIndex&cateId=" + cateid + \
#                  "&device=0&sellerType=-1&indexCode=tradeIndex%2CtradeGrowthRange%2CpayAmtParentCateRate" \
#                  "%2CpayCntParentCateRate&_=1540178532790&token= "
#             cateIDs.append(IP)
#         return cateIDs
# 合并二级cateid
# def Merge_cateid2(aggregate):
#     form = []
#     for x in aggregate:
#         data = Class_two_Decode(x)
#         form.append(data)
#     if len(form) == 1:
#         return form[0]
#     else:
#         mat = form[0]
#         for x in form[1:]:
#             mat = np.vstack((mat, x))
#         return mat

# 获取一级类目的所有二级类目名
# def Class_two_Decode(data):
#     data = eval(data)["data"]
#     class_bag = []
#     for x in data:
#         text = []
#         text.append(x['cateBo']["cateName"].replace('\\', ''))
#         text.append(x['cateBo']['cateId'])
#         class_bag.append(text)
#     class_bag = np.array(class_bag)
#     return class_bag
if __name__ == '__main__':
    # -!- coding: utf-8 -!-
    import json
    import numpy as np
    import pandas as pd
    from pandas import DataFrame
    import re
    from urllib.parse import quote
    from urllib import request,parse
    import datetime
    import calendar
    import pickle
    key_word = "奶瓶"
    OneCateID = {
        "尿片/洗护/喂哺/推车床":50014812,
        "电子/电工":50020579
                }
    itemID = 524817325933
    shop_ID = 50014812
    Brand_ID = 20448
    shop_ip = "https://sycm.taobao.com/mc/ci/shop/analysis?cateFlag=1&cateId=50014812&dateRange=2018-12-01%7C2018-12-01&dateType=day&parentCateId=0&rivalUser1Id=174683470&rivalUser2Id=&spm=a21ag.11815275.LeftMenu.d1480.75df50a5YpOaEp"
    Brand_ip = "https://sycm.taobao.com/mc/ci/brand/analysis?cateFlag=1&cateId=50014812&dateRange=2018-12-12%7C2018-12-12&dateType=day&device=0&parentCateId=0&sellerType=-1&spm=a21ag.11815275.LeftMenu.d1498.195350a5veSjkS&rivalBrand2Id=&rivalBrand1Id=20448"
    dateType = "month"
    # 时间生成器
    # date = Time_enerator(dateType, date)
    data = 0
    one_type = "item"
    tow_type = "hotpurpose"
    cateID = 50009522
    date = '2018-11-01'
    Choice = "交易指数"










