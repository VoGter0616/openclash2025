<div align="center">

# 🧩 OpenClash 订阅转换模板

</div>

---

> [!IMPORTANT]
> 三种路径解决的是“如何获得并维护策略组、规则和节点来源”，不能替代 OpenClash LuCI 中的插件设置。建议选择一种主路径，不要在不了解执行顺序和覆盖关系时叠加使用。

### 三种路径怎么选

| 使用路径 | 优点 | 代价与限制 | 推荐人群 |
| --- | --- | --- | --- |
| **① 订阅转换 + `.ini` 模板** | 操作最简单；在 OpenClash 中更新和切换订阅方便；无需手工维护 YAML | 依赖所选订阅转换后端的可用性、兼容性和隐私保障；也可以自建转换后端 | 希望省事、经常切换配置的大多数用户 |
| **② 远程 YAML 覆写模块** | 无需订阅转换；填写模块变量即可下载对应 YAML 并写入订阅；远程文件可随仓库维护更新 | 需要学会 OpenClash 覆写模块的添加、变量填写和排障；远程更新可能改变下一次加载结果 | 希望简单使用 YAML，又不想手工编辑文件的用户 |
| **③ 下载 YAML 后手工修改并导入** | 自由度最高；配置文件完全由自己控制；不依赖订阅转换后端 | 最复杂、最繁琐；需要理解 YAML、Provider、策略组和规则引用；仓库更新需自行对比迁移 | 熟悉 Mihomo YAML 的高阶用户 |

> [!NOTE]
> 本项目提供的订阅转换模板和 YAML，均由维护者依据典型场景与使用经验推定设计——通俗地说，包含一定程度的“合理脑补”。它们不可能 100% 贴合每个人的节点、地区、业务和网络环境。需要完全个性化的行为时，请自行编写或深度修改 YAML。


## 📁 `.ini` 模板列表

`cfg` 根目录共有 4 个模板：

| 版本 | 文件 | OpenClash 内置名称 | 定位 |
| --- | --- | --- | --- |
| 标准版 | [`Custom_Clash.ini`](./Custom_Clash.ini) | Aethersailor 规则 标准版 Custom_Clash | 均衡的日常分流，建议多数用户优先选择 |
| 标准 Fallback 版 | [`Custom_Clash_Fallback.ini`](./Custom_Clash_Fallback.ini) | — | 标准版策略组改为故障转移，减少人工切换 |
| 轻量版 | [`Custom_Clash_Lite.ini`](./Custom_Clash_Lite.ini) | Aethersailor 规则 轻量版 Custom_Clash_Lite | 减少业务策略组，结构更简洁 |
| 轻量 Fallback 版 | [`Custom_Clash_Lite_Fallback.ini`](./Custom_Clash_Lite_Fallback.ini) | — | 轻量结构与自动故障转移结合 |
| 极简 GFW 版 | [`Custom_Clash_GFW.ini`](./Custom_Clash_GFW.ini) | Aethersailor 规则 极简版(GFW) Custom_Clash_GFW | 主要代理 GFW 相关流量，其余默认直连 |
| 极简 GFW Fallback 版 | [`Custom_Clash_GFW_Fallback.ini`](./Custom_Clash_GFW_Fallback.ini) | — | 极简分流与自动故障转移结合 |
| 重度分流版 | [`Custom_Clash_Full.ini`](./Custom_Clash_Full.ini) | Aethersailor 规则 重度分流版 Custom_Clash_Full | 更多业务、地区与节点用途分组 |
| 重度分流 Fallback 版 | [`Custom_Clash_Full_Fallback.ini`](./Custom_Clash_Full_Fallback.ini) | — | 重度分流结构与自动故障转移结合 |


---

<div align="center">

请以仓库 `main` 分支中的最新文件为准。

</div>
