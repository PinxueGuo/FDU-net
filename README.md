# FDU-net

### 复旦大学自动重联网软件
 请按需自己选择以下版本exe使用：

##### FDU-net.exe
按提示输入学号密码，连接成功后将在后台运行。

##### FDU-net_IDtxt.exe
在ID.txt中，第一行写学号，第二行写密码。\
随后每次运行FDU-net.exe，无需输入学号密码。
 \
 \
 \
FDU-net.exe （适用于确定不会断电关机情况 eg: 没在实验室但想卷的日子）保持永远在线。\
FDU-net_IDtxt.exe （适用于可能会断电重启的情况 eg: 寒暑假）+ 自行设置断电重启+此exe开机自启动。
 \
 \
 \
PS:
* 需要已安装chrome浏览器，且chrome版本为96.
* 包内的chromedriver.exe请保持与当前要使用的FDU-net_v.exe在同一路径下
* 开启后首次登录可能不成功，若登录失败会10秒后重连，请耐心等待
* 本程序不会记录宁的学号密码
* 愿意自己动手的同学，可以用v0_my源码，写死学号密码自行编译打包自己专属exe，无需.txt即可实现和FDU-net_IDtxt.exe相同功能，更优雅?

代码已开源，可以自己改着玩，./score_code

Contributors: GSY, GPX
