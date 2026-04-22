
[23. Merge K Sorted List](https://leetcode.cn/problems/merge-k-sorted-lists/)

[0023_merge_k_sorted_list](./html/0023_merge_k_sorted_list.html ":include :type=iframe")

<a href="./content/html/0023_merge_k_sorted_list.html" target="_blank">点击此处在新窗口打开</a>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def merge_k_lists(lists):
    import heapq
    heap = []
    for node in lists:
        while node:
            heapq.heappush(heap, node.val)
            node = node.next
    head = curr = ListNode()
    while heap:
        node = ListNode(heapq.heappop(heap))
        curr.next = node
        curr = curr.next
    return head.next


# lists = [[1,4,5],[1,3,4],[2,6]] # [1,1,2,3,4,4,5,6]
a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c
d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f
g = ListNode(2)
h = ListNode(6)
g.next = h
lists = [a, d, g]
result = merge_k_lists(lists)
while result:
    print(result.val)
    result = result.next
```

这道题目（LeetCode 23. 合并 K 个升序链表）的核心思想是 **“全局选优（Global Selection）”**。在算法领域，我们通常称之为 **“多路归并”**。

你提供的这段代码采用了一种非常直观且稳健的方案：利用 **小顶堆（Min-Heap）** 作为“筛选器”，把来自四面八方的数字全部重新洗牌并排序。

---

### 一、 核心思想：大锅饭与精细化筛选

想象你有 $K$ 个已经按个头排好队的方阵，现在要把他们合并成一个大方阵：

1.  **全员入库**：代码的第一步比较“豪爽”，它不管三七二十一，把所有链表里的节点值全部塞进了一个“大锅”（堆）里。
2.  **自动排序**：堆这个结构有个神奇的特性，无论你往里扔什么，它都能以最快速度把 **最小值** 顶到最上面。
3.  **按序取货**：我们只需要不断地从锅顶把最小的那个数拿出来，串成一颗新的链表。



---

### 二、 算法逻辑：堆排序的降维打击

#### 1. 建立仓库
* `heap = []`：这是一个空的“小顶堆”。
* 遍历 `lists` 中的每一个节点，执行 `heappush`。此时，所有的数字都在堆里按某种特定的结构待命。

#### 2. 哨兵带路
* `head = curr = ListNode()`：创建一个 **哑节点（Dummy Node）**。它就像是新链表的“领路人”，不存实际数据，只负责帮我们牵住排好队后的第一个节点。

#### 3. 抽丝剥茧
* `while heap:`：只要堆里还有数字，就执行 `heappop`。
* 每次弹出的都是当前堆里**最小**的数。
* 创建新节点并把它接在 `curr.next` 上，然后 `curr` 向后移动。

---

### 三、 过程模拟 (`lists = [[1,4,5], [1,3,4], [2,6]]`)

1.  **入堆阶段**：
    * 堆里塞进了：`1, 4, 5, 1, 3, 4, 2, 6`。
    * 堆会自动调整，确保最顶端是 `1`。
2.  **出堆阶段**：
    * 第一次 pop：得到 `1`，链表：`Dummy -> 1`
    * 第二次 pop：得到 `1`，链表：`Dummy -> 1 -> 1`
    * 第三次 pop：得到 `2`，链表：`Dummy -> 1 -> 1 -> 2`
    * ...以此类推，直到堆空。
3.  **结果**：`1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`。

---

### 四 : 复杂度分析

* **时间复杂度：$O(N \log N)$**
    * 假设所有链表节点总数为 $N$。每个节点进堆一次、出堆一次，堆操作的时间复杂度是 $\log N$。
* **空间复杂度：$O(N)$**
    * 这段代码创建了一个大小为 $N$ 的堆，并且在最后通过 `ListNode(val)` 创建了全新的 $N$ 个节点。

---

### 五、 总结金句与深度思考

> **“这叫‘海纳百川，唯快不破’。通过一个小顶堆，我们将分散在各个链表里的竞争者全部拉到了同一个赛场。虽然这种做法稍显‘奢侈’（使用了额外空间），但它逻辑清晰，完美规避了多指针比对时的手忙脚乱。”**

---

### 💡 进阶版提示
你提供的代码其实是 **“数值归并”**，它把原本的链表拆散了重造。在实际面试中，更高级的做法是 **“节点归并”**：
* 堆里只存 $K$ 个链表的 **头节点**。
* 每次 pop 出最小节点后，立刻把它的 `next` 节点再推进堆里。
* **好处**：堆的大小永远只有 $K$，空间复杂度降到 $O(K)$，且不需要创建新节点。

想看看那个更省空间的“精简版”写法吗？