自用模板及测试

屏蔽adobe 给足权限排最上，单纯在应用层选择屏蔽只会屏蔽国外链接，因为国内也能访问adobe部分页面，因此在openclash中如果选择了绕过大陆，
国内能访问的adobe域名或ip也就跟着绕过了内核直接走了直连，所以还需在【插件设置】-【流量控制】-【绕过指定区域 IPv4 黑名单中】加上adobe域名：如下
adobe.com
adobelogin.com
adobe.io
behance.net

--- 最高优先级时间同步直连  ---
把下述添加到自定义规则里的优先规则
 1. 强制拦截全球所有 123 端口的时间同步流量走直连 (这行是最核心的，已经能盖住 99% 的情况)
- DST-PORT,123,DIRECT

2. 精准补漏 NASA 时间域名，强行直连
- DOMAIN-SUFFIX,nasa.gov,DIRECT

 3. 精准补漏微软 Windows 系统自带的时间域名，强行直连
- DOMAIN-SUFFIX,time.windows.com,DIRECT

https://github.com/Aethersailor/Custom_OpenClash_Rules/tree/main/rule
https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Clash
ruleset=🟦 OKX,clash-domain:https://xxx/okx.yaml,86400
可以转换为：https://testingcf.jsdelivr.net/gh/{用户名}/{仓库名}@{分支名}/{文件路径}
