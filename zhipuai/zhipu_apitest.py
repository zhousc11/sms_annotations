from zhipuai import ZhipuAI
client = ZhipuAI(api_key="SECRET") # 填写您自己的APIKey
prompt = '''
【话费查询】尊敬的客户，您好！您2018年06月的话费总额为:17.74元。话费查询请拨1008611。中国移动
【年中大促】支付宝、余额宝双红包来袭，最高99元！打开支付宝首页搜索：7140298，即可100%抢到！红包有效3天，每天可领1次。退订回T
Oreo&#39;saslamdunk!
【话费查询】尊敬的客户，您好！您2018年06月的话费总额为:17.74元。话费查询请拨1008611。中国移动
【百度地图】查看“上海虹桥站-上海站”步行指引、方向定位，点击：http://j.map.baidu.com/GDxZP地铁2号线(虹桥火车站上,中山公园下,6站)，换地铁4号线(上海火车站1口出,5站)，下车向西北430米
【知乎】YourZhihuverificationcodeis516570.
【哔哩哔哩】你的账号在2019-07-1519:20:26重置了登录密码，请使用新密码登录。如非本人操作，请及时找回密码。
shsjsjsjs
[NOWCODER]Yourverificationcodeis8861.
Use136646asyourlogincodeforPairs（ペアーズ）恋愛・婚活・結婚マッチングサービス.(AccountKitbyFacebook)
[TradeUP]Yourverificationcodeis:131777.Enterthiscodetoverifyyourphonenumber
【知乎】YourZhihuverificationcodeis869882.
【知乎】YourZhihuverificationcodeis799712.
以上是几条短信，请判断每一条短信是否是垃圾短信，并判断每条短信属于亲友，公益短信，营销，通知，验证码这几个类别中的哪一种。垃圾短信输出1，不是垃圾短信输出0.亲友输出1，公益短信输出2，营销输出3，通知输出4，验证码输出5，其他输出0
.请格式化输出，像0   6这样。请只输出数字组合，不要添加任何其他内容。请只输出数字组合，不要添加任何其他内容。请只输出数字组合，不要添加任何其他内容。'''
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content": prompt}
    ],
)
print(response.choices[0].message)