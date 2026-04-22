
[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

[0003_longest_substring_without_repeating_characters](./html/0003_longest_substring_without_repeating_characters.html ":include :type=iframe")

<a href="./content/html/0003_longest_substring_without_repeating_characters.html" target="_blank">点击此处在新窗口打开</a>

```python
def longest_substring(s):
    nonrepeat_set = set()
    max_len = 0
    left = 0
    for right in range(len(s)):
        while s[right] in nonrepeat_set:
            nonrepeat_set.remove(s[left])
            left += 1
        nonrepeat_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


s = "qrsvbspk"
result = longest_substring(s)
print(result)
```

这道题目（LeetCode 3. 无重复字符的最长子串）的核心思想是 **“滑动窗口（Sliding Window）”**，辅以 **“哈希集合（HashSet）”** 作为冲突检测器。

它的逻辑可以形象地理解为在字符串上拉动一把**具有弹性的尺子**。

### 一、 核心思想：维护一个“纯净”的窗口

算法的目标是找到一个最长的子区间，里面没有任何重复字母。为了实现 $O(N)$ 的高效执行，它遵循以下原则：

1. **贪心扩张**：右指针 `right` 总是尽可能地向右走，试图吞掉更多的字符来增加长度。
2. **被迫收缩**：一旦 `right` 吞下的字符在当前窗口里已经存在了（冲突），左指针 `left` 就必须出来“清理门户”。
3. **不走回头路**：`left` 和 `right` 都只会向右移动，不会像暴力破解那样反复回溯。

---

### 二、 算法逻辑的三个关键动作

#### 1. 探测（Explore）

`right` 指针每移动一步，就问哈希表：“这个新来的字符，咱家窗口里现在有吗？”

#### 2. 清理（Cleanup）

如果哈希表说“有”：

* 这意味着此时窗口是不合法的。
* **逻辑精髓**：我们不需要知道重复的字符具体在哪，只需要不断地让 `left` 向右移，并从哈希表中移除 `left` 指向的字符。
* 这个过程会一直持续，直到把那个造成冲突的旧字符“挤出”窗口为止。

#### 3. 记录（Record）

每当窗口恢复到“无重复”的状态（即 `while` 循环结束），我们计算当前窗口的长度 `right - left + 1`，并更新历史最大值 `max_len`。

---

### 三、 为什么这个算法比暴力法快？

* **暴力法 ($O(N^2)$)**：枚举所有可能的起点和终点，对每个子串都检查一遍是否有重复。这相当于在原地踏步，做了大量重复工作。
* **滑动窗口 ($O(N)$)**：利用了**区间的连续性**。
* 如果从索引 $i$ 到 $j$ 是无重复的，那么从 $i+1$ 到 $j$ 肯定也是无重复的。
* 通过滑动窗口，我们利用了已知的“纯净”区间，避免了重复检测。



---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 虽然代码里嵌套了一个 `while` 循环，但从宏观来看：字符串中的每个字符最多被 `right` 指针“入队”一次，被 `left` 指针“出队”一次。总操作数是 $2N$ 级别的。


* **空间复杂度：$O(K)$**
* $K$ 是字符集的大小（比如 ASCII 码是 128，Unicode 更多）。哈希集合最多存储这么多字符。



### 五、 总结金句

> **“右指针负责为理想开拓疆土，左指针负责为错误买单。每当现实（重复字符）击碎理想，左指针就断舍离，直到窗口重新变回纯粹的样子。”**
