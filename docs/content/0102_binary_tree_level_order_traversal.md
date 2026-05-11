
[102. Binary Tree Level Order Traversal](https://leetcode.cn/problems/binary-tree-level-order-traversal)

[0102_binary_tree_level_order_traversal](./html/0102_binary_tree_level_order_traversal.html ":include :type=iframe")

<a href="./content/html/0102_binary_tree_level_order_traversal.html" target="_blank">点击此处在新窗口打开</a>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_traversal(root):
    result = []
    queue = [root]
    while queue:
        part = []
        level_queue = []
        for node in queue:
            part.append(node.val)
            if node.left:
                level_queue.append(node.left)
            if node.right:
                level_queue.append(node.right)
        result.append(part)
        queue = level_queue
    return result


# root = [3,9,20,null,null,15,7] # [[3],[9,20],[15,7]]
root = TreeNode(3)
a = TreeNode(9)
b = TreeNode(20)
c = TreeNode(15)
d = TreeNode(7)
root.left = a
root.right = b
b.left = c
b.right = d
result = level_traversal(root)
print(result)
```

这道题目（LeetCode 102. 二叉树的层序遍历）的核心思想是 **“分层剥离与快照捕获（Layered Decoupling & Level Snapshot）”**。

这不仅仅是让每一个节点出队，而是要求我们在处理过程中，清晰地划分出**每一层**的边界。如果说普通的广度优先搜索（BFS）是一股脑流出的洪水，那这段代码就是将洪水精确地装进了不同的“集装箱”。

---

### 一、 核心思想：阵列式推进

在标准的 BFS 中，队列只是一个扁平的序列。而在这段代码中，我们引入了“层”的概念：

1. **逐层打包**：在每一轮循环开始时，队列里存放的正巧是**且仅是**当前这一层的所有节点。
2. **快照处理**：通过一个内层的 `for node in queue` 循环，我们在这一层节点消失之前，把它们的值全部提取出来，并把它们的后代预存到下一层。
3. **代际交替**：每一层都完成自己的使命后，将 `level_queue` 移交给 `queue`，开启下一轮的生长。

---

### 二、 算法逻辑：双重循环的节律

#### 1. 外部驱动 `while queue`

* 这是生命周期的主循环。只要队列里还有“种子”（节点），就继续向深处探索。

#### 2. 内部快照 `for node in queue`

* 这是代码最精妙的地方。在进入这个 `for` 循环的一瞬间，`queue` 的长度是固定的，它代表了**当前层的所有成员**。
* **提取价值**：`part.append(node.val)` 将当前层的结果汇总。
* **孕育未来**：将左右子节点放入 `level_queue`，但这不会干扰到正在进行的当前层遍历。

#### 3. 结果入库

* `result.append(part)`：每一层处理完，就像拍了一张合照，存入最终的大名单中。

---

### 三、 过程模拟 (`root = [3, 9, 20, 15, 7]`)

1. **初始状态**：`queue = [3]`, `result = []`。
2. **第一轮（第一层）**：
* 遍历 `queue` 中的 `3`。`part = [3]`。
* `3` 的孩子 `9, 20` 进入 `level_queue`。
* `result = [[3]]`, `queue = [9, 20]`。


3. **第二轮（第二层）**：
* 遍历 `queue` 中的 `9` 和 `20`。`part = [9, 20]`。
* `9` 无子节点；`20` 的孩子 `15, 7` 进入 `level_queue`。
* `result = [[3], [9, 20]]`, `queue = [15, 7]`。


4. **第三轮（第三层）**：
* 遍历 `15` 和 `7`。`part = [15, 7]`。
* 无新子节点进入。
* `result = [[3], [9, 20], [15, 7]]`, `queue = []`。


5. **结束**：队列为空，大功告成。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 每个节点被触碰且放入对应“集装箱”的过程都是一次性的。


* **空间复杂度：$O(N)$**
* 除了存储结果外，队列在最坏情况下（完全二叉树的底层）需要存储 $N/2$ 个节点。



---

### 五、 总结金句

> **“这叫‘层层递进，界限分明’。层序遍历的精髓不在于‘遍历’，而在于‘节奏感’。通过双重循环的设计，我们给原本混沌的 BFS 加入了时间上的刻度，使得每一层节点都能在属于自己的时刻被集体捕获。这种按层处理的模式，是解决所有‘树上最短路径’或‘空间分层设计’问题的标准答案。”**

---

### 💡 深度思考

这段代码中，我们手动创建了一个 `level_queue` 来存储下一层。其实，还有一种更省空间的写法：只用一个 `queue`，但在 `for` 循环前先记录下 `size = len(queue)`。你觉得这种“先记长度再循环”的做法，在逻辑表达上和现在的“双队列交换”相比，哪种更不容易让你在面试时写出 Bug？