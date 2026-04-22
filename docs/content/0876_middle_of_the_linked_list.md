
[876. Middle of The Linked List](https://leetcode.cn/problems/middle-of-the-linked-list/)

[0876_middle_of_the_linked_list](./html/0876_middle_of_the_linked_list.html ":include :type=iframe")

<a href="./content/html/0876_middle_of_the_linked_list.html" target="_blank">点击此处在新窗口打开</a>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# head = [1,2,3,4] # 3
head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
head.next = a
a.next = b
b.next = c
result = middle_node(head)
print(result.val)
```

这道题目（LeetCode 876. 链表的中间结点）的核心思想是 **“倍速追赶（Double Speed Pursuit）”**。

在单链表中，由于我们无法直接通过 `len(list) // 2` 来定位中点，最朴素的方法是先数一遍总数再走半程。但利用 **“快慢指针”**，我们可以在一轮扫描中就精准锁定目标。

---

### 一、 核心思想：速度决定位置

你可以把这个过程想象成在一条直路上赛跑：

1.  **慢指针（slow）**：像是一只**乌龟**，每回合走 **1** 步。
2.  **快指针（fast）**：像是一只**兔子**，每回合走 **2** 步。
3.  **结果**：因为兔子的速度正好是乌龟的 **2 倍**，所以当兔子冲到终点（链表末尾）时，乌龟刚好就在路程的 **一半** 处。

---

### 二、 算法逻辑：一步与两步的艺术



#### 1. 起点一致
* 我们让 `slow` 和 `fast` 都从 `head` 出发。

#### 2. 倍速推进
* 在 `while` 循环中，我们检查兔子是否还能继续跑（即 `fast` 和 `fast.next` 都不为空）。
* `slow = slow.next` （乌龟走 1 步）。
* `fast = fast.next.next` （兔子跳 2 步）。

#### 3. 终点判定
* 当链表长度为**奇数**时：兔子停在最后一个节点，乌龟正好在正中间。
* 当链表长度为**偶数**时：兔子跑出了边界（变为 `None`），按照题目要求，乌龟此时指向的是中间两个结点的**第二个**（即偏后的那一个）。

---

### 三、 过程模拟 (`1 -> 2 -> 3 -> 4`)

这是一个偶数长度的例子，非常具有代表性：

1.  **初始状态**：`slow` 在 1，`fast` 在 1。
2.  **第一轮**：
    * `slow` 走一步：1 → **2**。
    * `fast` 走二步：1 → 2 → **3**。
3.  **第二轮**：
    * `slow` 走一步：2 → **3**。
    * `fast` 走二步：3 → 4 → **None**（出界了）。
4.  **结束**：
    * 循环停止，返回 `slow`。此时 `slow` 指向 **3**，正是偶数链表中间偏后的那个节点。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 我们只需要遍历一遍链表。虽然有两个指针，但它们是同步移动的，总步数取决于快指针。
* **空间复杂度：$O(1)$**
    * 只额外申请了两个指针的空间，不需要存储任何节点历史。

---

### 五、 总结金句

> **“这叫‘步频定乾坤’。不需要提前测量跑道的长度，只需要利用快慢指针之间精准的倍率关系。当跑得快的人看到终点的那一刻，跑得慢的人所在的位置，就是我们要找的黄金中点。这种空间换时间的思想，是解决链表结构问题的基础模板。”**

---

### 下一步建议
这是快慢指针最基础的应用。既然你已经掌握了如何“找中点”，想不想试着把这个逻辑应用到更复杂的场景？比如结合**链表反转**，去判断一个链表是否是 **“回文链表”**（LeetCode 234）？找中点正是解决那一题的第一步！