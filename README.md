# netcut

### 网络剪切板

### API
***
#### api: /new
#### 新建剪切板
#### method: post
#### params:
cutName：剪切板名称(唯一) 【可选】如果不传该字段，则随机生成名称  
public：是否公开 【可选】默认为true  
pwd：密码 如果public设为false，则pwd为必选，查询或修改剪切板时必须携带；如果public为true，该字段无效  
content：剪切板内容 【可选】默认为空字符串
***
#### api: /save
#### 更新剪切板,如果剪切板不存在则会根据传入的cutName新建
#### method: post
#### params:
cutName：剪切板名称 【可选】未填入则默认新建一个名称随机的剪切板  
content：剪切板内容 【可选】默认为空字符串  
pwd：如果要写入的剪切板的public字段为false，pwd字段为必选；否则该字段无效  
***
#### api: /get
#### 获取剪切板内容
#### method: post
#### params:
cutName：剪切板名称 【必选】
pwd：如果查询的剪切板的public字段为false，pwd字段为必选；否则该字段无效  


