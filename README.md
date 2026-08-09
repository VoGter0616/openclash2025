<p align="center">VoGter的自用模板库</p>

---

## 📂 目录结构

| 目录 | 描述 |
| :--- | :--- |
| [/.github](./.github) | 自动化脚本及工具。 |
| [/rule](./rule) | 规则集。 |
| [Clash_custom.ini](./cfg/Clash_custom.ini) | OpenClash自定义转换文件。 |
| [Clash_test01.ini](./cfg/Clash_test01.ini) | OpenClash转换前测试文件。 |
| [Clash_Verge.ini](./cfg/Clash_Verge.ini) | Clash Verge自定义转换文件。 |
| [Shadowrocket_basic.conf](./cfg/Shadowrocket_basic.conf) | Shadowrocket自定义转换文件。 |

---

<details>
<summary><b>📄 点击展开 / 折叠查看：OpenClash 设置指南</b></summary>

<br>

# OpenClash使用设置

## 插件设置

### 模式设置

- 运行模式：Fake-ip（增强）模式
- 默认勾选：UDP流量转发
- 代理模式：Rule（策略代理）
- 如果是旁路由勾选旁路网关（旁路由）兼容
- 其他默认

### 流量控制

**默认勾选：**

- 路由本机代理
- 禁用QUIC
- 绕过服务器地址
- 开启绕过指定区域IP：绕过中国大陆

**绕过指定区域IPv4黑名单里添加：**

```
services.googleapis.cn
googleapis.cn
xn--ngstr-lra8j.com
adobe.com
adobelogin.com
adobe.io
behance.net

```

- 其他默认

### DNS设置

- 本地DNS劫持：使用Dnsmasq转发
- 其他默认

### 流媒体增强

如果有详细的分流规则，则不用设置（默认不设置）

### 黑白名单

默认不设置

### 外部控制

默认不设置

### IPv6设置

- 默认勾选：允许 IPv6 类型 DNS 解析
- Fake-IP 地址范围 (IPv6 Cidr)：fdfe:dcba:9876::1/64
- 其他默认

### GEO数据库订阅

**默认勾选：**

- 自动更新 GeoIP MMDB 数据库
- 自动更新 GeoIP Dat 数据库
- 自动更新 GeoSite 数据库

**数据库更新 URL：**

- https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/country.mmdb
- https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geoip.dat
- https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geosite.dat

### 大陆白名单订阅

开启自动更新，全部默认即可

### 定时重启

默认设置（根据自身情况设置）

### 版本更新

根据设备选择编译版本

- 更新分支：Master
- 使用Smart内核就开启Smart内核更新，不适用就默认停用

### 开发者选项

默认不设置

### 内核测试

默认不设置

### oicCloud

默认不设置

## 覆写设置

### 常规设置

- Github 地址修改：https://testingcf.jsdelivr.net/
- 其他默认

### DNS设置

**默认勾选：**

- 自定义上游 DNS 服务器
- 遵循规则(respect-rules)
- Fake-IP 地址范围 (IPv4 Cidr)：198.18.0.1/16
- Fake-IP 持久化
- Fake-IP-Filter
- Fake-IP-Filter-Mode：黑名单模式

```
*.lan
*.local
+.localdomain
localhost.ptlogin2.qq.com
time.apple.com
time.android.com
time.windows.com
+.ntp.org.cn
+.pool.ntp.org
+.xn--ngstr-lra8j.com
+.qq.com
+.tencent.com
+.wechat.com
+.servicewechat.com
+.gtimg.com
+.gtimg.cn
+.qpic.cn
+.qlogo.cn
+.tenpay.com
+.myqcloud.com
+.qcloud.com
+.douyin.com
+.douyincdn.com
+.douyinpic.com
+.douyinstatic.com
+.douyinliving.com
+.iesdouyin.com
+.douyinvod.com
+.douyinvideo.net
+.amemv.com
+.snssdk.com
+.byteimg.com
+.bytecdn.cn
+.ibytedtos.com
+.zijieapi.com
+.pstatp.com
+.toutiao.com
+.toutiaovod.com
+.bytedance.net
+.xiaohongshu.com
+.xhscdn.com
+.xhscdn.net
+.xhslink.com
+.xhsimg.com
dlg.io.mi.com
+.taobao.com
+.tmall.com
+.tbcdn.cn
+.alicdn.com
+.alibaba.com
+.alibabausercontent.com
+.alipay.com
+.alipayobjects.com
+.goofish.com
+.idlefish.com
+.aliyun.com
+.aliyuncs.com
+.mmstat.com
+.cainiao.com
+.amap.com
+.autonavi.com
fhnfile.oss-cn-shenzhen.aliyuncs.com
+.115.com
+.115cdn.com
+.115cdn.net
+.115img.com
+.116cd.cn
+.116cd.com
+.116cd.net
+.anxia.com
+.sq.cc
```

