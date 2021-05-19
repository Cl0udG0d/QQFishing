## QQFishing QQ钓鱼

![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/fishing.png)

🚀 QQFishing 模仿QQ空间手机统一登录页面的钓鱼网站

:blush:后端使用Python-Flask编写 前端白嫖+随便写写，数据库使用MySQL🔥

:zap:项目部署只支持Docker:whale:安装(~~懒得配置源码安装~~)，应 [issue-1](https://github.com/Cl0udG0d/QQFishing/issues/1)，添加源码安装教程

:trident:适用对象: 使用社会工程学定向钓鱼攻击的安全渗透人员

:four_leaf_clover:开发时间：2020年10月13日-> +oo  

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [使用说明](#使用说明)
- [部分截图](#部分截图)
- [参考学习](#参考学习)
- [维护者](#维护者)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)
- [赞赏码](#赞赏码)
- [留在最后](#留在最后)

## 背景

:fire:社会工程学钓鱼  
介绍的博客：https://www.cnblogs.com/Cl0ud/p/13818127.html

## 安装
该项目可使用Docker安装或源码安装（二选一）,以下是安装流程：

#### **Docker安装：**（在腾讯云Ubuntu机器上测试成功）

+ 在服务器或本机上安装docker和docker-compose

+ 运行以下三条命令：

  ```shell
  git clone https://github.com/Cl0udG0d/QQFishing
  cd QQFishing
  docker-compose up -d
  ```

+ 运行结束后访问 [http://ip地址:5000](http://ip:5000/)

**源码安装：（在阿里云Windows机器上测试成功）**

- Python版本:3.X，数据库:MySQL

- Git bash界面输入 git clone https://github.com/Cl0udG0d/QQFishing 进行下载（或直接下载ZIP源代码）

- 安装python类库: pip3 install -r requirements.txt

- 修改config.py数据库账号密码为本地账号密码,将config.py 中 HOSTNAME='mysql' 修改为 HOSTNAME='127.0.0.1'，如图：

  ![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/4.png)

- 修改index.py文件中的app.run()为app.run(host='0.0.0.0')，如图：

  ![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/2.png)

- 导入数据库init.sql文件（方法很多，例如：[phpstudy如何导入sql文件](https://www.php.cn/php-ask-424960.html)，init.sql在 /mysql/init/文件夹下，init.sql.zip在本目录下），进行自动初始化数据库和表，以及初始管理用户

- 运行python3 index.py，如图：

  ![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/1.png)

  访问 [http://ip地址:5000](http://ip:5000/)

- 如果访问不了，请检查是否是IP地址输错或者是云服务器防火墙端口未打开，如图：

  ![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/3.png)

**提示：默认管理员登录邮箱为:[springbird@qq.com](mailto:springbird@qq.com),密码为:springbird,登录之后请第一时间修改密码**



## 使用说明
暂无

## 部分截图
界面太丑了，不截图了  
算了还是截两张吧  
![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/index1.png)
![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/index2.png)
![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/index3.png)
![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/index4.png)


## 参考学习

- [qq-fishing-website](https://github.com/ChinaVeryNb/qq-fishing-website) — 模仿QQ空间手机统一登录页面的钓鱼网站
- [mailqq](https://github.com/Escher1108/mailqq) — 一个模拟腾讯QQ邮箱登录界面的钓鱼平台，有前端+后台控制
- [钓鱼](https://github.com/icindy/diaoyu) — 五分钟制作"钓鱼网站"

## 维护者

[@春告鳥](https://github.com/Cl0udG0d)

## 如何贡献

:beer:非常欢迎你的加入！[提一个 Issue](https://github.com/Cl0udG0d/QQFishing/issues/new) 或者提交一个 Pull Request。

:beers:当然也欢迎给我发邮件  2585614464@qq.com Join us！


### 贡献者

:jack_o_lantern:  
春告鳥：理工酸菜鱼，花溪黄焖鸡  

南风：发呆爱好者，废话输出机

不董:不董

## 使用许可

[MIT](LICENSE)  © 春告鳥

## 赞赏码

![](https://github.com/Cl0udG0d/QQFishing/blob/master/static/images/%E8%B5%9E%E8%B5%8F%E7%A0%81.png)

## 留在最后

:gift_heart: 请勿使用该项目进行违法犯罪，善恶终有报，天道好轮回
