import requests as visit
def city(city):
  citys=['北京','上海','重庆','天津']
  if city in citys:
    print('\033[32mHOPYBOX:WEATHER:'+visit.get('http://api.yanxi520.cn/api/bdtq.php?msg={}市'.format(city)).text)
  else:
    print('\033[32mHOPYBOX:WEATHER:'+visit.get('http://api.yanxi520.cn/api/bdtq.php?msg={}'.format(city)).text)
  del citys