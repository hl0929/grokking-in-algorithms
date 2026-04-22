
[567. Permutaion in String](https://leetcode.cn/problems/permutation-in-string)

[0567_permutation_in_string](./html/0567_permutation_in_string.html ":include :type=iframe")

<a href="./content/html/0567_permutation_in_string.html" target="_blank">点击此处在新窗口打开</a>

```python
def check_inclusion(s1, s2):
    if not s1 or not s2:
        return False
    need = [0] * 26
    for ch in s1:
        need[ord(ch) - ord("a")] += 1
    left = 0
    for right in range(len(s2)):
        need[ord(s2[right]) - ord("a")] -= 1
        while need[ord(s2[right]) - ord("a")] < 0:
            need[ord(s2[left]) - ord("a")] += 1
            left += 1
        if right - left + 1 == len(s1):
            return True
    return False
    

s1 = "ab" 
s2 = "eidbaoo" # true
result = check_inclusion(s1, s2)
print(result) 
```

这道题目（LeetCode 567. 字符串的排列）是“滑动窗口”与“哈希计数”的完美结合。如果说“最小覆盖子串”是找一个**足够大**的网，那么这道题就是要在长字符串里找一个**尺寸完全吻合**的“模具”。

它的核心思想是 **“固定长度的滑动窗口”**。

---

### 一、 核心思想：寻找完美的“拼图”

所谓 `s1` 的排列，本质上就是：在 `s2` 中找到一个子串，它包含的字符种类和数量与 `s1` **完全一致**。

1.  **消耗与补偿**：我们先把 `s1` 的所有字符看作是“欠债”（`need` 数组记录正数）。
2.  **窗口移动**：
    * **进窗（消耗）**：右边界 `right` 扫过一个字符，就从欠债表里减去 1。
    * **出窗（补偿）**：如果某个字符减过头了（变成负数），说明窗口里这个字符太多了，或者根本不需要。这时候左边界 `left` 必须右移，把字符还回去，直到平衡。
3.  **等长即成功**：因为我们的窗口逻辑保证了字符数量不会“透支”，所以只要窗口的长度刚好等于 `s1` 的长度，就说明找到了。

---

### 二、 算法逻辑：动态平账

以 `s1 = "ab", s2 = "eidbaoo"` 为例：

#### 1. 记账：s1 的“债务”
* `need` 数组里：`a: 1, b: 1`，其他都是 0。

#### 2. 右边界：疯狂消耗
* `right` 往右走，每遇到一个字符，就在 `need` 对应的位置减 1。
* 比如遇到 'e'，`need['e']` 变成 -1。

#### 3. 左边界：及时止损（while 循环）
* **关键点**：如果 `need[新进来的字符]` 变成了负数，说明当前窗口非法了。
* **动作**：`left` 必须右移，把 `s2[left]` 对应的字符重新加回到 `need` 里（还债），直到刚才那个负数变回 0 为止。
* 这样保证了：**窗口内的任何字符，其消耗量绝不会超过 `s1` 的供应量。**

#### 4. 长度校验
* 如果在上述“平账”之后，窗口的长度 `right - left + 1` 恰好等于 `len(s1)`，说明我们不多不少，正好凑齐了 `s1`。



---

### 三、 过程模拟 (`s1 = "ab", s2 = "eidbaoo"`)

1.  **遇到 'e'**：`need['e']` 变 -1。触发 `while`，`left` 右移吐出 'e'。窗口变空，长度 0。
2.  **遇到 'i'**：同上，窗口变空，长度 0。
3.  **遇到 'd'**：同上，窗口变空，长度 0。
4.  **遇到 'b'**：`need['b']` 从 1 变 0。不触发 `while`。窗口长度 1 (就是 "b")。
5.  **遇到 'a'**：`need['a']` 从 1 变 0。不触发 `while`。窗口长度 2 (就是 "ba")。
6.  **检查**：`2 == len(s1)`。**Bingo！返回 True。**

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 虽然有 `while`，但 `left` 和 `right` 都只把 `s2` 走了一遍。总计 $2 \times \text{len}(s2)$ 次操作。
* **空间复杂度：$O(1)$**
    * `need` 数组的大小固定为 26，与输入字符串的长度无关。

---

### 五、 总结金句

> **“这套算法就像是一个严格的收银员：`s1` 是顾客给的‘面额’。右边界每收一张钞票就减去面值，一旦发现找零找多了（变成负数），左边界就必须立刻退款，直到账面平衡。如果账面平衡且钞票张数对得上，这单买卖就成了。”**
