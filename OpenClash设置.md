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
"geosite:google,openai,anthropic,geolocation-!cn": ["https://1.1.1.1/dns-query#PROXY", "https://dns.google/dns-query#PROXY"]
```

**设置自定义上游 DNS 服务器**（在上方设置中启用本功能后生效）：

| 服务器分组 | 服务器地址 | 服务器类型 | 状态 |
| --- | --- | --- | --- |
| nameserver | 223.6.6.6/dns-query | HTTPS | 启用 |
| nameserver | dns.pub/dns-query | HTTPS | 启用 |
| nameserver | 119.29.29.29/dns-query | HTTPS | 启用 |
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
| 自定义模板地址 | https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/Clash_test01.ini |

其他参数根据自身情况设置。
