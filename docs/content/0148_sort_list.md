
[148. Sort List](https://leetcode.cn/problems/sort-list/)

[0148_sort_list](./html/0148_sort_list.html ":include :type=iframe")

<a href="./content/html/0148_sort_list.html" target="_blank">点击此处在新窗口打开</a>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def sort_list(head):
    if not head or not head.next:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sort_list(head)
    right = sort_list(mid)
    return merge(left, right)


def merge(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next


head = [4,2,1,3] # [1,2,3,4]
head = ListNode(4)
a = ListNode(2)
b = ListNode(1)
c = ListNode(3)
head.next = a
a.next = b
b.next = c
head = sort_list(head)
while head:
    print(head.val)
    head = head.next
```

这道题目（LeetCode 148. 排序链表）的核心思想是 **“分治法（Divide and Conquer）”**。

在数组中，我们常用快排或归并，但在链表这种“只能单向走”的结构中，**归并排序（Merge Sort）** 是最完美的搭档。它能以 $O(n \log n)$ 的时间复杂度将混乱的链表梳理得井井有条。

---

### 一、 核心思想：拆解与重组

你可以把这个过程想象成 **“部门拆分与精英选拔”**：

1.  **无限拆分**：如果一个团队（链表）人太多，管理很乱，我们就从中间一分为二，直到每个团队只剩 **1 个人**。显然，1 个人的团队天然是有序的。
2.  **两两合并**：将两个已经有序的小团队合并成一个更大的有序团队。在合并时，我们只需要比较两个队头的“精英”，谁小谁就先排进去。
3.  **递归回溯**：通过这种自底向上的合并，最终整个链表就变成了一个有序的整体。

---

### 二、 算法逻辑：双剑合璧



#### 1. 寻找中点（快慢指针）
* 链表不像数组能直接访问 `mid`。我们要派出一只 **乌龟（slow）** 和一只 **兔子（fast）**。
* 兔子跑两步，乌龟跑一步。当兔子跑到终点时，乌龟恰好在 **中点**。
* **关键动作**：`slow.next = None`。这一刀下去，链表才真正断成了左右两截。

#### 2. 递归拆解
* 对左半部分调用 `sort_list`，对右半部分调用 `sort_list`。
* 这个过程会一直持续到链表只剩一个节点（递归出口）。

#### 3. 归并合并（Merge）
* 准备一个 **哑节点（dummy）** 作为新排队的起点。
* 比较 `l1` 和 `l2` 的值：
    * 谁小，就把 `curr.next` 指向谁，并移动该链表的指针。
* **收尾**：如果一个队排完了，另一个队还没完，直接把剩下的“挂”在后面即可（因为剩下的本来就是有序的）。

---

### 三、 过程模拟 (`4 -> 2 -> 1 -> 3`)

1.  **第一次拆分**：
    * 中点在 `2`，断开。变为 `[4, 2]` 和 `[1, 3]`。
2.  **继续拆分**：
    * `[4, 2]` 拆为 `[4]` 和 `[2]`。
    * `[1, 3]` 拆为 `[1]` 和 `[3]`。
3.  **开始合并**：
    * **合并 `[4]` 和 `[2]`**：比较发现 2 小，结果为 `2 -> 4`。
    * **合并 `[1]` 和 `[3]`**：比较发现 1 小，结果为 `1 -> 3`。
4.  **终极合并**：
    * `l1: 2 -> 4`, `l2: 1 -> 3`
    * 第一轮：`1 < 2`，拿走 1。
    * 第二轮：`2 < 3`，拿走 2。
    * 第三轮：`3 < 4`，拿走 3。
    * 第四轮：剩下 4，挂在最后。
    * **结果**：`1 -> 2 -> 3 -> 4`。

---

### 四、 复杂度分析

* **时间复杂度：$O(n \log n)$**
    * 每一层合并需要 $O(n)$，而递归树的高度是 $\log n$。这是排序算法能达到的最优上限。
* **空间复杂度：$O(\log n)$**
    * 主要是递归调用产生的栈空间。
    * *注：如果是面试高级岗位，可能会问你如何用迭代法实现 $O(1)$ 空间的排序。*

---

### 五、 总结金句

> **“归并排序在链表上就像是在玩一场‘分而治之’的卡牌游戏。先通过快慢指针找到‘腰斩’的位置，把复杂的乱序问题降解成单节点的自然有序，再利用链表易于插入的特性，像拉拉链一样把两个有序序列严丝合缝地扣在一起。”**
