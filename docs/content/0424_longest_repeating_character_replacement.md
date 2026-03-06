
[0424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)

[0424_longest_repeating_character_replacement](./html/0424_longest_repeating_character_replacement.html ':include :type=iframe')

```python
def longest_repeating(s, k):
    repeat_map = dict()
    max_len = max_cnt = 0
    left = 0
    for right in range(len(s)):
        repeat_map[s[right]] = repeat_map.get(s[right], 0) + 1
        max_cnt = max(max_cnt, repeat_map[s[right]])
        if (right - left + 1) - max_cnt > k:
            repeat_map[s[left]] -= 1
            left += 1
        max_len = max(max_len, (right - left + 1))
    return max_len


s = "AABABBA" 
k = 1
result = longest_repeating(s, k)
print(result)
```

这个算法题目（LeetCode 424. 替换后的最长重复字符）是**滑动窗口（Sliding Window）**技巧的经典进阶应用。

它的核心逻辑可以被称为**“非收缩窗口”**策略，其核心思想是：**维护一个窗口，使得“窗口长度”与“窗口内出现频率最高的字符次数”之差不超过 $k$。**

### 一、 核心思想：窗口的“动态平衡”

我们要寻找的是一个最长的区间，这个区间满足：


$$\text{窗口长度} - \text{窗口内出现次数最多的字符频率 (max\_cnt)} \le k$$

* **窗口长度**：当前我们观察的范围。
* **max_cnt**：窗口内那个“主导字符”的数量。
* **差值**：就是我们需要替换掉的“杂质字符”数量。

只要“杂质”数量不大于 $k$，这个窗口就是合法的。

---

### 二、 算法逻辑的三步走

以 `s = "AABABBA", k = 1` 为例：

#### 1. 扩张（右指针 `right` 移动）

不断向右移动 `right` 指针，将新字符加入窗口。同时更新哈希表（或数组）中的字符计数，并动态维护一个 `max_cnt`（记录当前窗口内，或是历史上出现过的最高频率）。

#### 2. 判定与平移（左指针 `left` 移动）

当我们发现 `(right - left + 1) - max_cnt > k` 时，说明当前窗口内的“杂质”太多了，即使把 $k$ 次替换机会都用掉，也无法让窗口内全是重复字符。

* **注意**：此时我们只将 `left` 右移**一步**。
* **关键点**：我们不需要用 `while` 循环把窗口缩得很小，我们只需要让窗口**停止扩张**。因为我们追求的是“最长”长度，一旦我们达到过某个长度（比如 4），除非能找到长度为 5 的解，否则我们没必要把窗口缩回长度 2。

#### 3. 更新全局最大值

在每一步中，我们记录 `max_len = max(max_len, right - left + 1)`。

---

### 三、 两个高频面试追问（深度理解）

#### 1. 为什么 `max_cnt` 在左指针移动时不需要减小？

这是该算法最精妙、也最难理解的地方。

* `max_cnt` 实际上代表了我们**历史上探索到的最佳“主导字符”能力**。
* 如果我们要打破现有的 `max_len` 记录，我们需要一个新的窗口满足：`新长度 - 新max_cnt <= k`。
* 这意味着 `新max_cnt` 必须比 `旧max_cnt` 更大才有意义。
* 如果当前的 `max_cnt` 减小了，窗口只会变得更不合法。所以，**我们只需要关心 `max_cnt` 何时增加**，而不需要在它减小时去精确同步。

#### 2. 窗口为什么不“缩水”？

该算法的窗口大小是**单调不减**的。它像一个探测器，一旦发现了一个长度为 4 的合法区间，它就会维持这个大小（或者更大）向后滑动。如果后面的区域不合法，它就带着这个“历史最大规模”平移；如果遇到了更好的区域，它就进一步扩张。

---

### 四、 算法总结

| 维度 | 描述 |
| --- | --- |
| **核心技巧** | 滑动窗口 (Sliding Window) |
| **空间复杂度** | $O(1)$ (因为字符集大小固定，如 26 个大写字母) |
| **时间复杂度** | $O(N)$ (每个字符仅被左右指针扫描一次) |
| **直观理解** | 保持窗口规模，寻找能容纳更多相同字符的“风水宝地”。 |

通过这种方式，算法将一个看似需要多次遍历的复杂问题，优化成了只需要一次扫描的线性任务。