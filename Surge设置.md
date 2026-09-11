# Surge使用设置

## 设置向导

### 配置当前设备

- 设置为系统代理✅
- 启动增强模式✅
- 在Surge启动时显示该向导✅
点击继续

## 更多（左侧菜单栏最下面）

### 配置

- 从URL安装配置

```
https://raw.githubusercontent.com/VoGter0616/VoGter_Clash/main/cfg/Surge_basic.conf
```

> [!WARNING]
> 复制粘贴后点击下载，等待下载完成即可。Raw地址需要代理才可以正常访问GitHub下载，如果没有代理的条件可以把上述地址转换成国内CDN的地址即可，复制上述地址给AI生成（提示词：转换成testingcf.jsdelivr.net/加速连接）生成的新连接复制粘贴并下载即可使用

> [!WARNING]
> 下载完成后，右键 Surge_basic选择在文本编辑器中编辑
> 根据机场节点协议修改Host，详见[Host] 组标注
> 注意使用的时候一定要将Surge的订阅链接填写至“我的节点”，详见[Proxy Group] 组第7条。

以下是[Host]修改教程，如无专属DNS，则忽视此设置

```
[Host]
# > AnyTLS 节点专用 DNS（按需取消注释，并替换域名与 DNS IP）
# > 用途：机场 AnyTLS 节点必须使用专用 DNS 解析域名，否则测速超时
# > 将 your-domain.com 替换为节点实际域名，1.2.3.4 替换为机场要求的专用 DNS
# *.your-domain.com = server:1.2.3.4
```
***AnyTLS 节点专用 DNS获取方式***

直接拉取订阅机场的Surge订阅链接内的Host数据，将机场/Surge订阅链接复制到浏览器，自动下载生成.conf文件，使用文本编辑打开该文件（注意不要双击打开，右键选择打开方式）。在[Host]里找到该机场节点的域名以及后方的DNS，按照通配符的书写方式把机场anytls协议节点的域名和dns按照上述格式进行复制粘贴并修改。注意每个域名搭配一个dns。

例如

```
[Host]
# > AnyTLS 节点专用 DNS（按需取消注释，并替换域名与 DNS IP）
# > 用途：机场 AnyTLS 节点必须使用专用 DNS 解析域名，否则测速超时
# > 将 your-domain.com 替换为节点实际域名，1.2.3.4 替换为机场要求的专用 DNS
*.your-domain.com = server:dns1
*.your-domain.com = server:dns2
```

以下是[Proxy Group]修改教程，注意一定要用你所使用机场的Surge订阅链接覆盖“policy-path=”里内容，否则没有节点。policy-regex-filter 用来剔除不需要的节点，按需求修改正则表达式内的内容可以剔除不需要的节点。

```
# --- 7. 节点引入入口 ---
# > policy-regex-filter 用来剔除不需要的节点，按需求修改正则表达式内的内容
# > 注意：请把 https://你的机场订阅链接 替换为真实的 Surge 格式订阅链接
我的节点 = smart, policy-path=https://你的机场订阅链接, policy-regex-filter=^((?!(流量|官网|过期|剩余)).)*$, update-interval=86400, no-alert=true, hidden=false, include-all-proxies=true
```
- 修改完成后保存该文件（即覆盖当前文件）
- 右键顶部菜单栏Surge图标，点击切换配置，选择Surge_basic
- 第一次使用会弹出 外部资源，选择 全部更新。后续可手动更新规则（右键顶部菜单栏Surge图标，点击切换配置，选择更新全部外部资源）
- 重载配置 后完成配置

## 使用说明

- 右键顶部菜单栏Surge图标，出站模式选择规则判定
- 下方的规则默认使用最优节点，也可根据自己需求点击修改

> [!WARNING]
> 该设置已满足当前主机代理分流上网，还需要其他增值设置的自行去YouTube学习设置。
> 教程中使用的配置是VoGter个人使用，如有需要增加规则，可自行在Surge配置里进行修改
> 规则集数据来源于blackmatrix7大佬，由衷感谢大佬无私奉献

其他参数根据自身情况设置。

