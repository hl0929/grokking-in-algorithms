
[19. Remove Nth Node From End of List](https://leetcode.cn/problems/remove-nth-node-from-end-of-list)

[0019_remove_nth_node_from_end_of_list](./html/0019_remove_nth_node_from_end_of_list.html ":include :type=iframe")

<a href="./content/html/0019_remove_nth_node_from_end_of_list.html" target="_blank">点击此处在新窗口打开</a>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def remove_nth_from_end(head, n):
    dummy = ListNode(-1, head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


head = [1,2,3,4,5] 
n = 2 # [1,2,3,5]
head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
head.next = a
a.next = b
b.next = c
c.next = d
result = remove_nth_from_end(head, n)
while result:
    print(result.val)
    result = result.next
```


这道题目（LeetCode 19. 删除链表的倒数第 N 个结点）的核心思想是 **“前后指针（Forward & Backward Pointers）”**，也有人形象地称之为 **“尺取法”**。

在单链表中，我们无法从后往前数，但这难不倒聪明的开发者。我们只需要利用两个指针维护一个 **“固定长度的间距”**，就能精准定位倒数第 $N$ 个位置。

---

### 一、 核心思想：拉开身位的“侦查员”

你可以把这个过程想象成两名特种兵在执行任务：

1.  **先遣兵（fast）**：先出发，向前走 $N$ 步。
2.  **后勤兵（slow）**：在先遣兵走了 $N$ 步之后才出发。
3.  **同步推进**：两人保持这 $N$ 个身位的距离同时向前走。
4.  **精准打击**：当先遣兵到达 **终点（最后一个节点）** 时，后勤兵刚好就停在 **待删除节点的前一个位置**。

---

### 二、 算法逻辑：双指针位移



#### 1. 设立哨兵（dummy node）
* 为什么要用 `dummy`？因为如果要删除的是头节点（比如删倒数第 5 个，而链表总共就 5 个），没有 `dummy` 我们就会陷入“找不到前驱节点”的尴尬。
* `dummy` 就像是一个永远不会被删除的“0 号位”，保证了逻辑的统一。

#### 2. 拉开间距
* 让 `fast` 指针先走 $N$ 步。此时，`fast` 和 `slow` 之间隔了 $N$ 个节点。

#### 3. 齐头并进
* 同时移动 `fast` 和 `slow`，直到 `fast.next` 为空（即 `fast` 走到了链表的最后一个节点）。
* 此时，由于两人间距没变，`slow` 指针刚好指在 **倒数第 $N+1$ 个** 节点上。

#### 4. 切断联系
* 执行 `slow.next = slow.next.next`。
* 这一步相当于让 `slow` 直接跳过了那个“讨人嫌”的倒数第 $N$ 个节点，将其从链表中“抹除”。

---

### 三、 过程模拟 (`1 -> 2 -> 3 -> 4 -> 5, n = 2`)

1.  **初始化**：`dummy -> 1 -> 2 -> 3 -> 4 -> 5`，`slow` 和 `fast` 都在 `dummy`。
2.  **fast 先走 2 步**：`fast` 来到了节点 `2`。
3.  **同时移动**：
    * 第一步：`fast` 到 `3`，`slow` 到 `1`。
    * 第二步：`fast` 到 `4`，`slow` 到 `2`。
    * 第三步：`fast` 到 `5`（终点！）。此时 `slow` 在 `3`。
4.  **删除操作**：
    * `slow.next` 原本是 `4`。
    * 执行 `slow.next = slow.next.next`（即 `3.next = 5`）。
    * 节点 `4` 成功被踢出队伍。
5.  **结果**：`1 -> 2 -> 3 -> 5`。

---

### 四、 复杂度分析

* **时间复杂度：$O(L)$**
    * $L$ 是链表的长度。我们只对链表进行了一次完整的遍历，效率极高。
* **空间复杂度：$O(1)$**
    * 只额外申请了 `slow`、`fast` 和 `dummy` 三个指针空间。

---

### 五、 总结金句

> **“在单向行驶的链表公路上，回头看是不可能的。但只要我们派出一名先行者去拉开‘身位差’，后随者就能在先行者抵达终点时，通过这种‘时空错位’精准锁定倒数的位置。这叫：‘以逸待劳，借位制胜’。”**

这种“双指针身位差”的技巧是链表问题中的必备招式。既然你已经掌握了如何“删除倒数第 $N$ 个”，想不想试试看如何用类似的双指针逻辑，**一轮遍历** 就找到链表的 **“中间节点”**（LeetCode 876）？那个逻辑更简单，只需要调整一下两人的“步频”即可！