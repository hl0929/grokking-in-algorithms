
[144. Binary Tree Preorder Traversal](https://leetcode.cn/problems/binary-tree-preorder-traversal)

[0144_binary_tree_preorder_traversal](./html/0144_binary_tree_preorder_traversal.html ":include :type=iframe")

<a href="./content/html/0144_binary_tree_preorder_traversal.html" target="_blank">点击此处在新窗口打开</a>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    result = []
    def _preorder(root):
        if root:
            result.append(root.val)
            _preorder(root.left)
            _preorder(root.right)
    _preorder(root)
    return result


# root = [1,null,2,3] #[1,2,3]
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
root.right = a
a.left = b
result = preorder_traversal(root)
print(result)
```

这道题目（LeetCode 144. 二叉树的前序遍历）的核心思想是 **“根节点优先与递归式深度探索（Root-First & Recursive Depth Discovery）”**。

前序遍历是二叉树最符合直觉的访问方式，它像是一场“先落脚、再探险”的旅程。

---

### 一、 核心思想：先声夺人的访问秩序

在前序遍历中，我们严格遵守 **“根 -> 左 -> 右”** 的指令：

1. **首位确认**：每当你进入一个新领地，第一件事就是把当前的“领主”（根节点）记在名单上。
2. **左翼突围**：只要左边还有路，就优先彻底扫描完左侧的所有分支。
3. **右翼扫尾**：当左边所有可能性都穷尽后，才回过头来处理右侧的领地。

这种顺序保证了每一个子树的“根”都是在该子树中第一个被访问的。

---

### 二、 算法逻辑：套娃式的自我复制

#### 1. 递归函数 `_preorder(root)`

* 这是一个典型的**自相似**逻辑：处理整棵树的方法，和处理其中任何一个分叉的方法完全一样。
* **终止条件**：`if root:`。这是递归的护身符。如果节点不存在（走到了虚无的边界），就直接返回，防止程序崩溃。

#### 2. 三步走指令

* **记录**：`result.append(root.val)`。落地即生效。
* **左递归**：`_preorder(root.left)`。在处理右边之前，先潜入左子树的深渊。
* **右递归**：`_preorder(root.right)`。等左边全部“大白于天下”后，再开始右边的探索。

---

### 三、 过程模拟 (`1 -> null -> 2 -> 3`)

1. **访问 1**：
* 记录 `1`。`result = [1]`。
* 探测 `1.left` (None) -> 直接返回。
* 探测 `1.right` (2) -> 进入节点 2 的递归。


2. **访问 2**：
* 记录 `2`。`result = [1, 2]`。
* 探测 `2.left` (3) -> 进入节点 3 的递归。
* 探测 `2.right` (None)。


3. **访问 3**：
* 记录 `3`。`result = [1, 2, 3]`。
* 探测其左右，均为 None，返回。


4. **回溯结束**：所有函数调用栈清空，返回 `[1, 2, 3]`。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 每个节点都必须且仅会被递归函数访问一次。


* **空间复杂度：$O(H)$**
* 虽然没有显式使用队列，但系统**隐式栈**的大小取决于树的高度 $H$。在最坏的“长蛇阵”树中，复杂度为 $O(N)$。



---

### 五、 总结金句

> **“这叫‘步步为营，根基为先’。前序遍历的魅力在于它的确定性：根节点永远是它所在序列的领头羊。通过递归的自我召唤，我们将复杂的树形结构解构成了一串线性的名单。这种‘先记录、再深挖’的思维，不仅是遍历的基石，更是构建二叉树镜像、拷贝或序列化操作的逻辑起点。”**

---

### 💡 深度思考

递归法写起来爽快，但如果这棵树深达几万层，系统栈就会发生“爆仓”（Stack Overflow）。如果让你把这个递归改成**迭代（用 while 和 stack）**，为了保证“左”比“右”先出来，你应该先往栈里压入左孩子还是右孩子？（提示：栈是后进先出的！）

