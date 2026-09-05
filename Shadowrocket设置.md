# Shadowrocket使用设置

## 首页

### 订阅节点

右上角 ＋ 号添加节点，类型根据你的机场提供的订阅进行设置（部分机场支持一键导入Shadowrocket），其他设置保持默认即可，过滤可以使用AI生成正则表达式来过滤不需要的节点（提示词：^(?!.*(xxxx|xxxx)).*$，在小火箭的过滤正则中，填入以下代码：）就可以自动生成正则表达式，复制到已添加节点的过滤里即可生效。

### 全局路由：配置

开启代理并从上往下滑动屏幕进入代理分组页面，选择自己分流规则所需要使用的代理

## 配置

### 订阅配置

右上角 ＋ 号从给定的URL下载配置

**配置文件地址：**

```
https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/Shadowrocket_basic.conf
```

复制粘贴后点击下载，等待下载完成即可。Raw地址需要代理才可以正常访问GitHub下载，如果没有代理的条件可以把上述地址转换成国内CDN的地址即可，复制上述地址给AI生成（提示词：转换成testingcf.jsdelivr.net/加速连接）生成的新连接复制粘贴并下载即可使用

### 使用配置

1. 长按本地文件下载好的Shadowrocket_basic.conf，点击使用配置
2. 点击Shadowrocket_basic.conf右侧ⓘ进入配置文件，依次点击HTTPS解密-打开HTTPS解密-证书授权-证书-生成新的CA证书-安装证书-允许-点击右上角的√来保存。
3. 返回桌面依次点击设置-通用-VPN与设备管理-以下载的描述文件-点击Shadowrocket的文件-右上角安装-属于锁屏密码-右上角安装。
4. 回到Shadowrocket点击右上角确认既可正常使用配置文件。

## 数据

主要是在日志里查看代理日志（每次开关小火箭就会生成一个日志文件）进行数据分析，具体使用就个人情况而定。

## 设置

只设置 GeoLite2 数据库，其他保持默认即可。

1. 下滑在更新里找到 GeoLite2 数据库点击进入

| 类型 | URL |
| --- | --- |
| 国家 | https://cdn.jsdelivr.net/gh/Loyalsoldier/geoip@release/Country.mmdb |
| ASN | https://cdn.jsdelivr.net/gh/Loyalsoldier/geoip@release/GeoLite2-ASN.mmdb |

2. 复制粘贴后点击更新即可。

> 其他参数根据自身情况设置。
