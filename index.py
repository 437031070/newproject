import datetime

import numpy as np
from flask import Flask, render_template, request, make_response, redirect, Response,session
import BI
from flask_sqlalchemy import SQLAlchemy
import pymysql
import json
# from urllib.parse import quote
# from urllib import request,parse
np.set_printoptions(suppress=True)
pymysql.install_as_MySQLdb()
from pandas import DataFrame

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:123456@localhost/bi"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SECRET_KEY']="SASDAS"
db = SQLAlchemy(app)


#映射数据库表
#行业构成表
class Industry_composition(db.Model):
    __tablename__ = 'industry_composition'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Industry_composition = db.Column(db.String(40))
    date = db.Column(db.String(40))
    cateName = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    tradeGrowthRange = db.Column(db.String(40))
    payAmtParentCateRate = db.Column(db.String(40))
    payCntParentCateRate = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# #子行业分布表
class Subindustry_Distribution(db.Model):
    __tablename__ = 'subindustry_distribution'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    cateName = db.Column(db.String(40))
    slrCnt = db.Column(db.String(40))
    parentCateSlrRate = db.Column(db.String(40))
    tradeSlrCnt = db.Column(db.String(40))
    parentCateTradeSlrCntRate = db.Column(db.String(40))
# # #高流量店铺排行
class Shop_hotsearch(db.Model):
    __tablename__ = 'shop_hotsearch'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    shop_title = db.Column(db.String(40))
    cateRankId = db.Column(db.String(40))
    userId = db.Column(db.String(40))
    shopUrl = db.Column(db.String(40))
    b2CShop = db.Column(db.String(40))
    uvIndex = db.Column(db.String(40))
    seIpvUvHits = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    Search = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
    Visitor = db.Column(db.String(40))
# # #高交易店铺排行表
class Shop_hotsale(db.Model):
    __tablename__ = 'shop_hotsale'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    shop_title = db.Column(db.String(40))
    cateRankId = db.Column(db.String(40))
    userId = db.Column(db.String(40))
    shopUrl = db.Column(db.String(40))
    b2CShop = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    payRateIndex = db.Column(db.String(40))
    Conversion_rate = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# # #高流量商品排行
class Item_hotsearch(db.Model):
    __tablename__ = 'item_hotsearch'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    item_title = db.Column(db.String(40))
    itemId = db.Column(db.String(40))
    detailUrl = db.Column(db.String(40))
    cateRankId = db.Column(db.String(40))
    shop_title = db.Column(db.String(40))
    userId = db.Column(db.String(40))
    shopUrl = db.Column(db.String(40))
    uvIndex = db.Column(db.String(40))
    seIpvUvHits = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    Search = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
    Visitor = db.Column(db.String(40))
# # #高交易商品排行
class Item_hotsale(db.Model):
    __tablename__ = 'item_hotsale'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    item_title = db.Column(db.String(40))
    itemId = db.Column(db.String(40))
    detailUrl = db.Column(db.String(40))
    cateRankId = db.Column(db.String(40))
    shop_title = db.Column(db.String(40))
    userId = db.Column(db.String(40))
    shopUrl = db.Column(db.String(40))
    payRateIndex = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    Conversion_rate = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# # #高意向商品排行表
class item_hotpurpose(db.Model):
    __tablename__ = 'item_hotpurpose'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    item_title = db.Column(db.String(40))
    itemId = db.Column(db.String(40))
    detailUrl = db.Column(db.String(40))
    cateRankId = db.Column(db.String(40))
    shop_title = db.Column(db.String(40))
    userId = db.Column(db.String(40))
    shopUrl = db.Column(db.String(40))
    cltHits = db.Column(db.String(40))
    cartHits = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    Collection = db.Column(db.String(40))
    Shopping_Cart = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# # #高流量品牌排行表
class Brand_hotsearch(db.Model):
    __tablename__ = 'brand_hotsearch'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brandName = db.Column(db.String(40))
    brandId = db.Column(db.String(40))
    cateRankId = db.Column(db.String(40))
    uvIndex = db.Column(db.String(40))
    seIpvUvHits = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    Visitor = db.Column(db.String(40))
    Search = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# # #高交易品牌排行表
class Brand_hotsale(db.Model):
    __tablename__ = 'brand_hotsale'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brandName = db.Column(db.String(40))
    brandId = db.Column(db.String(40))
    cateRankId = db.Column(db.String(40))
    payRateIndex = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    Conversion_rate = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# # #热门属性表
class Hot_attributes(db.Model):
    __tablename__ = 'hot_attributes'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    payments_piece = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    Sale = db.Column(db.String(40))
# # #搜索词排行表
class Search_terms(db.Model):
    __tablename__ = 'search_terms'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    searchWord = db.Column(db.String(40))
    hotSearchRank = db.Column(db.String(40))
    seIpvUvHits = db.Column(db.String(40))
    clickHits = db.Column(db.String(40))
    clickRate = db.Column(db.String(40))
    payRate = db.Column(db.String(40))
    p4pRefPrice = db.Column(db.String(40))
    tmClickRate = db.Column(db.String(40))
    search = db.Column(db.String(40))
    click = db.Column(db.String(40))
