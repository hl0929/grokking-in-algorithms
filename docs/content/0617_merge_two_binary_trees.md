
[617. Merge Two Binary Trees](https://leetcode.cn/problems/merge-two-binary-trees)

[0617_merge_two_binary_trees](./html/0617_merge_two_binary_trees.html ":include :type=iframe")

<a href="./content/html/0617_merge_two_binary_trees.html" target="_blank">点击此处在新窗口打开</a>

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

        
def merge_trees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    queue = [(root1, root2)]
    while queue:
        node1, node2 = queue.pop(0)
        node1.val += node2.val
        # left 
        if node1.left and node2.left:
            queue.append((node1.left, node2.left))
        elif not node1.left:
            node1.left = node2.left
        # right
        if node1.right and node2.right:
            queue.append((node1.right, node2.right))
        elif not node1.right:
            node1.right = node2.right
    return root1
    
    
# root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] #[3,4,5,5,4,null,7]
root1 = TreeNode(1)
a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(5)
root1.left = a
root1.right = b
a.left = c
root2 = TreeNode(2)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(4)
g = TreeNode(7)
root2.left = d
root2.right = e
d.right = f
e.right = g
result = merge_trees(root1, root2)
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

        
def merge_trees(root1, root2):
    def _merge(root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = _merge(root1.left, root2.left)
        root1.right = _merge(root1.right, root2.right)
        return root1
    return _merge(root1, root2)
    
    
# root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] #[3,4,5,5,4,null,7]
root1 = TreeNode(1)
a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(5)
root1.left = a
root1.right = b
a.left = c
root2 = TreeNode(2)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(4)
g = TreeNode(7)
root2.left = d
root2.right = e
d.right = f
e.right = g
result = merge_trees(root1, root2)
print(level_traversal(result))
```

这道题目（LeetCode 617. 合并二叉树）的核心思想是 **“双树并行的叠加与嫁接（Parallel Overlap & Grafting）”**。

这题就像是将两张半透明的幻灯片重叠在一起：重合的部分数值相加，不重合的部分则直接继承。

---

### 一、 核心思想：结构上的“取长补短”

当两棵树重叠时，会发生三种情况：

1. **强强联手**：两个对应位置都有节点。此时数值进行叠加。
2. **单向继承**：一棵树有节点，另一棵没有。我们直接把有节点的那部分“嫁接”过来，之后那条分支下的所有子孙都不再需要遍历。
3. **双空即空**：两边都没有，那自然是一片虚无。

在这段代码中，我们采用 **BFS（广度优先搜索）** 的迭代方式，以 `root1` 为基准阵地，把 `root2` 的精华吸收进来。

---

### 二、 算法逻辑：同步扫描与按需挂载

#### 1. 先遣特判

* `if not root1: return root2`：如果第一棵树是空的，直接把第二棵树拿走。
* `if not root2: return root1`：同理，第二棵空了，就直接用第一棵。

#### 2. 初始化协同队列

* `queue = [(root1, root2)]`：队列里存的是一对一对的节点。我们保证进入队列的两个节点一定都不是 `None`。

#### 3. 循环内的“吞噬”逻辑

* **数值叠加**：`node1.val += node2.val`。既然两边都有，就把 `node2` 的力量借给 `node1`。
* **左子树的博弈**：
* **都有左孩子**：竞争激烈，双双入队，等待下一轮合并。
* **只有 `root2` 有**：`node1` 认输，直接通过 `node1.left = node2.left` 把对方的分支“整体搬运”过来。从此以后，这条线上的合并就结束了。


* **右子树的博弈**：
* 逻辑同上。如果 `node1` 缺右孩子，直接把 `node2.right` 挂上去。



---

### 三、 过程模拟 (`root1=[1,3,2], root2=[2,1,3]`)

1. **初始**：`queue = [(R1, R2)]`。
2. **第一轮**：
* 弹出根节点 `(1, 2)`。`R1.val` 变为 $1+2=3$。
* 左右都有，入队：`[(L1, L1'), (R1, R1')]`（假设 $L$ 为左，$R$ 为右）。


3. **第二轮**：
* 弹出左边一对 `(3, 1)`。值变为 4。
* 检查它们的子节点。如果 `node1` 某个方向为空，就把 `node2` 对应的整个子树直接指过去。


4. **结束**：所有重合的部分都加好了，不重合的部分也接好了，返回 `root1`。

---

### 四、 复杂度分析

* **时间复杂度：$O(\min(N, M))$**
* $N$ 和 $M$ 分别是两棵树的节点数。我们只遍历两棵树重叠的部分。一旦遇到“嫁接”情况，剩下的节点就无需再进队列。


* **空间复杂度：$O(\min(N, M))$**
* 队列的长度取决于重叠部分的最大宽度。



---

### 五、 总结金句

> **“这叫‘合二为一，借力打力’。合并二叉树的精髓在于以一棵树为蓝本进行的原地改造。通过迭代的同步队列，我们不仅处理了重叠节点的数值融合，更利用了链表式结构的特性，通过‘嫁接’指针实现了对非重叠子树的整块吸收。这种‘能省则省’的逻辑，让算法在处理大规模结构差异时依然能保持极高的效率。”**

---

### 💡 深度思考

这段代码中，一旦执行了 `node1.left = node2.left`，就不再把这对节点放入队列了。你觉得这种“整体挂载”会不会漏掉 `node2.left` 内部原本需要相加的逻辑？（提示：仔细看判断条件，只有在 `node1.left` 彻底缺失时才执行挂载，这意味着原本那里是一片空白，根本不存在“相加”的可能！）