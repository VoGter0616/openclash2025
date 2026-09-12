<div align="center">

# 🧩 OpenClash，Shadowrocket，Surge 订阅转换配置模板

</div>

<details>
<summary><b>📄 点击展开 / 折叠查看：OpenClash 设置指南</b></summary>

<br>

<!-- OPENCLASH_START -->
<!-- OPENCLASH_END -->

</details>

<details>
<summary><b>📄 点击展开 / 折叠查看：Shadowrocket 设置指南</b></summary>

<br>

<!-- SHADOWROCKET_START -->
<!-- SHADOWROCKET_END -->

</details>

<details>
<summary><b>📄 点击展开 / 折叠查看：Surge 设置指南</b></summary>

<br>

<!-- SURGE_START -->
<!-- SURGE_END -->

</details>

## 📁 `.ini` 模板列表

`cfg` 根目录共有 6 个模板：

| 文件 | 文件类型 | 定位 |
| --- | --- | --- |
| [Clash_IPLC_VIP.ini](./Clash_IPLC_VIP.ini) | ini | OpenClash自定义转换文件，IPLC.VIP专用转换。 |
| [Clash_custom.ini](./Clash_custom.ini) | ini | OpenClash自定义转换文件。 |
| [Clash_test.ini](./Clash_test.ini) | ini | OpenClash转换前测试文件。 |
| [Clash_Verge.ini](./Clash_Verge.ini) | ini | Clash Verge自定义转换文件。 |
| [Shadowrocket_basic.conf](./Shadowrocket_basic.conf) | conf | Shadowrocket自定义转换文件。 |
| [base.yaml](./yaml/base.yaml) | yaml | Clash Verge头文件组成的yaml。 |

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

---

<div align="center">

请以仓库 `main` 分支中的最新文件为准。

</div>