#### Nameserver-Policy

```yaml
"geosite:private,cn,geolocation-cn,apple-cn,microsoft@cn,steam@cn,bytedance,xiaohongshu": [223.5.5.5, 119.29.29.29, 2400:3200::1]
"+.cn": [223.5.5.5, 119.29.29.29, 2400:3200::1]
"+.中国": [223.5.5.5, 119.29.29.29, 2400:3200::1]
"+.公司": [223.5.5.5, 119.29.29.29, 2400:3200::1]
"+.网络": [223.5.5.5, 119.29.29.29, 2400:3200::1]

"+.qq.com": [223.5.5.5, 10.10.10.1]
"+.tencent.com": [223.5.5.5, 10.10.10.1]
"+.baidu.com": [223.5.5.5, 10.10.10.1]
"+.bilibili.com": [223.5.5.5, 10.10.10.1]
"+.taobao.com": [223.5.5.5, 10.10.10.1]
"+.jd.com": [223.5.5.5, 10.10.10.1]
"+.douyin.com": [223.5.5.5, 10.10.10.1]
"+.163.com": [223.5.5.5, 10.10.10.1]
"+.iqiyi.com": [223.5.5.5, 10.10.10.1]
"+.youku.com": [223.5.5.5, 10.10.10.1]

"geosite:google,openai,anthropic,github,telegram,twitter,geolocation-!cn": ["https://1.1.1.1/dns-query#PROXY", "https://dns.google/dns-query#PROXY"]
```

**设置自定义上游 DNS 服务器**（在上方设置中启用本功能后生效）：

| 服务器分组 | 服务器地址 | 服务器类型 | 状态 |
| --- | --- | --- | --- |
| nameserver | 223.5.5.5/dns-query | HTTPS | 启用 |
| nameserver | dns.pub/dns-query | HTTPS | 启用 |
| fallback | 1.1.1.1/dns-query | HTTPS | 启用 |
| fallback | dns.google/dns-query | HTTPS | 启用 |
| default- nameserver | 223.5.5.5 | UDP | 启用 |
| default- nameserver | 119.29.29.29 | UDP | 启用 |
| default- nameserver | 2400:3200::1 | UDP | 启用 |

### Meta设置

**默认勾选：**

- 启用 TCP 并发
- 启用统一延迟
- Geodata 数据加载方式：标准模式
- 启用 GeoIP Dat 版数据库
- 启用流量（域名）探测
- 探测（嗅探）纯 IP 连接
- 自定义流量探测（嗅探）设置

### Smart设置

根据个人使用情况设置

## 规则设置

**默认勾选：**

- 自定义规则

```

# 1. 禁用阿里系 UDP 443 端口 (HTTP/3 / QUIC)，强制回退到 TCP 提升加载稳定性
- AND,((NETWORK,UDP),(DST-PORT,443),(GEOSITE,alibaba)),REJECT
```

## 配置订阅

| 配置文件名 | （自定义） |
| --- | --- |
| 订阅地址 | （自定义） |
| User-Agent | clash.meta/1.19.20 |
| 在线订阅转换 | √ |
| 订阅转换服务地址 | （自己的后端或者api.wcc.best） |
| 订阅转换模板 | 自定义模板 |
| 自定义模板地址 | https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/cfg/Clash_test01.ini |

其他参数根据自身情况设置。


</details>

<details>
<summary><b>📄 点击展开 / 折叠查看：Shadowrocket 设置指南</b></summary>

<br>

# Shadowrocket使用设置

## 首页

### 订阅节点

右上角 ＋ 号添加节点，类型根据你的机场提供的订阅进行设置（部分机场支持一键导入Shadowrocket），其他设置保持默认即可，过滤可以使用AI生成正则表达式来过滤不需要的节点（提示词：保留其他节点，删除XXXXX，在小火箭的过滤正则中，填入以下代码：）就可以自动生成正则表达式，复制到已添加节点的过滤里即可生效。

### 全局路由：配置

开启代理并从上往下滑动屏幕进入代理分组页面，选择自己分流规则所需要使用的代理

## 配置

### 订阅配置

右上角 ＋ 号从给定的URL下载配置

**配置文件地址：**

```
https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/cfg/Shadowrocket_basic.conf
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


</details>


> [!WARNING]
> 
> 仅根据自己使用情况进行更新。
>
> 大部分规则来源于以下
> 
> https://github.com/Aethersailor/Custom_OpenClash_Rules/tree/main/rule
>
> https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Clash
>
> https://github.com/v2fly/domain-list-community/tree/master/data
>
> https://github.com/MetaCubeX/meta-rules-dat/tree/master?tab=readme-ov-file
>
> 感谢以上大佬的代码开源，如有侵权告知删
> 
> 如需使用，请自行斟酌后再用，有任何问题VoGter均无义务解决。
> 
> 所有内容均由VoGter收集于互联网，如有侵权告知删。
