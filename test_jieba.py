#encoding=utf-8
import jieba
"""
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print "Full Mode:", "/ ".join(seg_list)  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print "Default Mode:", "/ ".join(seg_list)  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print ", ".join(seg_list)

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print ", ".join(seg_list)

seg_list = jieba.cut("内蒙古包头市青山区沼园路16号融邦公寓小区8栋1202号",cut_all=True) #
print 'Full Mode:',', '.join(seg_list)
"""
import jieba.posseg as pseg
wl=['洪山区民族大道上钱村建龙尚谷3栋28楼','内蒙古包头市青山沼园路16号融邦公寓小区8栋1202号','亲爱的爸爸','小明','马锐','肥潇','文杰','王阿姨','大姨妈','大姨夫','表姑','尊敬的客户，您个人信用卡额度不足，本次消费失败。推荐掌上生活 cmbt.cn/3AUuzV 还款即时恢复额度，本跨行还款0手续费[招商银行]']
words=pseg.cut(wl[-1])
for w in words:
    print w.word,w.flag

seg_list = jieba.cut("内蒙古包头市青山区沼园路16号融邦公寓小区8栋1202号",cut_all=False) #
print 'Default Mode',', '.join(seg_list)
