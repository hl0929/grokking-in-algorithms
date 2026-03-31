
[438. Find all anagrams in a string](https://leetcode.cn/problems/find-all-anagrams-in-a-string) 

[0438_find_all_anagrams_in_a_string](./html/0438_find_all_anagrams_in_a_string.html ":include :type=iframe")

```python
def find_anagrams(s, p):
    if not s or not p or len(s) < len(p):
        return []
    need = [0] * 26
    for ch in p:
        need[ord(ch) - ord("a")] += 1
    need_count = sum(1 for i in need if i > 0)
    
    res = []
    window = [0] * 26
    valid = 0
    left = 0
    for right, ch in enumerate(s):
        idx = ord(ch) - ord("a")
        window[idx] += 1
        if window[idx] == need[idx]:
            valid += 1
        if right - left + 1 > len(p):
            left_idx = ord(s[left]) - ord("a")
            if window[left_idx] == need[left_idx]:
                valid -= 1
            window[left_idx] -= 1
            left += 1
        if right - left + 1 == len(p) and valid == need_count:
            res.append(left)
    return res


s = "cbaebabacd" 
p = "abc" #[0,6] 
result = find_anagrams(s, p)
print(result)
```

这道题目（LeetCode 438. 找到字符串中所有字母异位词）是滑动窗口算法中的 **“精密扫描仪”**。

在“字符串的排列”中，我们只需要找到一个满足条件的子串；而这道题要求我们像雷达扫描一样，在长字符串 $s$ 中找出 **所有** 符合 $p$ 特征的起始位置。

---

### 一、 核心思想：等宽窗口的“特征匹配”

你可以想象 $p$ 是一个 **标准模板（指纹）**，我们拿着一个和 $p$ **等宽** 的透明方框（滑动窗口），在 $s$ 上从左往右匀速滑动。

1.  **指纹建立**：用 `need` 数组记录 $p$ 中每个字母应有的数量。
2.  **动态匹配（Valid 计数器）**：
    * 我们不需要每次移动都重新清点窗口里的字母。
    * **进一个**：右边新字母进来，如果它的数量刚好达到了模板要求，我们的“达标计数器” `valid` 就加 1。
    * **出一个**：左边字母出去，如果它原本是达标的，现在少了一个导致不达标了，`valid` 就减 1。
3.  **坐标存档**：只要 `valid` 达到了模板中所有字母的种类数，说明当前窗口就是一个完美的异位词，记下此时的 `left`。



---

### 二、 算法逻辑：标准四步走

#### 1. 初始化：设定标杆
* 统计 $p$ 中每个字母出现的次数存入 `need`。
* `need_count` 代表 $p$ 中有多少种 **不同** 的字符（比如 $p=$ "abc"，则 `need_count` = 3）。

#### 2. 右边界进窗：更新状态
* `right` 向右移，把新字符加入 `window` 计数器。
* **关键动作**：如果这个字符在 `window` 里的数量 **正好等于** `need` 里的要求，说明这一类字符“凑齐了”，`valid += 1`。

#### 3. 左边界出窗：维持等宽
* **触发条件**：一旦窗口宽度 `right - left + 1` 大于了 $p$ 的长度，左边就必须踢出一个字符以保持窗口大小。
* **撤销动作**：在踢出 `s[left]` 之前，先获取它的索引 `left_idx`。如果它在窗口里的数量 **正好等于** 模板要求，踢掉它后就不达标了，`valid -= 1`。
* 更新 `window[left_idx]` 计数器，`left` 右移。

#### 4. 结果记录
* 当窗口长度正确且 `valid == need_count` 时，说明当前窗口内的字母种类和数量与模板 **严丝合缝**。
* 将此时的 `left` 存入结果列表 `res`。

---

### 三、 过程模拟 (`s = "cbaebabacd", p = "abc"`)

1.  **初始**：模板需要 `{a:1, b:1, c:1}`，目标种类 `need_count = 3`。
2.  **窗口扫到 "cba"**：
    * 'c', 'b', 'a' 陆续进来，每一类都达到 1 个，`valid` 逐步变到 3。
    * **判定**：窗口长度为 3，且 `valid == 3`，记录 `left = 0`。
3.  **向右移一位 (变为 "bae")**：
    * 右边 'e' 进来。
    * 左边 'c' 出去：'c' 原本是 1 个（达标），现在变成 0 个，`valid` 降为 2。
    * **判定**：`valid` 不等于 3，不记录。
4.  **继续向右**：直到窗口扫到最后的 "bac"（索引 6 开始）：
    * 此时 `valid` 再次回到 3，记录 `left = 6`。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 每个字符只进出窗口一次。这种“只更新差异”的逻辑，避免了每次移动都进行 $O(26)$ 的全量数组比较。
* **空间复杂度：$O(1)$**
    * 无论字符串多长，辅助数组的大小固定为 26。

---

### 五、 总结金句

> **“这套算法就像是工厂流水线上的‘精密卡尺’。它维持着一个恒定的宽度在零件上滑动，每向前挪一格，只关心‘新进来的’和‘被踢出的’。这种局部更新的逻辑，让它能以极快的速度扫完整个序列，而不漏掉任何一个吻合的瞬间。”**

这种“动态维护达标数（valid）”的方法是处理 **多集合匹配** 问题的核心套路。掌握了它，你就能在复杂的字符串搜索中实现真正的线性速度。