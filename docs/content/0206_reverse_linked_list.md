
[206. Reverse Linked List](https://leetcode.cn/problems/reverse-linked-list)

[0206_reverse_linked_list](./html/0206_reverse_linked_list.html ":include :type=iframe")

<a href="./content/html/0206_reverse_linked_list.html" target="_blank">点击此处在新窗口打开</a>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


head = [1,2,3,4] # [4,3,2,1]
head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
head.next = a
a.next = b
b.next = c
result = reverse_list(head)
while result:
    print(result.val)
    result = result.next
```

这道题目（LeetCode 206. 反转链表）是链表题中的**“基本功之首”**。如果说前面的快慢指针是在赛跑，那么反转链表就像是在玩一场 **“接力变向”** 的游戏。

它的核心思想是 **“迭代更迭（Iterative Reversal）”**。我们需要在不破坏链表结构的前提下，原地修改每一个节点的指向。

---

### 一、 核心思想：调转船头

单链表最磨人的地方在于：它只有 `next` 指向后面，没有“回头路”。要实现反转，我们必须在路过每一个节点时，强行让它从指向“下一家”变成指向“上一家”。

1.  **断开链接**：在改变指向前，必须先找个人（`next_node`）帮我们记住原来的下一家在哪，否则链表就断了。
2.  **反转指向**：让当前的节点（`curr`）指向它的前任（`prev`）。
3.  **全员前移**：前任变现任，现任变继任，大家集体向后挪一步。

---

### 二、 算法逻辑：三指针漂移



#### 1. 初始布局
* `prev`：初始化为 `None`。它是反转后的“新尾巴”。
* `curr`：初始化为 `head`。它是我们当前正在处理的“施工点”。

#### 2. 核心三步走（循环体内）
* **第一步（记路）**：`next_node = curr.next`。先把原本的下一个节点存起来，防止丢路。
* **第二步（调头）**：`curr.next = prev`。这是灵魂一笔，让当前的箭头指回后面去。
* **第三步（挪位）**：
    * `prev = curr`（前任往前挪）。
    * `curr = next_node`（现任往前挪）。

#### 3. 终点结算
* 当 `curr` 变成 `None` 时，说明所有节点都调转完毕了。
* 此时 `prev` 刚好指向原本的最后一个节点，也就是现在的 **新头节点**。

---

### 三、 过程模拟 (`1 -> 2 -> 3 -> 4`)

1.  **第一轮施工**：
    * 记住 `2`。
    * `1` 指向 `None`。
    * `prev` 变成 `1`，`curr` 变成 `2`。
2.  **第二轮施工**：
    * 记住 `3`。
    * `2` 指向 `1`。
    * `prev` 变成 `2`，`curr` 变成 `3`。
3.  **以此类推**...
4.  **最后**：
    * `4` 指向 `3`。
    * `prev` 变成 `4`，`curr` 变成 `None`。
    * 返回 `prev` (即数字 4)，链表变成了 `4 -> 3 -> 2 -> 1`。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 我们只需要老老实实地从头到尾走一遍，每个节点只处理一次。
* **空间复杂度：$O(1)$**
    * 我们只额外用了三个指针变量，完全是在原地“乾坤大挪移”，不需要额外开辟存储空间。

---

### 五、 总结金句

> **“反转链表就像是在黑暗中赶路，你每走一步，都要先用手摸着前面的路（`next_node`），然后转身把身后的路标（`curr.next`）调转方向。只要你前移的步子够稳（`prev` 和 `curr` 的交替），当你走到尽头时，原本的终点就成了新的起点。”**

---

### 下一步建议
反转链表是解决很多复杂题目的“底层组件”。比如：你想判断一个链表是否是 **“回文”** 吗？或者想 **“每 K 个一组反转链表”**（LeetCode 25）？掌握了这一段基础逻辑，那些难题都不过是在这个基础上多套几层循环而已！