# # #品牌词排行表
class Brand_Word(db.Model):
    __tablename__ = 'brand_Word'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    searchWord = db.Column(db.String(40))
    hotSearchRank = db.Column(db.String(40))
    relSeWordCnt = db.Column(db.String(40))
    avgWordSeIpvUvHits = db.Column(db.String(40))
    avgWordClickHits = db.Column(db.String(40))
    p4pRefPrice = db.Column(db.String(40))
    search = db.Column(db.String(40))
    click = db.Column(db.String(40))
# #
# # #修饰词排行表
class Modifiers_Word(db.Model):
    __tablename__ = 'modifiers_Word'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    searchWord = db.Column(db.String(40))
    hotSearchRank = db.Column(db.String(40))
    relSeWordCnt = db.Column(db.String(40))
    avgWordSeIpvUvHits = db.Column(db.String(40))
    avgWordClickHits = db.Column(db.String(40))
    p4pRefPrice = db.Column(db.String(40))
    search = db.Column(db.String(40))
    click = db.Column(db.String(40))
# # #核心词排行
class Core_word(db.Model):
    __tablename__ = 'core_word'
    id = db.Column(db.Integer,primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    searchWord = db.Column(db.String(40))
    hotSearchRank = db.Column(db.String(40))
    relSeWordCnt = db.Column(db.String(40))
    avgWordSeIpvUvHits = db.Column(db.String(40))
    avgWordClickHits = db.Column(db.String(40))
    p4pRefPrice = db.Column(db.String(40))
    search = db.Column(db.String(40))
    click = db.Column(db.String(40))
# # #搜索分析表
class Search_analysis30(db.Model):
    __tablename__ = 'search_analysis30'
    id = db.Column(db.Integer,primary_key=True)
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    word = db.Column(db.String(40))
    keyword = db.Column(db.String(40))
    seIpvUvHits = db.Column(db.String(40))
    spvRatio = db.Column(db.String(40))
    sePvIndex = db.Column(db.String(40))
    clickRate = db.Column(db.String(40))
    clickHits = db.Column(db.String(40))
    clickHot = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    payConvRate = db.Column(db.String(40))
    onlineGoodsCnt = db.Column(db.String(40))
    tmClickRatio = db.Column(db.String(40))
    p4pAmt = db.Column(db.String(40))
    Search_frequency = db.Column(db.String(40))
    click_Popularity = db.Column(db.String(40))
    click_Number = db.Column(db.String(40))
    click_Popularity = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# # #地域分析表
class Geographical_distribution(db.Model):
    __tablename__ = 'geographical_distribution'
    id = db.Column(db.Integer,primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    areaName = db.Column(db.String(40))
    slrCnt = db.Column(db.String(40))
    parentCateSlrRate = db.Column(db.String(40))
    tradeSlrCnt = db.Column(db.String(40))
    parentCateTradeSlrCntRate = db.Column(db.String(40))
# # #竞品入店来源表
class Source_of_entry_product(db.Model):
    __tablename__ = 'source_of_entry_product'
    id = db.Column(db.Integer,primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    itemID = db.Column(db.String(40))
    pageName = db.Column(db.String(40))
    rivalItem1PayByrCntIndex = db.Column(db.String(40))
    uv = db.Column(db.String(40))
    rivalItem1PayRateIndex = db.Column(db.String(40))
    rivalItem1TradeIndex = db.Column(db.String(40))
# # #竞品关键词表
# #=======================
class Keyword_competition(db.Model):
    __tablename__ = 'keyword_competition'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    item_ID = db.Column(db.String(40))
    keyword = db.Column(db.String(40))
    type_ = db.Column(db.String(40))
    real = db.Column(db.String(40))
# # #竞店热销商品构成表
# #===========================================
class Commodity_composition(db.Model):
    __tablename__ = 'commodity_composition'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    shop_ID = db.Column(db.String(40))
    item_title = db.Column(db.String(40))
    item_detailUrl = db.Column(db.String(40))
    discountPrice = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    tradeIndex_cycleCrc = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# # #竞店流量商品构成表
class Flow_Commodity(db.Model):
    __tablename__ = 'flow_Commodity'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    shop_ID = db.Column(db.String(40))
    item_title = db.Column(db.String(40))
    item_detailUrl = db.Column(db.String(40))
    discountPrice = db.Column(db.String(40))
    uv = db.Column(db.String(40))
    uv_cycleCrc = db.Column(db.String(40))
    Visitor = db.Column(db.String(40))
# 竞店类目构成表
class Category_of_competition(db.Model):
    __tablename__ = 'category_of_competition1'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    shop_ID = db.Column(db.String(40))
    cateLevel1Name = db.Column(db.String(40))
    cate_Id = db.Column(db.String(40))
    cateName = db.Column(db.String(40))
    cateLevel1Id = db.Column(db.String(40))
    payAmtRatio = db.Column(db.String(40))


# # #竞店价格带构成表
class Price_band(db.Model):
    __tablename__ = 'price_band'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    shop_ID = db.Column(db.String(40))
    priceSegName = db.Column(db.String(40))
    payAmtRatio = db.Column(db.String(40))
# # #竞店入店来源表
class Trend_of_competition_product(db.Model):
    __tablename__ = 'trend_of_competition_product'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    shop_ID = db.Column(db.String(40))
    priceSegName = db.Column(db.String(40))
    rivalShop1TradeIndex = db.Column(db.String(40))
    rivalShop1UvIndex = db.Column(db.String(40))
    rivalShop1PayByrCntIndex = db.Column(db.String(40))
    rivalShop1PayRateIndex = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
    Visitor = db.Column(db.String(40))
    payments_Number = db.Column(db.String(40))
    Paymen_Conversion_Rate = db.Column(db.String(40))
    Customer_unit_price = db.Column(db.String(40))
# # #品牌热销店铺表
class Compete_Brand_Tradeshop_top(db.Model):
    __tablename__ = 'compete_Brand_Tradeshop_top'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    shop_title = db.Column(db.String(40))
    shopUrl = db.Column(db.String(40))
    userId = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    payRateIndex = db.Column(db.String(40))
    tradeGrowthRange = db.Column(db.String(40))
    Conversion_rate = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# # #品牌流量店铺表
class Compete_Brand_flowshop_top(db.Model):
    __tablename__ = 'compete_Brand_flowshop_top'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    shop_title = db.Column(db.String(40))
    shopUrl = db.Column(db.String(40))
    userId = db.Column(db.String(40))
    seIpvUvHits = db.Column(db.String(40))
    uvIndex = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    Search_number = db.Column(db.String(40))
    Visitor = db.Column(db.String(40))
    Sale = db.Column(db.String(40))
# # #品牌热销商品表
class Competitive_Brand_Tradeshop_Commodities(db.Model):
    __tablename__ = 'competitive_Brand_Tradeshop_Commodities'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    item_title = db.Column(db.String(40))
    shop_title = db.Column(db.String(40))
    userId = db.Column(db.String(40))
    item_detailUrl = db.Column(db.String(40))
    itemId = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    payRateIndex = db.Column(db.String(40))
    tradeGrowthRange = db.Column(db.String(40))
    Conversion_rate = db.Column(db.String(40))
    Payment_amount = db.Column(db.String(40))
# #品牌流量商品表
class Competitive_Brand_Flow_Commodities(db.Model):
    __tablename__ = 'competitive_Brand_Flow_Commodities'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    item_title = db.Column(db.String(40))
    shop_title = db.Column(db.String(40))
    userId = db.Column(db.String(40))
    item_detailUrl = db.Column(db.String(40))
    itemId = db.Column(db.String(40))
    uvIndex = db.Column(db.String(40))
    seIpvUvHits = db.Column(db.String(40))
    tradeIndex = db.Column(db.String(40))
    Search_number = db.Column(db.String(40))
    Visitor = db.Column(db.String(40))
    Sale = db.Column(db.String(40))
# # #品牌类目构成表
class Competitive_Brand_Category_Composition(db.Model):
    __tablename__ = 'competitive_Brand_Category_Composition'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    brandIds = db.Column(db.String(40))
    payAmt_ratio = db.Column(db.String(40))
    cateName = db.Column(db.String(40))
    uv_ratio = db.Column(db.String(40))
    payItemCnt = db.Column(db.String(40))
    paySlrCnt = db.Column(db.String(40))
# # #品牌年龄客群表
class Brand_Age_Clients(db.Model):
    __tablename__ = 'brand_Age_Clients'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    Customer_index = db.Column(db.String(40))
    name = db.Column(db.String(40))
    text = db.Column(db.String(40))
    payments = db.Column(db.String(40))
# # #品牌年龄客群占比表
class Brand_Age_Clients_Proportion(db.Model):
    __tablename__ = 'brand_Age_Clients_Proportion'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    Customer_index = db.Column(db.String(40))
    name = db.Column(db.String(40))
    text = db.Column(db.String(40))
# # #品牌年龄交易指数表
class Brand_Age_Trading_index(db.Model):
    __tablename__ = 'brand_Age_Trading_index'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    Customer_index = db.Column(db.String(40))
    name = db.Column(db.String(40))
    text = db.Column(db.String(40))
    transaction = db.Column(db.String(40))
# # #品牌年龄支付转化率表
class Brand_Age_Payment_Conversion_Rate(db.Model):
    __tablename__ = 'brand_Age_Payment_Conversion_Rate'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    Customer_index = db.Column(db.String(40))
    name = db.Column(db.String(40))
    text = db.Column(db.String(40))
    Conversion_Rate = db.Column(db.String(40))
# # # 品牌性别客群指数表
# #
class Brand_Gender1_Clients(db.Model):
    __tablename__ = 'brand_Gender_Clients'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    Customer_index = db.Column(db.String(40))
    name = db.Column(db.String(40))
    text = db.Column(db.String(40))
    payments = db.Column(db.String(40))
# # # 品牌性别客群占比
class Brand_Gender_Clients_Proportion(db.Model):
    __tablename__ = 'brand_Gender_Clients_Proportion'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    Customer_index = db.Column(db.String(40))
    name = db.Column(db.String(40))
    text = db.Column(db.String(40))
# # #品牌性别交易指数表
# #========================================
#
class Brand_Gender_Clients_Proportion_one(db.Model):
    __tablename__ = 'brand_Gender_Clients_Proportion_one'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module_one = db.Column(db.Integer)
    data_type_one = db.Column(db.Integer)
    date_one = db.Column(db.Integer)
    brand_id_one = db.Column(db.Integer)
    Customer_index1_one = db.Column(db.Integer)
    name_one = db.Column(db.Integer)
    text_one = db.Column(db.Integer)


# # #品牌性别支付转化率表
# #
class Brand_Gender_Clients_two(db.Model):
    __tablename__ = 'brand_Gender_Clients_two'
    id = db.Column(db.Integer, primary_key=True)
    cateID = db.Column(db.String(40))
    Data_module = db.Column(db.String(40))
    data_type = db.Column(db.String(40))
    date = db.Column(db.String(40))
    brand_id = db.Column(db.String(40))
    Customer_index = db.Column(db.String(40))
    name = db.Column(db.String(40))
    text = db.Column(db.String(40))
    Conversion_Rate = db.Column(db.String(40))


db.create_all()






#ZB
@app.route("/")
def index_view():
    return render_template("zB.html")

# 首页
@app.route("/index",methods=["POST","GET"])
def main_index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        #框里的值
        data = request.form.get("shuju")
        print(data)
        #下拉框的值
        Choice = request.form.get("xiala")
        print(Choice)
        dic = []
        data = BI.Exponential_reduction(data,Choice)
        for x, y in zip(data,range(len(data))):
            text = {}
            text["encryption_index"] = x[0]
            text["True_value"] = x[1]
            dic.append(text)
        print(dic)
        jsonStr = json.dumps(dic)
        return jsonStr
# 一级功能类目选项

@app.route("/gn1", methods=["POST", "GET"])
def gn1():
    if request.method == "GET":
        return render_template("gn1.html")
    else:
        # 得到所有一级大盘类目数据
        udata = request.form.get("text", "")
        # print(udata)
        IPS = BI.Collection_category_ID1(udata)
        dic = {}

        for x in IPS:
            dic[x] = 0
        ip = "https://sycm.taobao.com/mc/common/getShopCate.json?leaf=true&edition=std,pro,vip&_=1544781219715&token="
        return render_template("gn1.html", l=dic, lianjie=ip)


# 二级功能类型选项
# @app.route("/gn2", methods=["POST"])
# def gn2():
#     l = []
#     mat = []
#     data = request.form.get("text2")
#     l.append(data)
#     data1 = request.form.get("text3")
#     l.append(data1)
#     data2 = request.form.get("text4")
#     l.append(data2)
#     for x in l:
#         if x != "":
#             mat.append(x)
#     mat = BI.Merge_cateid2(mat)
#     data = request.form.get("text5")
#     cate_name,cateid = BI.Category_collection(data, mat)
#
#     for x in cateid:
#         cate_id_add_sql(x[0],int(x[1]))
#     for y in cate_name:
#         cate_name_add_sql(y[0],y[1],y[2])
#
#     return render_template("gn1.html")
#行业构成
@app.route("/gn3", methods=["POST","GET"])
def gn3():
    if request.method == "GET":
        return render_template("gn2.html")
    else:
        # try:
        cateid = request.form.get("cateId")
        Industry_type = request.form.get("Industry_type")
        IPS = BI.Industry_market(cateid, Industry_type)
        ips = list(IPS.values())
        dates = list(IPS.keys())
        dic = {}
        if request.form.get("data1") or request.form.get("data2") or request.form.get("data3") or request.form.get("data4") or request.form.get("data5") or request.form.get("data6") or request.form.get("data7") or request.form.get("data8") or request.form.get("data9") or request.form.get("data10") or request.form.get("data11") or request.form.get("data12"):
            for x in range(1,13):
                Industry_type = request.form.get("Industry_type")
                cateid = request.form.get("cateId")
                time = request.form.get("time" + str(x))
                data = request.form.get("data" + str(x))
                if data != "":
                    dic[time]= data

            for x in dic:
                if Industry_type == "行业交易构成":
                    date = x
                    data = dic[x]
                    form = BI.Industry_composition_Decode(date, data, cateid)
                    for cow in form:
                        print(len(cow))
                        data = Industry_composition(cateID=cow[0],Industry_composition=cow[1],date=cow[2],cateName=cow[3],tradeIndex=cow[4],tradeGrowthRange=cow[5],payAmtParentCateRate=cow[6],payCntParentCateRate=cow[7],Payment_amount=cow[8])
                        db.session.add(data)
                        db.session.commit()
                elif Industry_type == "卖家分布":
                    date = x
                    data = dic[x]
                    form = BI.seller_composition_Decode(date,data,cateid)

        # except:
        #     return render_template("Error.html")

        return render_template("gn2.html",ips=IPS,dates=dates,cateid=cateid,Industry_type=Industry_type)
#/hn
@app.route("/hn",methods=["POST","GET"])
def hn_show():
    if request.method == "GET":
        return render_template("gn3.html")
    else:
        try:
            cateid = request.form.get("cateId")
            Industry_type = request.form.get("Industry_type")
            Industry_type2 = request.form.get("Industry_type2")
            if Industry_type == "商品":
                Industry_type = "item"
                if Industry_type2 == "高交易":
                    Industry_type2 = "hotsale"
                elif Industry_type2 == "高流量":
                    Industry_type2 = "hotsearch"
                elif Industry_type2 == "高意向":
                    Industry_type2 = "hotpurpose"
            elif Industry_type == "店铺":
                Industry_type = "shop"
                if Industry_type2 == "高交易":
                    Industry_type2 = "hotsale"
                elif Industry_type2 == "高流量":
                    Industry_type2 = "hotsearch"
            elif Industry_type == "品牌":
                Industry_type = "brand"
                if Industry_type2 == "高交易":
                    Industry_type2 = "hotsale"
                elif Industry_type2 == "高流量":
                    Industry_type2 = "hotsearch"
            IPS = BI.Store_ranking(cateid,Industry_type2,Industry_type)
            ips = list(IPS.values())
            dates = list(IPS.keys())
            dic = {}
            if request.form.get("data1") or request.form.get("data2") or request.form.get("data3") or request.form.get("data4") or request.form.get("data5") or request.form.get("data6") or request.form.get("data7") or request.form.get("data8") or request.form.get("data9") or request.form.get("data10") or request.form.get("data11") or request.form.get("data12"):
                for x in range(1,13):
                    print(x)
                    Industry_type = request.form.get("Industry_type")

                    cateid = request.form.get("cateId")

                    Industry_type2 = request.form.get("Industry_type2")
                    time = request.form.get("time" + str(x))
                    print(time)
                    data = request.form.get("data" + str(x))
                    print(data)
                    if data != "":
                        dic[time]= data

                mat = []
                for x in dic:
                    date = x
                    data = dic[x]
                    form = BI.Industry_ranking_Data_decoding(date,cateid,data,Industry_type,Industry_type2)
                    mat.append(form)
                form_start = mat[0]

                if len(mat) > 1:
                    for form in mat[1:]:

                        form_start = np.vstack((form_start,form))
        except:
            return render_template("Error.html")

        return render_template("gn3.html",ips=IPS,dates=dates,cateid=cateid,Industry_type=Industry_type,Industry_type2=Industry_type2)

#下拉
@app.route("/xl_qz",methods=["POST","GET"])
def xiala_views():
    if request.method=="POST":
        data1 = request.form.get('data1')
        print(data1)
        if data1 == "店铺":
            str = "<option>高交易</option><option>高流量</option>"
            return str
        elif data1 =="品牌":
            str = "<option>高交易</option><option>高流量</option>"
            return str
        elif data1 == "商品":
            str = " <option>高交易</option><option>高流量</option><option>高意向</option>"
            return str

#热门属性
@app.route("/Attribute",methods=["GET","POST"])
def attribute_views():
    if request.method=="GET":
        return render_template("Attribute.html")
    else:
        try:
            attribute_ip = request.form.get("data1")
            data = request.form.get("data2")
            data = BI.Hot_attributes(data, attribute_ip)
            #热门属性存入数据库

        except:
            return render_template("Error.html")
        return render_template("Attribute.html",data1=attribute_ip)

#搜索排行
@app.route("/Search_area",methods=["POST","GET"])
def Search_area_views():
    if request.method=="GET":
        return render_template("Search_ranking.html")
    else:
        cateId = request.form.get("cateId")
        session["cateId"]=cateId
        IPS = BI.Search_terms(cateId)
        IPS1 = BI.geographical_distribution(cateId)
        return render_template("Search_ranking.html",IPS=IPS,IPS1=IPS1,cateId=cateId)
#搜索排行 框内提取值
@app.route("/extract_Search_area",methods=["POST","GET"])
def extract():
    if request.method=="POST":
        try:
            cateId = session['cateId']
            print(cateId)
            keyword = {}

            Search_terms = request.form.get("data1")
            # 得到搜索词
            if Search_terms:
                data = BI.Search_terms_Decode(cateId,Search_terms)
                # 待存入数据库
            brand_Word = request.form.get("data2")
            # 得到品牌词
            if brand_Word:
                data = BI.brand_Word_Decode(cateId,brand_Word)
                # 待存入数据库
            Core_word = request.form.get("data3")
            if Core_word:
                data = BI.Core_word_Decode(cateId, Core_word)
            Modifiers = request.form.get("data4")
            if Modifiers:
                data = BI.Modifiers_Decode(cateId, Modifiers)
            analysis = request.form.get("data5")
            if analysis:
                keyword["地狱分析"] = analysis
        except:
            return render_template("Error.html")

        return render_template("Search_ranking.html",cateId=cateId)

#搜索分析
@app.route("/Analysis",methods=["POST","GET"])
def Analysis_views():
    if request.method == "GET":
        return render_template("Analysis.html")
    else:
        try:
            #接收前端的关键词
            key_word = request.form.get("data")
            session['key_word']=key_word

            #调用BI
            IPS = BI.Search_analysis30(key_word)
        except:
            return render_template("Error.html")

        return render_template("Analysis.html",IPS=IPS)
#接收搜索分析返回框内值
@app.route("/Fh_Anl",methods=["POST","GET"])
def Fh_anl_views():
    if request.method == "POST":
        try:
            key_word = session.get('key_word')

            return_val = request.form.get("data1")

            data = BI.Search_analysis30_Decode(key_word,return_val)
        except:
            return render_template("Error.html")

            #存入数据库
        return render_template("Analysis.html")
#竞店分析
@app.route("/Race_shop",methods=["POST","GET"])
def Race_views():
    if request.method=="GET":
        dates = ["最近30天"]
        date_name = BI.one_year_enerator()
        for date in date_name:
            dates.append(date[0])
        return render_template("Race_shop.html",dates=dates)
    else:
        try:
            dates = ["最近30天"]
            date_name = BI.one_year_enerator()
            for date in date_name:
                dates.append(date[0])
            #竞店IP
            shop_ip = request.form.get('data2')
            session["shop_ip"]=shop_ip
            #时间
            date = request.form.get('data3')
            if date != "最近30天":
                dateType = "month"
                date = BI.Time_enerator(dateType, date)

            else:
                dateType = "recent30"
                date = BI.Time_enerator(dateType, date)
            session["date"]=date
            IPS,cateID,shopID = BI.shop_Commodity_composition(shop_ip,date,dateType)
            session['cateID']=cateID
            session['shopID']=shopID
            IPS_bag = {}
            for x in IPS:
                IPS_bag[x[0]] = x[1]
            print(IPS_bag)
        except:
            return render_template("Error.html")
        return render_template("Race_shop.html",dates=dates,IPS=IPS_bag,date=date,shop_ip=shop_ip)
#提取竞店分析框内值
@app.route("/addRace_shop",methods=["POST","GET"])
def addRace_shop_views():
    if request.method == "POST":
        try:

            shop_ip=session.get("shop_ip")
            dates = ["最近30天"]
            date_name = BI.one_year_enerator()
            for date in date_name:
                dates.append(date[0])
            date = session.get("date")
            cateID = session.get['cateID']
            shopID = session.get['shopID']
            if request.form.get("x1") or request.form.get("x2") or request.form.get("x3") or request.form.get("x4") or request.form.get("x5"):
                if request.form.get("x1"):
                    data1=request.form.get("x1")
                    data1=BI.Commodity_composition_Decode(cateID,shopID,data1,date)
                    print(data1)
                    #待存入数据库
                elif request.form.get("x2"):
                    data2 = request.form.get("x2")
                    data1 = BI.Commodity_composition_Decode(cateID,shopID,data2, date)
                elif request.form.get("x3"):
                    data3 = request.form.get("x3")
                    data1 = BI.Commodity_composition_Decode(cateID,shopID,data3, date)
                elif request.form.get("x4"):
                    data4 = request.form.get("x4")
                    data1 = BI.Commodity_composition_Decode(cateID,shopID,data4, date)
                elif request.form.get("x5"):
                    data5 = request.form.get("x5")
                    data1 = BI.Trend_of_competition_product_Decode(cateID,shopID,data5, date)
        except:
            return render_template("Error.html")
        return render_template("Race_shop.html",dates=dates,shop_ip=shop_ip)

#竞品分析
@app.route("/Competing_goods",methods=["POST","GET"])
def Competing_goods_views():
    if request.method=="GET":
        return render_template("Competing_goods.html")
    else:
        try:
            # cateID = request.form.get("cateId")
            item_ip = request.form.get("IP")
            #此data是ips
            data,cate_ID,item_ID = BI.Keyword_competition(item_ip)
            session["cate_ID"] = cate_ID
            session["item_ID"] = item_ID
            words = []
            for cow in data:
                text = {}
                text['时间'] = cow[0]
                text[cow[1]] = cow[2]
                text[cow[3]] = cow[4]
                words.append(text)
            print(words)
        except:
            return render_template("Error.html")
        return render_template("Competing_goods.html",words=words)

#接受 竞品60条数据
@app.route("/Competing",methods=["POST","GET"])
def Competing_views():
    if request.method=="POST":
        try:
            for x in range(1,61):
                if request.form.get("x"+str(x)):
                    data = request.form.get("x"+str(x))
                    cate_ID = session.get['cate_ID']
                    item_ID = session.get['item_ID']
                    data = BI.Keyword_competition_Decode(data,cate_ID,item_ID)
                    #待传入数据库
        except:
            return render_template("Error.html")
        return render_template("Competing_goods.html")
# 竞品2
@app.route("/Competing_goods2",methods=["POST","GET"])
def Competing_goodsviews():
    if request.method=="GET":
        return render_template("Competing_goods2.html")
    else:
        try:
            item_ip = request.form.get("IP")

            data, cateID,item_ID = BI.Source_of_entry_product(item_ip)
            session["cateID"] = cateID
            session["itemID"] = item_ID
        except:
            return render_template("Error.html")

        return render_template("Competing_goods2.html",data=data)
#接收竞2框内值
@app.route("/goods2",methods=["POST","GET"])
def goods_views():
    if request.method=="POST":

        try:
            if request.form.get("data1") or request.form.get("data2") or request.form.get("data3") or request.form.get("data4") or request.form.get("data5") or request.form.get("data6") or request.form.get("data7") or request.form.get("data8") or request.form.get("data9") or request.form.get("data10") or request.form.get("data11") or request.form.get("data12") or request.form.get("data13"):

                for x in range(1,14):

                    print(x)
                    #提取cateID
                    cateID = session.get('cateID')
                    print(cateID)
                    #提取ID
                    itemID = session.get("itemID")
                    #提取时间值

                    times = request.form.get("time"+str(x))

                    #提取框内值
                    if request.form.get("data"+str(x)):
                        datas = request.form.get("data"+str(x))
                        print(itemID)
                        print(cateID)

                        print(times)
                        print(datas)
                        data = BI.Source_of_entry_product_Decode(cateID,itemID,datas,times)
                        print(data)

                        # 交接逻辑 存入数据库
        except:
            return render_template("Error.html")
        return render_template("Competing_goods2.html")

#竞品牌分析

@app.route("/brand",methods=["POST","GET"])
def Compeviews():
    if request.method=="GET":
        dates = ["最近30天"]
        date_name = BI.one_year_enerator()
        for date in date_name:
            dates.append(date[0])
        return render_template("brand.html",dates=dates)
    else:
        try:
            Brand_ip = request.form.get("data2")
            session["Brand_ip"] = Brand_ip
            date = request.form.get("data3")
            session["date"]=date
            if date != "最近30天":
                dateType = "month"
            else:
                dateType = "recent30"
            IPS, Brand_id,cateID = BI.Competitive_brand(Brand_ip, date, dateType)
            session['cateID']=cateID
            mat = []
            for cow in IPS:
                dic = {cow[0]:cow[1]}
                mat.append(dic)
            IPS = mat
            session["Brand_id"] = Brand_id
        except:
            return render_template("Error.html")

        return render_template("brand.html",IPS=IPS,date=date,Brand_ip=Brand_ip)



#接收竞品牌2框内值
@app.route("/brand2",methods=["POST","GET"])
def good_views():
    if request.method=="POST":
        try:
            bag = {}
            Brand_ip = session.get("Brand_ip")
            date = session.get("date")
            cateID = session.get('cateID')
            for x in range(1,14):
                if request.form.get("x"+str(x)) or request.form.get("date"+str(x)) :
                   #框内值
                    data = request.form.get("knz"+str(x))

                    title = request.form.get("date" + str(x))
                    brand_id = session.get("Brand_id")
                    if data!="":
                        bag[title] = data
            print(bag)
            for x in bag:
                print(x)
                if x == "热销TOP店铺榜:":
                    datac = BI.compete_Brand_Tradeshop_top(cateID,bag[x], date, brand_id)
                #     待存入数据库
                elif x == "流量TOP店铺榜:":
                    datac = BI.compete_Brand_flowshop_top(cateID,bag[x], date, brand_id)
                    #     待存入数据库
                elif x == '热销TOP商品榜:':

                    datac = BI.Competitive_Brand_Tradeshop_Commodities(cateID,bag[x], date, brand_id)
                elif x == "流量TOP商品榜:":
                    datac = BI.Competitive_Brand_Flow_Commodities(cateID,bag[x], date, brand_id)
                elif x == "类目构成:":
                    datac = BI.Competitive_Brand_Category_Composition(cateID,bag[x], date, brand_id)
                elif x == "年龄客群构成:":
                    datac = BI.Brand_Age_Clients(cateID,bag[x], date, brand_id)
                elif x == "年龄客群占比构成:":
                    datac = BI.Brand_Age_Clients_Proportion(cateID,bag[x], date, brand_id)
                elif x == "年龄交易指数构成:":
                    datac = BI.Brand_Age_Trading_index(cateID,bag[x], date, brand_id)
                elif x == "年龄支付转化率指数构成:":
                    datac = BI.Brand_Age_Payment_Conversion_Rate(cateID,bag[x], date, brand_id)
                elif x == "性别客群构成:":
                    datac = BI.Brand_Gender_Clients(cateID,bag[x], date, brand_id)
                elif x == "性别客群占比构成:":
                    datac = BI.Brand_Gender_Clients_Proportion(cateID,bag[x], date, brand_id)
                elif x == "性别交易指数构成:":
                    datac = BI.Brand_Gender_Trading_index(cateID,bag[x], date, brand_id)
                elif x == "性别支付转化率指数构成:":
                    datac = BI.Payment_Conversion_Rate(cateID,bag[x], date, brand_id)

                    #交接逻辑 存入数据库
            dates = ["最近30天"]
            date_name = BI.one_year_enerator()
            for date in date_name:
                dates.append(date[0])
        except:
            return render_template("Error.html")
        return render_template("brand.html",Brand_ip=Brand_ip,dates=dates,date=date)
#测试
@app.route("/test",methods=["POST","GET"])
def test_views():
    if request.method=="GET":
        return render_template("index.html")
    else:
        data = request.form.get("test")
        print(data)
        return render_template("index.html")
#行业趋势
@app.route("/Industry_trends_map",methods=["POST","GET"])
def Industry_trends_views():
    if request.method=="GET":
        return render_template("Industry_trends_map.html")
    else:
        data={"date":["2018-10-01","2018-11-01","2018-12-01"],
            "data1":[10,20,50],
            "data2":[15,10,30]}
        data = json.dumps(data)
        return data

#404
@app.errorhandler(404)
def a(e):
    return render_template("404.html"),404


# @app.route("/addsql")
# def cate_id_add_sql(cate_name,cate_id):
#     data = Cate_id(cate_name=cate_name,cate_id=cate_id)
#     db.session.add(data)
#     db.session.commit()
# def cate_name_add_sql(cate_name1,cate_name2,cate_name3):
#     data = Cate_name(cate_name1=cate_name1,cate_name2=cate_name2,cate_name3=cate_name3)
#     db.session.add(data)
#     db.session.commit()
# def Cate_name_show():
#     user1 = Cate_name.query.all()
#     mat=[]
#     for x in user1:
#         text = []
#         text.append(x.cate_name1)
#         text.append(x.cate_name2)
#         text.append(x.cate_name3)
#         mat.append(text)
#     mat = np.array(mat)
#     return mat
#  市场大盘
# def Trade_transactions_add_sql(cateID,type,date,cateName,tradeIndex,tradeGrowthRange,
#                                payAmtParentCateRate,payCntParentCateRate):
#     data = Trade_transactions(cateID=cateID,type=type,date=date,cateName=cateName,tradeIndex=tradeIndex,
#                      tradeGrowthRange=tradeGrowthRange,payAmtParentCateRate=payAmtParentCateRate,
#                      payCntParentCateRate=payCntParentCateRate)
#     db.session.add(data)
#     db.session.commit()
# def Industry_Maijia_add_sql(cateID,type,date,cateName,slrCnt,parentCateSlrRate,
#                             tradeSlrCnt,parentCateTradeSlrCntRate):
#     data = Industry_Maijia(cateID=cateID,type=type,date=date,cateName=cateName,slrCnt=slrCnt,
#                      parentCateSlrRate=parentCateSlrRate,tradeSlrCnt=tradeSlrCnt,
#                      parentCateTradeSlrCntRate=parentCateTradeSlrCntRate)
#     db.session.add(data)
#     db.session.commit()
# # 市场排行
# def Industry_ranking_shop_hotsearch(cateID,Data_block,Data_type,date,shop_Name,
#                                     userId,shopUrl,b2CShop,uvIndex,seIpvUvHits,tradeIndex):
#     data = Industry_ranking_shop_hotsearch(cateID=cateID,Data_block=Data_block,Data_type=Data_type,date=date,
#                            shop_Name=shop_Name,userId=userId,shopUrl=shopUrl,b2CShop=b2CShop,
#                            uvIndex=uvIndex,seIpvUvHits=seIpvUvHits,tradeIndex=tradeIndex)
#     db.session.add(data)
#     db.session.commit()
# def Industry_ranking_shop_hotsale(cateID,Data_block,Data_type,date,shop_Name,
#                                     userId,shopUrl,b2CShop,tradeIndex,payRateIndex):
#     data = Industry_ranking_shop_hotsale(cateID=cateID,Data_block=Data_block,Data_type=Data_type,date=date,
#                            shop_Name=shop_Name,userId=userId,shopUrl=shopUrl,b2CShop=b2CShop,
#                            tradeIndex=tradeIndex,payRateIndex=payRateIndex)
#     db.session.add(data)
#     db.session.commit()
# def Industry_ranking_item_hotsearch(cateID,Data_block,Data_type,date,item_Name,
#                                     itemId,detailUrl,shop_name,userId,shopUrl,uvIndex,seIpvUvHits,tradeIndex):
#     data = Industry_ranking_item_hotsearch(cateID=cateID,Data_block=Data_block,Data_type=Data_type,date=date,
#                         item_Name=item_Name,itemId=itemId,detailUrl=detailUrl,shop_name=shop_name,userId=userId,
#                            shopUrl=shopUrl,uvIndex=uvIndex,seIpvUvHits=seIpvUvHits,tradeIndex=tradeIndex)
#     db.session.add(data)
#     db.session.commit()
# def Industry_ranking_item_hotsale(cateID,Data_block,Data_type,date,item_Name,
#                                     itemId,detailUrl,shop_name,userId,shopUrl,tradeIndex,payRateIndex):
#     data = Industry_ranking_item_hotsale(cateID=cateID,Data_block=Data_block,Data_type=Data_type,date=date,
#                         item_Name=item_Name,itemId=itemId,detailUrl=detailUrl,shop_name=shop_name,userId=userId,
#                            shopUrl=shopUrl,tradeIndex=tradeIndex,payRateIndex=payRateIndex)
#     db.session.add(data)
#     db.session.commit()
# def Industry_ranking_item_hotpurpose(cateID,Data_block,Data_type,date,item_Name,
#                                     itemId,detailUrl,shop_name,userId,shopUrl,cltHits,cartHits,tradeIndex):
#     data = Industry_ranking_item_hotpurpose(cateID=cateID,Data_block=Data_block,Data_type=Data_type,date=date,
#                         item_Name=item_Name,itemId=itemId,detailUrl=detailUrl,shop_name=shop_name,userId=userId,
#                            shopUrl=shopUrl,cltHits=cltHits,cartHits=cartHits,tradeIndex=tradeIndex)
#     db.session.add(data)
#     db.session.commit()
#
# def Industry_ranking_brand_hotsearch(cateID,Data_block,Data_type,date,brandName,brandId,uvIndex,
#                                      seIpvUvHits,tradeIndex):
#     data = Industry_ranking_brand_hotsearch(cateID=cateID,Data_block=Data_block,Data_type=Data_type,date=date,
#                                             brandName=brandName,brandId=brandId,uvIndex=uvIndex,
#                                             seIpvUvHits=seIpvUvHits,tradeIndex=tradeIndex)
#     db.session.add(data)
#     db.session.commit()
# def Industry_ranking_brand_hotsale(cateID,Data_block,Data_type,date,brandName,brandId,tradeIndex,
#                                    payRateIndex):
#     data = Industry_ranking_brand_hotsale(cateID=cateID,Data_block=Data_block,Data_type=Data_type,date=date,
#                                             brandName=brandName,brandId=brandId,tradeIndex=tradeIndex,
#                                           payRateIndex=payRateIndex)
#     db.session.add(data)
#     db.session.commit()


if __name__=="__main__":
    # 家里主机IP
    # app.run(debug=True,host="192.168.0.106")
    #wife
    app.run(debug=False)
    #DN
    # app.run(debug=False,host="176.47.2.41")
    # 罗辑(公司)主机IP
    # app.run(debug=True, host="192.168.2.166")


