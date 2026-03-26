
[76. Minimum Window Substring](https://leetcode.cn/problems/minimum-window-substring/)

[0076_minimum_window_substring](./html/0076_minimum_window_substring.html ":include :type=iframe")

```python
def min_window(s, t):
    if not s or not t:
        return ""
    need = dict()
    for c in t:
        need[c] = need.get(c, 0) + 1
    missing = len(t)
    left = start = end = 0
    for right, c in enumerate(s, 1):
        if need.get(c, 0) > 0:
            missing -= 1
        need[c] = need.get(c, 0) - 1
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if end == 0 or right - left < end - start:
                start, end = left, right
    return s[start:end]


s = "ADOBECODEBANC"
t = "ABC"
result = min_window(s, t)
print(result)  
```

这道题目（LeetCode 76. 最小覆盖子串）是滑动窗口算法中的“大 Boss”。如果说前面的“删除重复项”是搬运工，那这道题就是一个 **“伸缩自如的捕鱼网”**。

它的核心思想是 **“滑动窗口（Sliding Window）”**，通过维护一个动态的区间，在 $O(N)$ 的时间内找到满足条件的最小范围。

---

### 一、 核心思想：先吃饱，再减肥

我们要从字符串 `s` 中找到包含 `t` 中所有字符的最小子串。

1.  **扩张（寻找可行解）**：右边界 `right` 不断向右移动，把鱼（字符）抓进网里。直到网里的鱼**刚好凑齐**了我们要的所有种类和数量。
2.  **收缩（寻找最优解）**：一旦鱼凑齐了，我们就尝试把左边界 `left` 向右移。只要网里剩下的鱼依然能凑齐 `t`，我们就不断“减肥”，直到减不动为止。
3.  **动态记忆**：在这个过程中，记录下那个最窄的“网”的尺寸。

---

### 二、 算法逻辑：伸缩循环

以 `s = "ADOBEC...", t = "ABC"` 为例：

#### 1. 记账：我们需要什么？
* 准备一个 `need` 字典。如果 `t = "ABC"`，那我们就记下：`A:1, B:1, C:1`。
* `missing` 变量代表：我们还差多少个字符才能凑齐。

#### 2. 右边界扩张：疯狂吞噬
* 只要 `missing > 0`，`right` 就往右走。
* 碰到一个字符，如果是我们要的，`missing` 减 1。
* 无论是不是我们要的，都在 `need` 字典里把它的欠条减 1（变成负数代表我们手里多出来的溢出货）。

#### 3. 左边界收缩：精简持股
* 当 `missing == 0` 时，说明鱼齐了！
* 此时看 `left` 指向的字符。如果 `need[s[left]] < 0`，说明这个字符是**多余的**（可能是因为 `s` 里本身就多，或者是 `t` 根本不需要）。
* 既然多余，就扔掉它，`left` 右移，直到不能再扔为止。



---

### 三、 过程模拟 (`s = "ADOBECODEBANC", t = "ABC"`)

1.  **扩张阶段**：`right` 一路吃到索引 5（字符 'C'）。此时网里有 "ADOBEC"，包含了 A、B、C。`missing` 变成 0。
2.  **初步收缩**：此时 `left` 指向 'A'。`need['A']` 是 0（不多不少），所以不能收缩。记录当前长度 6。
3.  **继续扩张**：`right` 继续走，吃到了后面的 'B' 和 'A'。
4.  **再次收缩**：当 `right` 走到结尾时，发现前面的 "ADOBE..." 里有很多多余字符。`left` 疯狂右移，跳过 "ADOBE"，最后缩到了 "BANC"。
5.  **结算**：比较发现 "BANC"（长度 4）比之前的 "ADOBEC" 更短，更新答案。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 虽然代码里有 `for` 嵌套 `while`，但每个字符最多被 `right` 扫过一次，被 `left` 扫过一次。它们都是单向奔跑，总操作数是 $2N$。
* **空间复杂度：$O(K)$**
    * $K$ 是字符集的大小（比如 ASCII 128 个字符）。我们只用了字典来存这些字符的频率。

---

### 五、 总结金句

> **“滑动窗口就像是一个有原则的吃货：右边界负责‘贪婪’，不顾一切地把目标装进碗里；左边界负责‘极简’，只要碗里的东西够吃，就拼命把不必要的脂肪减掉。在这一进一出之间，剩下的就是最精华的干货。”**
