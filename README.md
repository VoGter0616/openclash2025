<p align="center">VoGter的自用模板库</p>

---

## 📂 目录结构

| 目录 | 描述 |
| :--- | :--- |
| [/.github](./.github) | 自动化脚本及工具。 |
| [/rule](./rule) | 规则集。 |
| [Clash_IPLC_VIP.ini](./cfg/Clash_IPLC_VIP.ini) | OpenClash自定义转换文件，机场IPLC.PLUS专用。 |
| [Clash_custom.ini](./cfg/Clash_custom.ini) | OpenClash自定义转换文件。 |
| [Clash_test01.ini](./cfg/Clash_test01.ini) | OpenClash转换前测试文件。 |
| [Clash_Verge.ini](./cfg/Clash_Verge.ini) | Clash Verge自定义转换文件。 |
| [Shadowrocket_basic.conf](./cfg/Shadowrocket_basic.conf) | Shadowrocket自定义转换文件。 |

---

<details>
<summary><b>📄 点击展开 / 折叠查看：OpenClash 设置指南</b></summary>

<br>

# OpenClash使用设置

## 首页

### 运行状态——覆写模块（openclah v0.47.081以上版本）

**在openclash_custom_overwrite.sh文件内的exit 0上方粘贴并修改成所需机场节点域名解析DNS**
```
    ruby_edit "$CONFIG_FILE" "['dns']['proxy-server-nameserver']" "['节点域名解析DNS1','节点域名解析DNS2']"
```

## 插件设置

### 模式设置

- 运行模式：Fake-ip（TUN-混合）模式
- 网络栈类型：System
- 代理模式：Rule（策略代理）
- 旁路网关（旁路由）兼容✅（如果是旁路由勾选）
- 其他默认

### 流量控制

- 路由本机代理✅
- 禁用QUIC✅
- 绕过服务器地址✅
- 实验性：绕过指定区域IP：绕过中国大陆
- 其他默认

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

- IPv6 流量代理✅
- IPv6 代理模式:Mix混合模式
- 允许IPv6 类型 DNS 解析✅
- Fake-IP 地址范围 (IPv6 Cidr)：fdfe:dcba:9876::1/64
- 实验性：绕过指定区域IPv6:绕过中国大陆
- 其他默认

### GEO数据库订阅

- 自动更新 GeoIP MMDB 数据库✅
```
https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/country.mmdb
```

- 自动更新 GeoIP Dat 数据库✅
```
https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geoip.dat
```

- 自动更新 GeoSite 数据库✅
```
https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@release/geosite.dat
```

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

