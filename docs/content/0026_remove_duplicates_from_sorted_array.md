
[26. Remove Duplicates from Sorted Array](https://leetcode.cn/problems/remove-duplicates-from-sorted-array)

[0026_remove_duplicates_from_sorted_array](./html/0026_remove_duplicates_from_sorted_array.html ":include :type=iframe")

<a href="./content/html/0026_remove_duplicates_from_sorted_array.html" target="_blank">点击此处在新窗口打开</a>

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


nums = [1,1,2,2,3] # 3
result = remove_duplicates(nums)
print(result)
```

这道题目（LeetCode 26. 删除有序数组中的重复项）的核心思想是 **“双指针（Two Pointers）”**。如果说前面的题目是在做“收割”或“比对”，这道题更像是在做一个 **“高效的搬运工”**。

由于题目要求 **“原地修改”** 且数组是 **“有序”** 的，我们不需要额外的空间，只需要两个指针在数组上“赛跑”。

---

### 一、 核心思想：快慢指针的“过滤”

你可以把这个过程想象成：**一个施工队正在翻修一条排好队的序列，要把重复的人踢走，只留下领头的那一个。**

1.  **慢指针（Slow）**：代表“已经排好、没有重复的队伍”的末尾。
2.  **快指针（Fast）**：代表“正在检查的新元素”。
3.  **核心逻辑**：快指针不停地往前走，寻找**“新鲜面孔”**。一旦发现一个和慢指针不一样的数，就把它搬到慢指针的下一个位置。

---

### 二、 算法逻辑：发现新大陆

以 `nums = [1, 1, 2, 2, 3]` 为例：

#### 1. 初始状态
* `slow` 停在第 0 位（数字 1）。
* `fast` 从第 0 位开始向后扫描。

#### 2. 忽略重复：快指针狂奔
* 当 `fast` 看到 `1` 时，发现和 `slow` 指向的 `1` 一样。
* **动作**：无视它，`fast` 继续往前走。

#### 3. 搬运新数：慢指针扩容
* 当 `fast` 走到数字 `2` 时，发现：**“嘿，这是一个新面孔！”**（`nums[fast] != nums[slow]`）。
* **动作**：
    * `slow` 往前挪一个坑位（`slow += 1`）。
    * 把这个新的 `2` 填到这个坑里（`nums[slow] = nums[fast]`）。



---

### 三、 过程模拟 (`nums = [1, 1, 2, 2, 3]`)

1.  **开始**：`slow = 0`, `fast = 0`。`nums[0]` 是 1。
2.  **fast = 1**：看到 1。`nums[1] == nums[slow]`，跳过。
3.  **fast = 2**：看到 2。**发现新数！**
    * `slow` 变成 1。
    * `nums[1] = 2`。数组变为 `[1, 2, 2, 2, 3]`。
4.  **fast = 3**：看到 2。`nums[3] == nums[slow]` (此时 slow 指向 2)，跳过。
5.  **fast = 4**：看到 3。**发现新数！**
    * `slow` 变成 2。
    * `nums[2] = 3`。数组变为 `[1, 2, 3, 2, 3]`。
6.  **结束**：返回 `slow + 1 = 3`。前三个数 `[1, 2, 3]` 就是我们要的结果。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 快指针 `fast` 仅仅把数组从头到尾走了一遍，没有任何回头的操作。
* **空间复杂度：$O(1)$**
    * 我们只用了两个整数变量（指针），完全没有开辟新数组，符合题目的“原地”要求。

---

### 五、 总结金句

> **“这叫‘新官上任，只留新人’。快指针负责在前方开路侦查，慢指针负责在后方按顺序占坑。只要快指针发现的不是老面孔，就通知慢指针腾出下一个位置，把新人接过来坐下。”**
