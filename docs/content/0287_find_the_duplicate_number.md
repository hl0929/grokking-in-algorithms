
[287. Find the Duplicate Number](https://leetcode.cn/problems/find-the-duplicate-number/) 

[0287_find_the_duplicate_number](./html/0287_find_the_duplicate_number.html ":include :type=iframe")

<a href="./content/html/0287_find_the_duplicate_number.html" target="_blank">点击此处在新窗口打开</a>

```python
def find_duplicate(nums):
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


nums = [1,3,4,2,2] #2 
result = find_duplicate(nums)
print(result)
```

这道题目（LeetCode 287. 寻找重复数）的核心思想是 **“弗洛伊德判圈算法（Floyd's Cycle-Finding Algorithm）”**，也就是俗称的 **“龟兔赛跑”**。

这题最精妙的地方在于：它把一个普通的数组搜索问题，转换成了一个 **“单链表找环入口”** 的拓扑问题。

---

### 一、 核心思想：数组即链表

为什么数组可以看成链表？
* 如果我们把数组的值 `nums[i]` 看作是“指向下一个节点的指针”，那么 `0 -> nums[0] -> nums[nums[0]]` 就构成了一条路径。
* 因为数组中有 **重复的数字**，意味着有两个不同的“房间”都指向了同一个“房间”。
* **结论**：在链表的语言里，这就叫 **“入环点”**。重复的那个数字，就是环的入口。

---

### 二、 算法逻辑：两阶段追逐



#### 第一阶段：确认有环（找相遇点）
* **乌龟（slow）** 每次走一步：`slow = nums[slow]`。
* **兔子（fast）** 每次走两步：`fast = nums[nums[fast]]`。
* 只要有重复数，路径就一定有环。兔子虽然跑得快，但最终会在环里从后面追上乌龟。
* **当 `slow == fast` 时**，它们在环内的某一点相遇了。

#### 第二阶段：寻找入口（找重复数）
* 此时，让乌龟回到起点（`slow = 0`），兔子留在原地（相遇点），但速度降为 **每次走一步**。
* **神奇的数学定理**：当它们再次相遇时，相遇的位置恰好就是 **环的入口**。
* 这个入口对应的数字，就是那个被多个指针指向的 **重复数**。

---

### 三、 过程模拟 (`nums = [1, 3, 4, 2, 2]`)

我们可以把跳转逻辑写出来：`0 -> 1 -> 3 -> 2 -> 4 -> 2 (循环)`

1.  **第一阶段（找相遇点）**：
    * `slow` 路径：0 → 1 → 3 → 2
    * `fast` 路径：0 → 3 → 4 → 2
    * 在数字 **2** 处，`slow == fast`，第一阶段结束。

2.  **第二阶段（找入口）**：
    * `slow` 回到起点 0，`fast` 留在 2。
    * 两人同时走一步：
        * `slow`: 0 → 1
        * `fast`: 2 → 4
    * 再走一步：
        * `slow`: 1 → 3
        * `fast`: 4 → 2
    * *等等，这个例子中由于环的特殊性，第二次相遇点依然是 2。*
    * **返回结果**：2。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 第一阶段兔子最多跑两圈，第二阶段乌龟最多走一圈，总路程是线性的。
* **空间复杂度：$O(1)$**
    * **这是本题最强悍的地方！** 我们没有用哈希表（那需要 $O(N)$ 空间），也没有排序（那会修改原数组），只用了两个指针。

---

### 五、 总结金句

> **“这是一个关于‘宿命’的算法。重复的数字就像是时空裂缝，让原本笔直的道路变成了无尽的循环。乌龟和兔子在环里相撞的那一刻，其实已经拿到了开启真相的钥匙。只需要重新出发，在下一次重逢时，裂缝的起点便会现形。”**