- 自定义上游 DNS 服务器✅
- 遵循规则(respect-rules)✅
- Fake-IP 持久化✅
- Fallback-Filter✅
```
fallback-filter:
  geoip: true
  geoip-code: CN
  ipcidr:
    - 10.0.0.0/8
    - 100.64.0.0/10
    - 127.0.0.0/8
    - 169.254.0.0/16
    - 172.16.0.0/12
    - 192.168.0.0/16
    - 224.0.0.0/4
  domain:
    # =========================================================
    # Google / Gemini / YouTube
    # =========================================================
    - "+.google.com"
    - "+.googleapis.com"
    - "+.gstatic.com"
    - "+.googleusercontent.com"
    - "+.googlevideo.com"
    - "+.googleadservices.com"
    - "+.googlesyndication.com"
    - "+.doubleclick.net"
    - "+.ggpht.com"
    - "+.youtube.com"
    - "+.youtube-nocookie.com"
    - "+.ytimg.com"
    - "+.youtu.be"
    - "+.gemini.google.com"
    - "+.ai.google.dev"
    - "+.generativelanguage.googleapis.com"
    - "+.aistudio.google.com"

    # =========================================================
    # OpenAI / ChatGPT
    # =========================================================
    - "+.openai.com"
    - "+.chatgpt.com"
    - "+.oaistatic.com"
    - "+.oaiusercontent.com"
    - "+.oaistatsig.com"

    # OpenAI 依赖的部分第三方服务
    - "+.challenges.cloudflare.com"
    - "+.workos.com"
    - "+.workos.imgix.net"
    - "+.workoscdn.com"
    - "+.intercom.io"
    - "+.intercomcdn.com"
    - "+.sentry.io"
    - "+.datadoghq.com"

    # =========================================================
    # Anthropic / Claude
    # =========================================================
    - "+.anthropic.com"
    - "+.claude.ai"
    - "+.claude.com"

    # =========================================================
    # AI / 开发者 AI 服务
    # =========================================================
    - "+.huggingface.co"
    - "+.hf.co"
    - "+.replicate.com"
    - "+.perplexity.ai"
    - "+.poe.com"
    - "+.cohere.com"
    - "+.mistral.ai"
    - "+.mistral.com"
    - "+.groq.com"
    - "+.x.ai"
    - "+.grok.com"
    - "+.cursor.com"
    - "+.cursor.sh"
    - "+.windsurf.com"
    - "+.codeium.com"

    # =========================================================
    # GitHub / GitLab / 开发者服务
    # =========================================================
    - "+.github.com"
    - "+.githubusercontent.com"
    - "+.githubassets.com"
    - "+.github.io"
    - "+.gitlab.com"
    - "+.gitlab.io"
    - "+.bitbucket.org"
    - "+.sourcegraph.com"
    - "+.npmjs.com"
    - "+.npmjs.org"
    - "+.pypi.org"
    - "+.pythonhosted.org"
    - "+.docker.com"
    - "+.docker.io"
    - "+.dockerusercontent.com"
    - "+.jsdelivr.net"
    - "+.unpkg.com"
    - "+.cdnjs.com"
    - "+.cdnjs.cloudflare.com"

    # =========================================================
    # Cloudflare / CDN / DNS
    # =========================================================
    - "+.cloudflare.com"
    - "+.cloudflare-dns.com"
    - "+.cloudflareclient.com"
    - "+.workers.dev"
    - "+.pages.dev"
    - "+.cloudfront.net"
    - "+.fastly.net"
    - "+.akamaized.net"
    - "+.akamaihd.net"
    - "+.edgekey.net"
    - "+.edgesuite.net"

    # =========================================================
    # Facebook / Instagram / Meta
    # =========================================================
    - "+.facebook.com"
    - "+.facebook.net"
    - "+.fbcdn.net"
    - "+.fbsbx.com"
    - "+.instagram.com"
    - "+.cdninstagram.com"
    - "+.threads.net"
    - "+.threads.com"
    - "+.whatsapp.com"
    - "+.whatsapp.net"

    # =========================================================
    # X / Twitter
    # =========================================================
    - "+.x.com"
    - "+.twitter.com"
    - "+.twimg.com"

    # =========================================================
    # Telegram
    # =========================================================
    - "+.telegram.org"
    - "+.t.me"
    - "+.telegra.ph"
    - "+.telegram.me"
    - "+.telegram.dog"

    # =========================================================
    # Reddit
    # =========================================================
    - "+.reddit.com"
    - "+.redditmedia.com"
    - "+.redditstatic.com"
    - "+.redd.it"

    # =========================================================
    # Discord
    # =========================================================
    - "+.discord.com"
    - "+.discordapp.com"
    - "+.discordapp.net"
    - "+.discord.gg"
    - "+.discord.media"

    # =========================================================
    # Microsoft / Azure / Copilot
    # =========================================================
    - "+.microsoft.com"
    - "+.microsoftonline.com"
    - "+.msauth.net"
    - "+.msftauth.net"
    - "+.live.com"
    - "+.office.com"
    - "+.office.net"
    - "+.office365.com"
    - "+.azure.com"
    - "+.azureedge.net"
    - "+.windows.net"
    - "+.bing.com"
    - "+.bingapis.com"
    - "+.copilot.microsoft.com"

    # =========================================================
    # Apple
    # =========================================================
    - "+.apple.com"
    - "+.icloud.com"
    - "+.icloud-content.com"
    - "+.mzstatic.com"
    - "+.itunes.apple.com"
    - "+.push.apple.com"

    # =========================================================
    # Amazon / AWS
    # =========================================================
    - "+.amazon.com"
    - "+.amazonaws.com"
    - "+.amazonvideo.com"
    - "+.aws.amazon.com"

    # =========================================================
    # Netflix
    # =========================================================
    - "+.netflix.com"
    - "+.netflix.net"
    - "+.nflxvideo.net"
    - "+.nflximg.net"
    - "+.nflximg.com"
    - "+.nflxso.net"
    - "+.nflxext.com"

    # =========================================================
    # Spotify
    # =========================================================
    - "+.spotify.com"
    - "+.spotifycdn.com"
    - "+.scdn.co"

    # =========================================================
    # Disney+
    # =========================================================
    - "+.disneyplus.com"
    - "+.disney-plus.net"
    - "+.dssott.com"
    - "+.media.dssott.com"

    # =========================================================
    # Twitch
    # =========================================================
    - "+.twitch.tv"
    - "+.twitchcdn.net"
    - "+.ttvnw.net"

    # =========================================================
    # 游戏 / Steam / Epic / PlayStation / Xbox
    # =========================================================
    - "+.steampowered.com"
    - "+.steamcommunity.com"
    - "+.steamstatic.com"
    - "+.steamcontent.com"
    - "+.steamusercontent.com"
    - "+.steamserver.net"
    - "+.epicgames.com"
    - "+.epicgamescdn.com"
    - "+.playstation.com"
    - "+.playstation.net"
    - "+.xbox.com"
    - "+.xboxlive.com"
    - "+.ea.com"
    - "+.eaassets.com"
    - "+.ubisoft.com"
    - "+.ubisoftconnect.com"
    - "+.rockstargames.com"
    - "+.nvidia.com"

    # =========================================================
    # 常用国外资讯 / 社区
    # =========================================================
    - "+.wikipedia.org"
    - "+.wikimedia.org"
    - "+.medium.com"
    - "+.quora.com"
    - "+.stackexchange.com"
    - "+.stackoverflow.com"
    - "+.stackprinter.com"

    # =========================================================
    # 隐私 / DNS / 网络测试
    # =========================================================
    - "+.browserleaks.com"
    - "+.dnsleaktest.com"
    - "+.ipleak.net"
    - "+.ipinfo.io"
    - "+.whatismyipaddress.com"
    - "+.whatismyip.com"
    - "+.whoer.net"

    # =========================================================
    # NTP / 时间同步
    # =========================================================
    - "+.pool.ntp.org"
    - "+.ntp.org"

    # =========================================================
    # 补充：常用协作/工具服务
    # =========================================================
    - "+.notion.so"
    - "+.figma.com"
    - "+.slack.com"
    - "+.zoom.us"
    - "+.teamviewer.com"
```
- Fake-IP-Filter✅
- Fake-IP-Filter-Mode：黑名单模式

