
[143. Reoder List](https://leetcode.cn/problems/reorder-list)

[0143_reorder_list](./html/0143_reorder_list.htmll ":include :type=iframe")

<a href="./content/html/0143_reorder_list.html" target="_blank">点击此处在新窗口打开</a>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    if not head or not head.next:
        return head
    
    # step1: 找中点
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # step2: 反转后半部分
    prev = None
    curr = slow.next
    slow.next = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    # step3: 合并
    first, second = head, prev
    while second:
        tmp1 = first.next
        tmp2 = second.next
        
        first.next = second
        second.next = tmp1
        
        first = tmp1
        second = tmp2


head = [1,2,3,4,5] # [1,5,2,4,3]
head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
head.next = a
a.next = b
b.next = c
c.next = d
reorder_list(head)
while head:
    print(head.val)
    head = head.next
```

这道题目（LeetCode 143. 重排链表）的核心思想是 **“拆解、逆转与交叉缝合（Deconstruct, Reverse & Interleave）”**。

它被称为链表题中的“全能选手”，因为解决这一道题，你需要同时动用链表的三大基础技巧：**快慢指针找中点**、**链表反转**以及**多指针合并**。

---

### 一、 核心思想：链表的“折叠重叠”

想象你手里有一条拉直的拉链，我们要把它重排成 $L_0 \to L_n \to L_1 \to L_{n-1} \dots$ 的样子。这就像是：
1.  **从中间剪断**：把拉链分成左、右两半。
2.  **右半段调头**：把右半部分彻底反转过来。
3.  **交错拉合**：左边出一个，右边插一个，像缝衣服一样把它们拼在一起。

---

### 二、 算法逻辑：三部曲



#### 1. 寻找中点（快慢指针）
* **慢指针 (slow)** 走一步，**快指针 (fast)** 走两步。
* 当快指针到头时，慢指针恰好在“腰部”。这就是我们要剪断链表的地方。

#### 2. 逆转后半部分（原地反转）
* 我们把中点以后的节点 `slow.next` 独立出来，进行反转。
* **为什么要反转？** 因为原链表是单向的，我们无法直接从尾巴往回走，反转之后，尾部节点就变成了这半段的“新头”，方便我们向后遍历。

#### 3. 穿针引线（交错合并）
* 现在手里有两条链表：`first`（前半段）和 `second`（反转后的后半段）。
* 我们使用两个临时指针 `tmp1` 和 `tmp2` 提前记下各自的“下一个节点”，然后开始连线：
    * `first.next = second`（左连右）
    * `second.next = tmp1`（右连回左）

---

### 三、 过程模拟 (`1 -> 2 -> 3 -> 4 -> 5`)

1.  **找中点**：
    * `slow` 停在 `3`，`fast` 到达 `5`。
    * 切断：前半部分 `1 -> 2 -> 3`，后半部分 `4 -> 5`。
2.  **反转后半部分**：
    * `4 -> 5` 变成了 `5 -> 4`。
3.  **合并**：
    * **第一轮**：`1` 指向 `5`，`5` 连回 `2`。链表：`1 -> 5 -> 2...`
    * **第二轮**：`2` 指向 `4`，`4` 连回 `3`。链表：`1 -> 5 -> 2 -> 4 -> 3`
    * **结束**：后半段已空，重排完成。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 找中点耗时 $N/2$，反转耗时 $N/2$，合并耗时 $N/2$。总时间依然是线性的。
* **空间复杂度：$O(1)$**
    * **这是本题的核心追求！** 虽然可以用数组存下所有节点再重排，但那样会消耗 $O(N)$ 空间。现在的做法是“原地整容”，只用了几个指针，极其优雅。

---

### 五、 总结金句

> **“这叫‘分而治之，原地乾坤’。重排链表是对单向链表局限性的一次华丽突围。由于不能回头，我们就把后半段倒过来走；由于链表易断，我们就用临时指针提前‘锚定’。这三步走的策略，将一个原本需要随机访问的复杂问题，拆解成了三个极简的线性流程。这种‘以空间换时间’的反向操作（即不消耗额外空间），是面试官最想看到的链表功底。”**

---

### 💡 深度思考
在合并阶段，为什么循环条件是 `while second` 而不是 `while first`？（提示：想想当链表总长度是奇数时，前半段和后半段谁更长一点点？）

