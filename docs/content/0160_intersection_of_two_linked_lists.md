
[160. Intersection of Two Linked Lists](https://leetcode.cn/problems/intersection-of-two-linked-lists)

[0160_intersection_of_two_linked_lists](./html/0160_intersection_of_two_linked_lists.html ":include :type=iframe")

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    nodeA, nodeB = headA, headB
    while nodeA != nodeB:
        nodeA = nodeA.next if nodeA else headB
        nodeB = nodeB.next if nodeB else headA
    return nodeA


# listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 # 2
listA = ListNode(1)
a = ListNode(9)
b = ListNode(1)
c = ListNode(2)
d = ListNode(1)
listA.next = a
a.next = b
b.next = c
c.next = d
listB = ListNode(3)
listB.next = c
result = get_intersection_node(listA, listB)
print(result.val)
```

这道题目（LeetCode 160. 相交链表）的核心思想是 **“浪漫相遇论（The Romantic Encounter）”**，在算法界它有一个更响亮的名字叫 **“双指针对等遍历”**。

这道题最精妙的地方在于：两个链表的长度可能不同，但通过一次“身份互换”，我们能让两个指针走过完全相等的路程。

---

### 一、 核心思想：走过你走过的路

如果两个链表相交，它们会形成一个 “Y” 字型。因为前面的引道长度不同，两个指针同步走很难同时到达交点。

**解决办法：**
1.  **A 走完 A 的路，再去走 B 的路。**
2.  **B 走完 B 的路，再去走 A 的路。**
3.  **结果：** 两人走过的总路程都是 `链表A的长度 + 链表B的长度`。既然路程相等，步频相同，那么他们如果有交点，就一定会**在交点处相遇**；如果没有交点，他们最终会同时走到终点（`None`）。

---

### 二、 算法逻辑：消除长度差



#### 1. 裁判起跑
* 设定 `nodeA` 指向 `headA`，`nodeB` 指向 `headB`。

#### 2. 身份互换（循环体内）
* `nodeA` 不断向后走。如果走到头了（变成 `None`），就立刻转场到 `headB` 的起点。
* `nodeB` 不断向后走。如果走到头了（变成 `None`），就立刻转场到 `headA` 的起点。

#### 3. 相遇判定
* 在这个过程中，只要 `nodeA == nodeB`，循环就会停止。
* **情况 1（相交）：** 他们会在交点第一次碰面。
* **情况 2（不相交）：** 他们会各自走完 $L1+L2$ 的路程，最后同时变成 `None`，此时 `None == None`，循环依然停止，返回 `None`。

---

### 三、 过程模拟 (`listA = [1,9,1,2,4], listB = [3,2,4]`)

假设交点是 `2`：
1.  **第一轮：**
    * `nodeA` 走完 `1, 9, 1, 2, 4`。
    * `nodeB` 走完 `3, 2, 4`。
    * 此时 `nodeB` 先到头，它转场去 `listA` 的开头（即指向 `1`）。
2.  **第二轮：**
    * `nodeA` 也到头了，它转场去 `listB` 的开头（即指向 `3`）。
    * 重点来了：此时 `nodeA` 走的是 `B` 的路，`nodeB` 走的是 `A` 的路。
    * 经过抵消，它们会**同时**来到交点 `2`。

---

### 四、 复杂度分析

* **时间复杂度：$O(M + N)$**
    * $M$ 和 $N$ 分别是两个链表的长度。每个指针最多走过两个链表的总长度。
* **空间复杂度：$O(1)$**
    * 我们只用了两个额外的指针，没有使用哈希表来存储节点（虽然哈希法也能做，但需要 $O(M)$ 空间）。

---

### 五、 总结金句

> **“这叫‘错位时空的重逢’。如果我走的路比你长，那我就去走你走过的路，补齐那段差值。只要我们最终的终点是一致的，那么在互换身份的那一刻起，我们就注定会在那个交汇点相撞。这也许是所有链表算法中最浪漫的一个方案。”**

---

### 下一步建议
这种“消除长度差”的思想在处理链表问题时非常有用。你已经看过了很多双指针的用法：**快慢指针（找环、找中点）**、**固定间距指针（找倒数第 N）**，以及今天的 **身份互换指针（找交点）**。这三板斧舞好了，链表题目你基本就能横着走了！需要我帮你总结一下这三种双指针的区别吗？
