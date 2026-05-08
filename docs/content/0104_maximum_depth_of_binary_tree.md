
[104. Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

[0104_maximum_depth_of_binary_tree](./html/0104_maximum_depth_of_binary_tree.html ":include :type=iframe")

<a href="./content/html/0104_maximum_depth_of_binary_tree.html" target="_blank">点击此处在新窗口打开</a>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def max_depth(root):
    if not root:
        return 0
    queue = [root]
    depth = 0
    while queue:
        depth += 1
        next_level = []
        for node in queue:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level
    return depth


# root = [3,9,20,null,null,15,7] #3
root = TreeNode(3)
a = TreeNode(9)
b = TreeNode(20)
c = TreeNode(15)
d = TreeNode(7)
root.left = a
root.right = b
b.left = c
b.right = d
result = max_depth(root)
print(result)
```

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def max_depth(root):
    def _depth(root):
        if not root:
            return 0
        left = _depth(root.left)
        right = _depth(root.right)
        return max(left, right) + 1
    return _depth(root)


# root = [3,9,20,null,null,15,7] #3
root = TreeNode(3)
a = TreeNode(9)
b = TreeNode(20)
c = TreeNode(15)
d = TreeNode(7)
root.left = a
root.right = b
b.left = c
b.right = d
result = max_depth(root)
print(result)
```

这道题目（LeetCode 104. 二叉树的最大深度）的核心思想是 **“层序遍历与波动扫描（Level-Order Traversal & Breadth-First Search）”**。

虽然求深度最常见的写法是递归（DFS），但这段代码选择了一种更具“颗粒感”的方式：**广度优先搜索（BFS）**。它不急着扎进地心，而是一层一层地“扫荡”。

---

### 一、 核心思想：剥洋葱式的探索

想象二叉树是一个洋葱，根节点是芯，叶子节点是外皮：

1. **按层计数**：我们每完整地处理完“一整层”节点，深度计数器就 `+1`。
2. **队列存储**：我们用一个容器（`queue`）记住当前这一层的所有成员。
3. **衍生下一代**：在处理当前层的同时，把它们所有的子节点（下一层）收集起来，准备下一轮的扫描。

---

### 二、 算法逻辑：波纹式扩张

#### 1. 边界守护

* `if not root: return 0`：空树没有深度，这是逻辑的起点。

#### 2. 初始化“先遣队”

* `queue = [root]`：初始时，第一层只有根节点自己。
* `depth = 0`：从零开始，准备计数。

#### 3. 逐层击破（While 循环）

* 只要 `queue` 不为空，说明还有下一层可以“卷”。
* **深度递增**：`depth += 1`。只要进入循环，就意味着当前这一层是存在的。
* **新旧交替**：
* 代码创建了一个 `next_level` 列表。
* 通过 `for node in queue` 遍历当前层的所有节点，把它们的左右孩子统统塞进 `next_level`。
* 最后 `queue = next_level`，完成“换届”。



---

### 三、 过程模拟 (`3 -> [9, 20] -> [15, 7]`)

1. **初始**：`queue = [3]`, `depth = 0`。
2. **第一轮**：
* `depth = 1`。
* 处理节点 `3`，其子节点 `9` 和 `20` 入队。
* `queue` 变为 `[9, 20]`。


3. **第二轮**：
* `depth = 2`。
* 处理 `9`（无子节点），处理 `20`（子节点 `15` 和 `7` 入队）。
* `queue` 变为 `[15, 7]`。


4. **第三轮**：
* `depth = 3`。
* 处理 `15` 和 `7`，均无子节点。
* `queue` 变为空。


5. **结束**：返回 `3`。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 每个节点都恰好入队一次、出队一次，没有任何废动作。


* **空间复杂度：$O(W)$**
* $W$ 是树的最大宽度（即节点最多的一层）。在完全二叉树中，最底层大约有 $N/2$ 个节点，所以空间复杂度最坏也是 $O(N)$。



---

### 五、 总结金句

> **“这叫‘步步为营，层层递进’。BFS 解法将抽象的树高转化为了具体的‘迭代次数’。它不像 DFS 那样孤军深入、依赖回溯，而是像水面散开的波纹，稳扎稳打地覆盖每一个角落。这种层层换届的思路，不仅能算出最大深度，更是解决‘二叉树右视图’或‘每一层平均值’等层级问题的万能模板。”**

---

### 💡 深度思考

递归解法（DFS）通常只需要一行代码 `return max(max_depth(root.left), max_depth(root.right)) + 1`。相比之下，这种 BFS 写法虽然长了一点，但它在处理**极深、极不平衡**的树时，能有效避免“栈溢出”的风险。你觉得在面试中，是追求代码的极致简洁（递归），还是追求运行时的极致稳健（迭代）更有优势？