```
*.somethingstranges.com
*.lan
*.localdomain
*.example
*.invalid
*.localhost
*.test
*.local
*.home.arpa
*.direct
cable.auth.com
network-test.debian.org
detectportal.firefox.com
resolver1.opendns.com
global.turn.twilio.com
global.stun.twilio.com
app.yinxiang.com
injections.adguard.org
localhost.*.weixin.qq.com
*.blzstatic.cn
*.cmpassport.com
id6.me
open.e.189.cn
opencloud.wostore.cn
id.mail.wo.cn
mdn.open.wo.cn
hmrz.wo.cn
nishub1.10010.com
enrichgw.10010.com
*.wosms.cn
*.jegotrip.com.cn
*.icitymobile.mobi
*.pingan.com.cn
*.cmbchina.com
*.10099.com.cn
*.microdone.cn
+.msftconnecttest.com
+.msftncsi.com
time.*.com
time.*.gov
time.*.edu.cn
time.*.apple.com
time1.*.com
time2.*.com
time3.*.com
time4.*.com
time5.*.com
time6.*.com
time7.*.com
ntp.*.com
ntp1.*.com
ntp2.*.com
ntp3.*.com
ntp4.*.com
ntp5.*.com
ntp6.*.com
ntp7.*.com
+.pool.ntp.org
*.time.edu.cn
*.ntp.org.cn
time.android.com
time.windows.com
music.163.com
*.music.163.com
*.126.net
musicapi.taihe.com
music.taihe.com
songsearch.kugou.com
trackercdn.kugou.com
*.kuwo.cn
api-jooxtt.sanook.com
api.joox.com
joox.com
y.qq.com
*.y.qq.com
streamoc.music.tc.qq.com
mobileoc.music.tc.qq.com
isure.stream.qqmusic.qq.com
dl.stream.qqmusic.qq.com
aqqmusic.tc.qq.com
amobile.music.tc.qq.com
*.xiami.com
*.music.migu.cn
music.migu.cn
localhost.ptlogin2.qq.com
localhost.sec.qq.com
+.qq.com
+.tencent.com
+.wechat.com
+.servicewechat.com
+.weixin.qq.com
+.qqmail.com
+.gtimg.com
+.qpic.cn
+.qlogo.cn
+.tenpay.com
+.myqcloud.com
+.qcloud.com
+.qcloudcdn.com
+.dnsv1.com
+.taobao.com
+.tmall.com
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
+.fhnfile.oss-cn-shenzhen.aliyuncs.com
+.kunlunca.com
+.kunlungr.com
+.aliclouddns.com
+.baidu.com
+.shifen.com
+.bdstatic.com
+.bdydns.com
+.baidubce.com
+.bcebos.com
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
+.ibytedtos.com
+.zijieapi.com
+.pstatp.com
+.toutiao.com
+.toutiaovod.com
+.bytedance.net
+.jd.com
+.jcloudimg.com
+.jd360.hk
+.360buyimg.com
+.jcloud.com
+.bilibili.com
+.bilicdn1.com
+.hdslb.com
+.163.com
+.126.com
+.netease.com
+.163jiasu.com
+.iqiyi.com
+.qy.net
+.iqiyipic.com
+.youku.com
+.ykimg.com
+.tudou.com
+.xiaohongshu.com
+.xhscdn.com
+.xhscdn.net
+.xhslink.com
+.xhsimg.com
+.pinduoduo.com
+.pinduoduo.net
+.yangkeduo.com
+.kuaishou.com
+.yximgs.com
+.ksapisrv.com
+.meituan.com
+.meituan.net
+.dianping.com
+.dpfile.com
+.zhihu.com
+.zhimg.com
+.sina.com.cn
+.weibo.com
dlg.io.mi.com
+.115.com
+.115cdn.com
+.115cdn.net
+.115img.com
+.116cd.com
+.116cd.net
+.anxia.com
+.sq.cc
+.xunlei.com
+.sandai.net
+.n0808.com
+.wscdns.com
+.chinanetcenter.com
+.ourglu.com
+.qingcdn.com
+.qiniu.com
+.qiniucdn.com
+.clouddn.com
+.ksyun.com
+.ksyuncs.com
+.360tpcdn.com
+.mi.com
+.xiaomi.com
+.market.xiaomi.com
+.miui.com
+.huawei.com
+.vmall.com
+.csdn.net
+.jianshu.com
+.sohu.com
+.sogou.com
+.cn
+.battlenet.com.cn
+.wotgame.cn
+.wggames.cn
+.wowsgame.cn
mesu.apple.com
swscan.apple.com
swquery.apple.com
swdownload.apple.com
swcdn.apple.com
swdist.apple.com
lens.l.google.com
stun.l.google.com
na.b.g-tun.com
stun.*.*
stun.*.*.*
+.stun.*.*
+.stun.*.*.*
+.stun.*.*.*.*
+.stun.*.*.*.*.*
+.stun.playstation.net
heartbeat.belkin.com
*.linksys.com
*.linksyssmartwifi.com
*.router.asus.com
local.adguard.org
+.pub.3gppnetwork.org
+.uu.163.com
ps.res.netease.com
+.media.dssott.com
shark007.net
#添加局域网内ddns域名
```

