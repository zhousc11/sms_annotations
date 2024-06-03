from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import json

# 星火认知大模型Spark3.5 Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
# 星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
SPARKAI_APP_ID = 'SECRET'
SPARKAI_API_SECRET = 'SECRET'
SPARKAI_API_KEY = 'SECRET'
# 星火认知大模型Spark3.5 Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = 'generalv3.5'

if __name__ == '__main__':
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    sms_content = '''【土巴兔】【土巴兔】您好，刚刚是土巴兔装修平台来电，为更好地为您服务，稍后将再次来电请注意接听。您可以打开土巴兔APP看精美图片了解最新案例，点击下载&amp;gt;&amp;gt;https://dwz.cn/6VWlpay6
（020）95575的来电，感谢您的支持！【广发证券】
尊敬的客户，我们关注到您尚未完成广发证券开户，为方便您顺利完成开户，我们将安排专属客户经理协助您进一步操作，请留意接听我司95575或
载https://url.cn/5M1U1Ct【腾讯科技】
你好，欢迎报名《zyr-3.13系统测试数据》课程，首次上课时间为2019年08月08日10:50，若还未下载企鹅辅导app，点击下
【亨氏官方旗舰店】番茄酱2元，铁锌钙米粉325g包邮价21.9元，更多优惠上苏宁抢t.suning.cn/9aHywCD回T退订
【淘托精选】您订阅的2019-08-08报价为黄金342.95元/g18K261.21元/g钯金327.1元/g铂金195.3元/g
【中国人寿】尊敬的客户：生活中充满风险，家人的健康和安全是我们每个人最大的心愿。中国人寿愿与您相伴，撑起家庭保护伞，无惧风险，为爱担当
！保险产品详情请点击：http://www.e-chinalife.com/gky查看，退订回复T。
【滴滴外卖】来就送最高(6元无门槛)立减券，滴滴食堂(0元配送)更省钱！戳https://z.didi.cn/2pMMB退订TD
【云汉芯城】您有一张500元京东卡即将过期，请及时查看！http://tinyurl.com/yyl9xdtg回复TD退订
你的LBT我己付款，麻烦给我确认下。'''
    part_prompt = '以上是几条短信，请判断每一条短信是否是垃圾短信，并判断每条短信属于亲友，公益短信，营销，通知，验证码这几个类别中的哪一种。垃圾短信输出1，不是垃圾短信输出0.亲友输出1，公益短信输出2，营销输出3，通知输出4，验证码输出5，其他输出0.请格式化输出，像0   6这样。'
    prompt = sms_content + '/n' + part_prompt
    messages = [ChatMessage(
        role="user",
        content=prompt
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    # print(a)
    # print(type(a))
    a = str(a)
    print(a)
    print(type(a))
    # txt_data = json.loads(a)
    # b = txt_data['generations'][0][0]['text']
    # print(b)
    # print(type)
