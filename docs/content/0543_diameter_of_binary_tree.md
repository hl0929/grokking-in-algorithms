
[543. Diameter of Binary Tree](https://leetcode.cn/problems/diameter-of-binary-tree)

[0543_diameter_of_binary_tree](./html/0543_diameter_of_binary_tree.html ":include :type=iframe")

<a href="./content/html/0543_diameter_of_binary_tree.html" target="_blank">点击此处在新窗口打开</a>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def diameter_of_tree(root):
    result = [0]
    def _diameter(root):
        if not root:
            return 0
        left = _diameter(root.left)   # 左子树的高度
        right = _diameter(root.right) # 右子树的高度
        diameter = left + right
        result[0] = max(result[0], diameter)
        return max(left, right) + 1
    _diameter(root)
    return result[0]
    
    
# root = [1,2,3,4,5] #3
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
root.left = a
root.right = b
a.left = c
a.right = d
result = diameter_of_tree(root)
print(result)
```

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def diameter_of_tree(root):
    if not root:
        return 0
    stack = [(root, False)]
    depth_map = {}
    result = 0
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if not visited:
            stack.append((node, True))
            # 栈是LIFO，为了先处理左子树，需要先压右再压左
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
        else:
            left_height = depth_map.get(node.left, 0)
            right_height = depth_map.get(node.right, 0)
            result = max(result, left_height + right_height)
            depth_map[node] = max(left_height, right_height) + 1
    return result
    
    
# root = [1,2,3,4,5] #3
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
root.left = a
root.right = b
a.left = c
a.right = d
result = diameter_of_tree(root)
print(result)
```

这道题目（LeetCode 543. 二叉树的直径）的核心思想是 **“穿针引线与自底向上的高度贡献（Bottom-up Depth & Global Path Tracking）”**。

它是二叉树题目中非常经典的一种模式：**“借着求高度的东风，顺便把直径给算了。”**

---

### 一、 核心思想：寻找“最长的弯道”

二叉树的直径，定义为树中任意两个节点之间路径长度的最大值。

1. **直径的构成**：对于任何一个节点，经过它的最长路径长度 = **左子树的高度 + 右子树的高度**。
2. **未必过根节点**：最长的路径可能完全隐藏在某一侧的子树里（比如左子树非常茂盛，而右子树很矮）。
3. **顺风车策略**：我们不需要专门写一个求直径的函数。在递归计算每个节点高度（Depth）的过程中，我们顺手把“左高 + 右高”算出来，并去挑战全局最大值。

---

### 二、 算法逻辑：双重使命的递归

#### 1. 外部变量 `result = [0]`

* 这是一个“全局记录仪”（用列表是为了在递归内部修改它）。它不关心递归到了哪一层，只负责记录历史上出现过的最大直径。

#### 2. 递归函数 `_diameter(root)` 的双重身份

这个函数在每一次调用时，其实都在做两件事：

* **对内（局部计算）**：计算经过当前节点的路径长度 `left + right`，并更新 `result[0]`。
* **对外（返回贡献）**：返回当前子树对父节点能贡献的最大高度 `max(left, right) + 1`。

#### 3. “后序”思维

* 必须先拿到左边的结果，再拿到右边的结果，最后才能在当前节点做决策。这是一种典型的自底向上（Bottom-up）处理方式。

---

### 三、 过程模拟 (`1 -> [2, 3], 2 -> [4, 5]`)

1. **触底**：递归一直深入到叶子节点 `4` 和 `5`。
2. **处理节点 4 & 5**：
* 左右孩子皆空，高度返回 `1`。
* 此时它们的直径贡献都是 `0+0 = 0`。


3. **处理节点 2**：
* 接收到左边（4）高度为 1，右边（5）高度为 1。
* **更新全局直径**：`result[0] = max(0, 1 + 1) = 2`。
* **返回高度给父节点**：`max(1, 1) + 1 = 2`。


4. **处理节点 1**：
* 接收到左边（2）高度为 2，右边（3）高度为 1。
* **更新全局直径**：`result[0] = max(2, 2 + 1) = 3`。
* **返回高度**：`max(2, 1) + 1 = 3`。


5. **最终结果**：`result[0]` 锁定为 3。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 每个节点只被访问一次，就像一次完美的深搜旅行。


* **空间复杂度：$O(H)$**
* $H$ 为树的高度。这是递归时系统栈占用的空间。在最差的“斜树”情况下，$H$ 等于 $N$。



---

### 五、 总结金句

> **“这叫‘醉翁之意不在酒’。表面上我们在勤勤恳恳地计算每一棵子树的高度，实际上我们心怀鬼胎，时刻在寻找那个能让‘左高+右高’达到巅峰的转折点。这种在递归返回值之外，利用外部变量捕捉全局最优解的套路，是解决所有‘树上路径’问题的金钥匙。”**

---

### 💡 深度思考

在这个代码里，我们定义直径为**路径中边的数量**（即 `left + right`）。如果面试官突然改口，定义直径为**路径中节点的数量**，你觉得代码里哪一行需要微调？（提示：只需要在 `result[0]` 的更新逻辑里多加一个 1 吗？）

