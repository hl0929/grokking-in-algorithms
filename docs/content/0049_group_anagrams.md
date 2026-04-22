
[49. Group Anagrams](https://leetcode.cn/problems/group-anagrams)

[0049_group_anagrams](./html/0049_group_anagrams.html ":include :type=iframe")

<a href="./content/html/0049_group_anagrams.html" target="_blank">点击此处在新窗口打开</a>

```python
def group_anagrams(strs):
    groups = dict()
    for s in strs:
        ch_list = [0] * 26
        for ch in s:
            ch_list[ord(ch) - ord("a")] += 1
        key = tuple(ch_list)
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"] # [["bat"],["nat","tan"],["ate","eat","tea"]]| 
result = group_anagrams(strs)
print(result)
```

这道题目（LeetCode 49. 字母异位词分组）是前两道题的“终极进化版”。如果说“有效的字母异位词”是检查**两份清单**是否一致，那么这道题就是要求你把**成百上千份清单**进行**“归类存档”**。

它的核心思想是：**“特征提取（Hashing for Grouping）”**。

---

### 一、 核心思想：给单词办“身份证”

在“两数之和”里，我们记录的是数字的需求；在这里，我们要为每一个单词生成一张**唯一的身份证（Key）**。

1.  **同源同证**：只要两个单词是字母异位词（比如 "eat" 和 "tea"），它们统计出来的字母频率一定是一模一样的。
2.  **以证找组**：我们建立一个大仓库（哈希表 `groups`），身份证就是“柜子编号”，长得一样的单词都扔进同一个柜子里。

---

### 二、 算法逻辑：三步走

以 `strs = ["eat", "tea", "tan"]` 为例：

#### 1. 刻章：统计字符频率
对于每一个单词（如 `"eat"`），我们不看它的顺序，只看它的组成。
* 我们准备一个长度为 26 的数组 `ch_list`。
* `"eat"` 刻出来的章是：`a:1, e:1, t:1`，其余全为 0。

#### 2. 备案：转化为不可变的“键”
在 Python 中，列表是不能直接当字典的 Key 的（因为它会变）。所以代码里有一步关键操作：`key = tuple(ch_list)`。
* 这就像是把刚才刻好的章**过塑封死**，变成了一个不可修改的“标准身份证”。



#### 3. 入库：物以类聚
* 去 `groups` 仓库里查：**“有没有拿这个身份证登记过的柜子？”**
* **没见过**：新开一个柜子，把单词放进去。
* **见过**：直接把单词扔进那个旧柜子。

---

### 三、 过程模拟 (`strs = ["eat", "tea", "tan"]`)

1.  **遇到 "eat"**:
    * 统计：`[1, 0, ..., 1, ..., 1, ...]` (a:1, e:1, t:1)
    * 转化：将其变为 `tuple` 作为 Key。
    * 操作：仓库里没这个 Key，新建 `groups[key] = ["eat"]`。

2.  **遇到 "tea"**:
    * 统计：同样得到 `a:1, e:1, t:1` 的频率。
    * 转化：生成的 Key 与 "eat" **完全一致**！
    * 操作：发现仓库已有此 Key，追加到列表：`groups[key] = ["eat", "tea"]`。

3.  **遇到 "tan"**:
    * 统计：得到 `a:1, n:1, t:1`。
    * 转化：生成了一个全新的 Key。
    * 操作：新建柜子：`groups[new_key] = ["tan"]`。

---

### 四、 复杂度分析

* **时间复杂度：$O(N \times K)$**
    * $N$ 是单词的总个数，$K$ 是单词的最大长度。
    * 我们需要遍历每个单词（$N$），且对每个单词统计频率（$K$）。

* **空间复杂度：$O(N \times K)$**
    * 最坏情况下，如果没有两个单词是异位词，我们需要存下所有的字符串。

---

### 五、 总结金句

> **“这个算法就像是一个大型分拣中心。每一个单词进来先脱掉‘顺序’的外衣，露出‘频率’的肉身。只要肉身一致，管你以前叫 tea 还是 eat，通通关进同一个小黑屋。”**
