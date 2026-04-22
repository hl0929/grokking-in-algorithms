
[234. Palindrome Linked List](https://leetcode.cn/problems/palindrome-linked-list/)

[0234_palindrome_linked_list](./html/0234_palindrome_linked_list.html ":include :type=iframe")

<a href="./content/html/0234_palindrome_linked_list.html" target="_blank">点击此处在新窗口打开</a>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def is_palindrome(head):
    # 找中点
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 反转后半部分
    prev, curr = None, slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    # 比较两部分
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True


head = [1,2,2,1] #true | head = [1,2] #false
head = ListNode(1)
a = ListNode(2)
b = ListNode(2)
c = ListNode(1)
head.next = a
a.next = b
b.next = c
result = is_palindrome(head)
print(result)
```


这道题目（LeetCode 234. 回文链表）的核心思想是 **“空间转换与双向奔赴”**。

由于链表不能像数组那样直接通过下标 `left` 和 `right` 对撞比较，这道题最精妙的地方在于它结合了链表的三个经典技巧：**快慢指针**、**链表反转**、**双指针比较**。

---

### 一、 核心思想：镜像折叠

你可以把这个过程想象成 **“折纸游戏”**。为了判断一张长纸条（链表）两端的文字是否对称，我们先找到中点，把后半段纸条 **反转** 过来，然后让两端文字 **“面对面”** 逐一对比。

1.  **确定中位**：利用快慢指针，精准定位链表的“腰部”。
2.  **原地掉头**：把后半部分的指向全部反转，让原本向后走的链表改成向前走。
3.  **双头比对**：从原链表头和反转后的新头同时出发，只要有一个字符对不上，回文就宣告破灭。

---

### 二、 算法逻辑：三部曲



#### 1. 寻找中点（快慢指针）
* **乌龟（slow）** 走一步，**兔子（fast）** 走两步。
* 当兔子到达终点时，乌龟刚好停在链表的 **中间位置**。
* *无论链表长度是奇是偶，这个方法都能准确把链表切成两半。*

#### 2. 原地掉头（反转后半段）
* 从 `slow` 指针开始，我们将链表的 `next` 指针反向。
* **动作**：使用 `prev` 和 `curr` 两个指针，让当前节点指向前一个节点。
* *这一步不需要额外空间，直接在原链表上操作。*

#### 3. 面对面比对
* **左头（left）**：指向原链表的头。
* **右头（right）**：指向反转后产生的“新头”（即原链表的尾巴）。
* **同步移动**：同时向中间靠拢，对比 `val`。如果全部一致，那就是回文。

---

### 三、 过程模拟 (`1 -> 2 -> 2 -> 1`)

1.  **找中点**：
    * `slow` 最终停在第二个 `2`。
    * 链表现在被看作 `[1, 2]` 和 `[2, 1]` 两部分。
2.  **反转后半部分**：
    * 将 `2 -> 1` 反转为 `1 -> 2`。
    * 此时我们有两个入口：一个是原始的 `head`（指向 `1`），一个是反转后的 `prev`（指向 `1`）。
3.  **双指针比对**：
    * 第一位：`1 == 1`，过。
    * 第二位：`2 == 2`，过。
    * `right` 走到底了，匹配成功！

---

### 四、 复杂度分析

* **时间复杂度：$O(n)$**
    * 找中点 $O(n/2)$，反转 $O(n/2)$，比较 $O(n/2)$。总共还是线性的。
* **空间复杂度：$O(1)$**
    * 这是本方案最优雅的地方。通过原地修改指针，我们完全没有用到额外的数组或栈。

---

### 五、 总结金句

> **“这道题是链表技巧的‘全家桶’。它不借用外部容器，而是通过改变链表的‘拓扑结构’，把一个难以逾越的反向访问问题，巧妙地转化成了两个同向链表的对等匹配。这种在有限空间里‘乾坤大挪移’的思维，正是高效算法的魅力所在。”**

掌握了这一题，你就同时掌握了 **“找链表中点”** 和 **“反转链表”** 这两个高频面试核心点。想一想，如果面试官要求 **不能修改原链表结构**，你该如何用 **递归** 的方式来实现同样的功能呢？