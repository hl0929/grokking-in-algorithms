
[226. Invert Binary Tree](https://leetcode.cn/problems/invert-binary-tree)

[0226_invert_binary_tree](./html/0226_invert_binary_tree.html ":include :type=iframe")

<a href="./content/html/0226_invert_binary_tree.html" target="_blank">点击此处在新窗口打开</a>

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
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
        
        
def invert_tree(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        node.left, node.right = node.right, node.left
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root
    
    
# root = [4,2,7,1,3,6,9] # [4,7,2,9,6,3,1]
root = TreeNode(4)
a = TreeNode(2)
b = TreeNode(7)
c = TreeNode(1)
d = TreeNode(3)
e = TreeNode(6)
f = TreeNode(9)
root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
result = invert_tree(root)
print(level_traversal(result))
```

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
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
        
        
def invert_tree(root):
    def _invert(root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        _invert(root.left)
        _invert(root.right)
        return root
    return _invert(root)
    
    
# root = [4,2,7,1,3,6,9] # [4,7,2,9,6,3,1]
root = TreeNode(4)
a = TreeNode(2)
b = TreeNode(7)
c = TreeNode(1)
d = TreeNode(3)
e = TreeNode(6)
f = TreeNode(9)
root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
result = invert_tree(root)
print(level_traversal(result))
```

这道题目（LeetCode 226. 翻转二叉树）的核心思想是 **“全域镜像置换与广度优先扫描（Universal Mirror Swap & BFS）”**。

这题在算法界名气极大（源于 Homebrew 作者的梗），但回归本质，它就是一场 **“从上到下、由内而外”的左右大调换**。

---

### 一、 核心思想：左右互搏的递归美学

翻转一棵树，就像是在镜子里看它。

1. **局部反转**：对于每一个节点，我们不管它的子树有多深，先把它眼前的两个“孩子”（左儿子和右儿子）交换位置。
2. **全局覆盖**：只要我们确保每一个节点都执行了“交换孩子”的操作，整棵树自然就完成了镜像翻转。
3. **迭代推进**：这段代码巧妙地使用了 **BFS（广度优先搜索）**。它不急着深钻，而是像洪水淹没大地一样，扫过一层，翻转一层。

---

### 二、 算法逻辑：排队换位

#### 1. 启动队列

* `queue = [root]`：我们把根节点作为第一个“待手术对象”放进队列。

#### 2. 交换手术（While 循环）

只要队列里还有节点，就说明翻转任务还没完成：

* **出队就诊**：`node = queue.pop(0)`，取出当前要处理的节点。
* **左右互换**：`node.left, node.right = node.right, node.left`。
* **这是灵魂一行**：它不管左边是森林还是荒漠，直接把左指针和右指针指向的对象调换。


* **衍生后续**：
* 如果换完后左边有孩子，入队。
* 如果换完后右边有孩子，入队。
* 这样可以保证这些孩子节点在未来的循环中也会被抓出来“交换它们自己的孩子”。



---

### 三、 过程模拟 (`root = [4, 2, 7]`)

1. **初始**：`queue = [4]`。
2. **第一轮**：
* 弹出 `4`。交换 `4` 的左右。现在 `4.left = 7`, `4.right = 2`。
* 把 `7` 和 `2` 塞进队列。`queue = [7, 2]`。


3. **第二轮**：
* 弹出 `7`。交换 `7` 的左右孩子（如果有的话），并将孩子入队。


4. **第三轮**：
* 弹出 `2`。交换 `2` 的左右孩子（如果有的话），并将孩子入队。


5. **结束**：所有节点都经历过交换，返回根节点。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 每个节点都被访问且交换了一次指针，工作量与节点总数成正比。


* **空间复杂度：$O(W)$**
* $W$ 是树的最大宽度。队列中最多同时存放一层的所有节点。



---

### 五、 总结金句

> **“这叫‘翻转乾坤，逐层镜像’。翻转二叉树的精髓在于：你不需要一次性看透整棵树的未来，只需要处理好眼下的左右逻辑。通过一个队列的吞吐，我们将这种简单的局部交换传播到了每一个节点。这种‘先换指针，后进队列’的迭代思维，让复杂的树形结构变换退化成了简单的线性扫描。记住，只要每一个局部的世界都颠倒了，整个宇宙也就翻转了。”**

---

### 💡 深度思考

这段代码用的是 **BFS（层序遍历）** 来翻转。其实，用 **DFS（前序或后序遍历）** 递归实现起来会更简洁（只需 3 行）。你觉得，在翻转二叉树这件事上，是这种“层层推进”的逻辑更符合直觉，还是那种“子问题递归”的逻辑更优雅？