**设置自定义上游 DNS 服务器**（在上方设置中启用本功能后生效）：**

| 服务器分组 | 服务器地址 | 服务器类型 | 状态 | 操作 |
| --- | --- | --- | --- | --- |
| nameserver | 223.5.5.5 | UDP | 启用 | |
| nameserver | 119.29.29.29 | UDP | 启用 | |
| fallback | 1.1.1.1/dns-query#PROXY | HTTPS | 启用 | PROXY为策略节点组配置里的策略组 |
| fallback | dns.google/dns-query#PROXY | HTTPS | 启用 | PROXY为策略节点组配置里的策略组 |
| default- nameserver | 223.5.5.5 | UDP | 启用 |  |
| default- nameserver | 119.29.29.29 | UDP | 启用 |  |

### Meta设置

- 启用 TCP 并发✅
- 启用统一延迟✅
- 其他默认
- 启用流量（域名）探测✅
- 探测（嗅探）纯 IP 连接✅
- 自定义流量探测（嗅探）设置✅
```
# 嗅探域名 可选配置
sniffer:
  force-dns-mapping: true
  parse-pure-ip: true
  override-destination: true
  sniff:
    QUIC:
      ports: [443]
    TLS:
      ports: [443, 8443]
    HTTP:
      ports: [80, 8080-8880]
      override-destination: true
  force-domain:
    - "+.netflix.com"
    - "+.nflxvideo.net"
    - "+.amazonaws.com"
    - "+.media.dssott.com"
    - "+.google.com"
    - "+.googleapis.com"
    - "+.youtube.com"
    - "+.googlevideo.com"
    - "+.facebook.com"
    - "+.instagram.com"
    - "+.twitter.com"
    - "+.telegram.org"
    - "+.openai.com"
    - "+.chatgpt.com"
  skip-domain:
    # 腾讯/微信系
    - "+.qq.com"
    - "+.tencent.com"
    - "+.wechat.com"
    - "+.gtimg.com"
    - "+.qpic.cn"
    - "+.qlogo.cn"
    - "+.myqcloud.com"
    - "+.qcloud.com"
    # 字节跳动/抖音系
    - "+.douyin.com"
    - "+.douyincdn.com"
    - "+.douyinpic.com"
    - "+.iesdouyin.com"
    - "+.douyinvod.com"
    - "+.amemv.com"
    - "+.snssdk.com"
    - "+.byteimg.com"
    - "+.ibytedtos.com"
    - "+.toutiao.com"
    - "+.bytedance.net"
    # 小红书
    - "+.xiaohongshu.com"
    - "+.xhscdn.com"
    - "+.xhslink.com"
    # 阿里系
    - "+.taobao.com"
    - "+.tmall.com"
    - "+.alicdn.com"
    - "+.alibaba.com"
    - "+.alipay.com"
    - "+.aliyun.com"
    - "+.aliyuncs.com"
    - "+.amap.com"
    # 115网盘
    - "+.115.com"
    - "+.115cdn.com"
    - "+.115img.com"
    - "+.116cd.com"
    - "+.anxia.com"
    - "+.sq.cc"
    # 小米
    - "+.mi.com"
    - "+.dlg.io.mi.com"
    # 苹果推送
    - "+.push.apple.com"
    # 国内大厂CDN
    - "+.baidu.com"
    - "+.bdstatic.com"
    - "+.jd.com"
    - "+.bilibili.com"
    - "+.163.com"
    - "+.youku.com"
    - "+.meituan.com"
    - "+.zhihu.com"
    - "+.weibo.com"
    - "+.sina.com.cn"
  # skip-src-address:
  #   - 192.168.0.3/32
  # skip-dst-address:
  #   - 192.168.0.3/32
```

