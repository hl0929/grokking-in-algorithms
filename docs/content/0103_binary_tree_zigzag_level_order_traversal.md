
[103. Binary Tree Zigzag Level Order Traversal](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal)

[0103_binary_tree_zigzag_level_order_traversal](./html/0103_binary_tree_zigzag_level_order_traversal.html ":include :type=iframe")

<a href="./content/html/0103_binary_tree_zigzag_level_order_traversal.html" target="_blank">点击此处在新窗口打开</a>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_traversal(root):
    result = []
    queue = [root]
    level = 0
    while queue:
        part = []
        level_queue = []
        for node in queue:
            part.append(node.val)
            if node.left:
                level_queue.append(node.left)
            if node.right:
                level_queue.append(node.right)
        if level % 2:
            part.reverse()
        level += 1
        result.append(part)
        queue = level_queue
    return result


# root = [3,9,20,null,null,15,7] # [[3],[20,9],[15,7]]
root = TreeNode(3)
a = TreeNode(9)
b = TreeNode(20)
c = TreeNode(15)
d = TreeNode(7)
root.left = a
root.right = b
b.left = c
b.right = d
result = zigzag_level_traversal(root)
print(result)
```

这道题目（LeetCode 103. 二叉树的锯齿形层序遍历）的核心思想是 **“分层捕获与定向反转（Level-wise Capture & Directional Reversal）”**。

如果说标准的层序遍历是稳步前进的“阅兵式”，那么锯齿形遍历就是灵动的“之字形舞步”。它在保留了层级秩序的基础上，为每一层注入了不断变换的方向感。

---

### 一、 核心思想：秩序中的叛逆

在普通的层序遍历中，我们始终坚持从左往右。但在锯齿形遍历里：

1. **奇偶定序**：我们给每一层编号（从 0 开始）。偶数层维持现状（从左往右），奇数层则反其道而行之（从右往左）。
2. **先拓扑再镜像**：算法并没有在入队时就搞乱顺序，而是先老老实实地按层把节点收集好，然后在最后一步通过“镜像反转”来达到视觉上的之字形效果。
3. **钟摆效应**：随着 `level` 变量的自增，输出结果在“正序”与“倒序”之间来回摆动。

---

### 二、 算法逻辑：带标记的分层扫描

#### 1. 层级计数器 `level`

* 这是整个逻辑的“指挥棒”。它不参与节点的生长，只决定当前这一层结果（`part`）在存入最终大名单之前，是否需要执行一次 `reverse()`。

#### 2. 标准的层序底座

* 代码使用了双重循环结构（`while queue` + `for node in queue`）。
* 这保证了我们在每一轮处理中，拿到的都是整整齐齐的一层节点。无论我们要怎么反转结果，**下一层的生长顺序（先左后右入队）始终保持不变**。

#### 3. 结果的“后期处理”

* `if level % 2: part.reverse()`：这就是魔法发生的地方。
* 第 0 层（偶数）：不反转 -> `[3]`
* 第 1 层（奇数）：反转 -> `[9, 20]` 变成 `[20, 9]`
* 第 2 层（偶数）：不反转 -> `[15, 7]`



---

### 三、 过程模拟 (`root = [3, 9, 20, 15, 7]`)

1. **第 0 层 (`level=0`)**：
* `queue = [3]`。
* 取出 `3`，`part = [3]`。
* 子节点 `9, 20` 入队。
* `level % 2` 为假，不反转。`result = [[3]]`。


2. **第 1 层 (`level=1`)**：
* `queue = [9, 20]`。
* 遍历提取，`part = [9, 20]`。
* 子节点 `15, 7` 入队。
* **关键时刻**：`level % 2` 为真，执行 `part.reverse()`。
* `part` 变为 `[20, 9]`。`result = [[3], [20, 9]]`。


3. **第 2 层 (`level=2`)**：
* `queue = [15, 7]`。
* 提取 `part = [15, 7]`。不反转。
* `result = [[3], [20, 9], [15, 7]]`。



---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 每个节点遍历一次。虽然 `reverse()` 也要花时间，但每层反转的总代价累加起来依然是 $O(N)$。


* **空间复杂度：$O(N)$**
* 队列和结果列表的空间消耗。



---

### 五、 总结金句

> **“这叫‘步法不变，视野互换’。锯齿形遍历的精妙之处在于它对‘变’与‘不变’的精准掌控：入队的逻辑永远是‘先左后右’，确保了结构的稳定；而输出的逻辑则通过‘奇反偶正’，实现了形态的灵动。这种在成熟模板（层序遍历）上进行轻量级后期加工的思路，是解决此类‘变体遍历’问题最高效、最不易出错的工业级写法。”**

---

### 💡 深度思考

这段代码通过 `part.reverse()` 进行后期处理。其实，我们也可以在收集 `part` 时使用 **双端队列（Deque）**，根据层数的奇偶决定是从“头部插入”还是“尾部插入”。你觉得这种“边收集边决定方向”的做法，与现在的“收集完再反转”相比，哪一种在处理超大规模数据时性能更优？
