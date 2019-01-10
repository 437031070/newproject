#子行业分布

def Subindustry_Distribution():
    data = Subindustry_Distribution(cateID=cow[0], Data_module=cow[1], date=cow[2], cateName=cow[3],slrCnt=cow[4], parentCateSlrRate=cow[5], tradeSlrCnt=cow[6],parentCateTradeSlrCntRate=cow[7])
    db.session.add(data)
    db.session.commit()

#高流量店铺排行
def shop_hotsearch():
    data = Shop_hotsearch(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],shop_title=cow[4], cateRankId=cow[5],userId=cow[6],shopUrl=cow[7],b2CShop= ,uvIndex=,seIpvUvHits=,tradeIndex=,Search=,Payment_amount=,Visitor=,)
    db.session.add(data)
    db.session.commit()
#高交易店铺排行

def shop_hotsale():
    data = Shop_hotsearch(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],shop_title=cow[4], cateRankId=cow[5],userId=cow[6],shopUrl=cow[7],b2CShop= ,tradeIndex=,payRateIndex=,Conversion_rate=,Payment_amount=)
    db.session.add(data)
    db.session.commit()
#高流量商品排行

def Item_hotsearch():
    data = Item_hotsearch(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],item_title=cow[4], itemId=cow[5],detailUrl=cow[6],cateRankId=cow[7],shop_title= ,userId=,shopUrl=,uvIndex=,seIpvUvHits=,tradeIndex=,Search=,Payment_amount=,Visitor=)
    db.session.add(data)
    db.session.commit()

#高交易商品排行

def Item_hotsale():
    data = Item_hotsale(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],item_title=cow[4], itemId=cow[5],detailUrl=cow[6],cateRankId=cow[7],shop_title= ,userId=,shopUrl=,payRateIndex=,tradeIndex=,Conversion_rate=,Payment_amount=)
    db.session.add(data)
    db.session.commit()

#高流量品牌排行
def Brand_hotsearch():
    data = Brand_hotsearch(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],brandName=cow[4], brandId=cow[5],cateRankId=cow[6],uvIndex=cow[7],seIpvUvHits= ,tradeIndex=,Visitor=,Search=,Payment_amount=)
    db.session.add(data)
    db.session.commit()
#高交易品牌排行
def Brand_hotsale():
    data = Brand_hotsale(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],item_title=cow[4], itemId=cow[5],detailUrl=cow[6],cateRankId=cow[7],payRateIndex= ,tradeIndex=,Conversion_rate=,Payment_amount=)
    db.session.add(data)
    db.session.commit()

#热门属性
def Hot_attributes():
    data = Hot_attributes(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],payments_piece=cow[4],tradeIndex=cow[5],Sale=cow[6])
    db.session.add(data)
    db.session.commit()

#搜索词排行
def Search_terms():
    data = Search_terms(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],searchWord=cow[4], hotSearchRank=cow[5],seIpvUvHits=cow[6],clickHits=cow[7],clickRate= ,payRate=,p4pRefPrice=,tmClickRate=,search=,click=)
    db.session.add(data)
    db.session.commit()
#品牌词排行

def Brand_Word():
    data = Brand_Word(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],searchWord=cow[4], hotSearchRank=cow[5],relSeWordCnt=cow[6],avgWordSeIpvUvHits=cow[7],avgWordClickHits= ,p4pRefPrice=,search=,click=)
    db.session.add(data)
    db.session.commit()

#修饰词排行
def Modifiers_Word():
    data = Modifiers_Word(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],searchWord=cow[4], hotSearchRank=cow[5],seIpvUvHits=cow[6],clickHits=cow[7],clickRate= ,payRate=,p4pRefPrice=,tmClickRate=,search=,click=)
    db.session.add(data)
    db.session.commit()
#核心词排行
def Core_word():
    data = Core_word(cateID=cow[0], Data_module=cow[1],data_type=cow[2], date=cow[3],searchWord=cow[4], hotSearchRank=cow[5],seIpvUvHits=cow[6],clickHits=cow[7],clickRate= ,payRate=,p4pRefPrice=,tmClickRate=,search=,click=)
    db.session.add(data)
    db.session.commit()
#地域分析
def Geographical_distribution():
    data = Geographical_distribution(cateID=cow[0], Data_module=cow[1],date=cow[2], areaName=cow[3],slrCnt=cow[4], parentCateSlrRate=cow[5],tradeSlrCnt=cow[6],parentCateTradeSlrCntRate=cow[7])
    db.session.add(data)
    db.session.commit()