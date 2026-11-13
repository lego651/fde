# FDE

网站：**https://lego651.github.io/fde/** · 每个客户一个页面：`/fde/<slug>/`（时间线 + 文档）和 `/fde/<slug>/docs/`（全部文档）

| 客户 | 文件夹 | 网址 |
|---|---|---|
| V-Health Rehab Clinic | `VHealth/` | https://lego651.github.io/fde/vhealth/ |

## 怎么用（给 Jason）

文档发布基本是**自动的**。在 Claude Code 里正常让 Claude 做客户的分析、计划、海报、表格就行，它会自动放到对应客户的页面上。

| 你想做什么 | 怎么跟 Claude 说 |
|---|---|
| 做一份新文档并发布 | 正常提需求就行，例如"VHealth 做一份 Google 评价分析" |
| 确保发布（保险起见） | 加一句 **"放到 pages"**，或者输入 **`/fde-docs`** |
| 改文档状态 | "转介绍分析改成已完成"（状态：分析中 / 使用中 / 已完成） |
| 在已有文档里补充内容 | "把这些发现放到转介绍那份文档里" |
| 先看几个方案再决定 | "先给我看3个方案"：只做预览，不发布；选定后再发布 |
| 暂时不要发布 | 直接说"先别 push" |
| **添加新客户** | "新客户：<名字>，<一句话介绍>，logo 是 <链接或文件>"。Claude 会确认文件夹名和网址，再运行 `scripts/new_client.py` |

**每次都提到客户名字。** 有多个客户以后，Claude 要先确定文档属于哪个客户；不确定时会问你。

**Claude 只给了 `claude.ai/artifact/...` 链接？** 那只是预览。补一句"放到 pages"。

### 为什么它一定会做（三层保障）

1. **Skill** `fde-docs`（`.claude/skills/fde-docs/SKILL.md`，已链接到 `~/.claude/skills/`）：完整步骤。
2. **规则**：仓库 `CLAUDE.md` 和全局 `~/.claude/CLAUDE.md` 都写了"客户文档必须发布到 Pages"。
3. **Stop hook**（`~/.claude/settings.json` → `scripts/stop_check.sh`）：Claude 每次准备结束时自动检查。有文件没登记、页面没重新生成、没 commit 或没 push，就**不让它结束**，必须先补完。只在碰过这个仓库的会话里生效。

例外：Claude 完全没把文件放进仓库（只做了 artifact），hook 发现不了，这时候靠第 1、2 层，或者你补一句"放到 pages"。

### 换电脑 / 重新设置

```bash
git clone https://github.com/lego651/fde.git ~/TEMP/fde
ln -sfn ~/TEMP/fde/.claude/skills/fde-docs ~/.claude/skills/fde-docs
```
然后在 `~/.claude/settings.json` 的 `hooks.Stop` 里加：
```json
{ "hooks": [ { "type": "command", "command": "/Users/jason/TEMP/fde/scripts/stop_check.sh", "timeout": 30 } ] }
```
改完 settings 要重启 Claude Code 才生效。

## 结构

```
<Client>/                  一个客户一个文件夹，互不混用
  docs.json                文档清单（唯一需要手改的登记处）
  index.html               时间线页 /<slug>/（顶部文档卡片由脚本生成）
  docs.html                全部文档页 /<slug>/docs/（脚本生成，不要手改）
  deliverables/            HTML / PDF 交付物
  *.md                     Markdown 文档（Jekyll 渲染成 .html）
  assets/                  logo 等
scripts/
  build_docs.py            python3 scripts/build_docs.py <Client> | --all --check
  new_client.py            新建客户（文件夹、页面、首页卡片）
  stop_check.sh            Claude Code Stop hook
.claude/skills/fde-docs/   Skill
*-preview.html             设计预览，不提交、不上线
```

`scripts/`、`CLAUDE.md`、`README.md`、`*-preview.html` 已在 `_config.yml` 里排除，不会出现在网站上。

---

Helping local small and medium businesses (SMBs) adopt AI, and building recurring SaaS revenue from them.

Status: early — go-to-market strategy first. Work is coordinated by Paperclip agents (CEO, CTO, CMO); the founder approves plans and publishes anything public.

## Layout (proposed)

- `strategy/` — positioning, ICP, pricing hypotheses, GTM plan
- `marketing/` — content drafts (never published by agents)
- `research/` — market and competitor notes