### Smart设置

根据个人使用情况设置

## 规则设置

- 仅代理命中规则流量✅
- 自定义规则✅

**rules:下填写**
```
# 1. NTP 端口强制直连（最高优先级）
- DST-PORT,123,DIRECT

# 2. 禁用阿里系 UDP 443 端口 (HTTP/3 / QUIC)
- AND,((NETWORK,UDP),(DST-PORT,443),(GEOSITE,alibaba)),REJECT

# 3. 禁用腾讯系 UDP 443 端口
- AND,((NETWORK,UDP),(DST-PORT,443),(GEOSITE,tencent)),REJECT

# 4. 禁用字节跳动系 UDP 443 端口
- AND,((NETWORK,UDP),(DST-PORT,443),(GEOSITE,bytedance)),REJECT

# 5. 其他自定义规则...
#- DOMAIN,局域网内DDNS域名,DIRECT

```

## 配置订阅

| 配置文件名 | （自定义） |
| --- | --- |
| 订阅地址 | （自定义） |
| User-Agent | clash.meta/1.19.20 |
| 在线订阅转换 | ✅ |
| 订阅转换服务地址 | （自己的后端或者api.wcc.best） |
| 订阅转换模板 | 自定义模板 |
| 自定义模板地址 | [https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/cfg/Clash_IPLC_VIP.ini](https://raw.githubusercontent.com/VoGter0616/openclash2025/refs/heads/main/cfg/Clash_IPLC_VIP.ini) |

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
> https://github.com/ACL4SSR/ACL4SSR/tree/master/Clash/config
>
> 感谢以上大佬的代码开源，如有侵权告知删
> 
> 如需使用，请自行斟酌后再用，有任何问题VoGter均无义务解决。
> 
> 所有内容均由VoGter收集于互联网，如有侵权告知删。
