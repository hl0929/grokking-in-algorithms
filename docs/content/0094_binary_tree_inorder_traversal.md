
[94. Binary Tree Inorder Traversal](https://leetcode.cn/problems/binary-tree-inorder-traversal)

[0094_binary_tree_inorder_traversal](./html/0094_binary_tree_inorder_traversal.html ":include :type=iframe")

<a href="./content/html/0094_binary_tree_inorder_traversal.html" target="_blank">点击此处在新窗口打开</a>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def inorder_traversal(root):
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result


root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
root.right = a
a.left = b
result = inorder_traversal(root)
print(result)
```

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def inorder_traversal(root):
    result = []
    def _inorder(root):
        if root:
            _inorder(root.left)
            result.append(root.val)
            _inorder(root.right)
    _inorder(root)
    return result


root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
root.right = a
a.left = b
result = inorder_traversal(root)
print(result)
```


这道题目（LeetCode 94. 二叉树的中序遍历）的核心思想是 **“显式栈模拟与左偏深度探索（Explicit Stack Simulation & Left-First Exploration）”**。

如果说递归遍历是利用系统的“隐身栈”自动回溯，那么这段代码就是通过手动维护一个 `stack`，将二叉树的深度优先搜索（DFS）拆解成了清晰的“进、出、转”三个动作。

---

### 一、 核心思想：左、根、右的“三部曲”

中序遍历的逻辑是：先遍历左子树，再访问根节点，最后遍历右子树。

1. **一路向左**：只要当前节点有左孩子，就不能急着访问它，而是要把它“压入箱底”（栈），去寻找更左边的可能。
2. **触底反弹**：当左边走到尽头（`curr` 为空），我们就从栈里弹出最近的一个节点。这个节点就是当前最左的“根”。
3. **折向右方**：访问完根节点后，剩下的任务就是去处理它的右子树。

---

### 二、 算法逻辑：双层循环的艺术

#### 1. 变量分工

* `stack`：手动维护的栈，用来记住“回家的路”。
* `curr`：当前的探测指针，它像一个侦察兵，始终冲在最前面。

#### 2. 外层循环 `while curr or stack`

* 这是整个引擎的动力。只要 `curr` 还没走完，或者栈里还有节点没处理，任务就没结束。

#### 3. 内层循环 `while curr`（一路向左）

* 这是最执着的搜索。它会把当前节点及其所有的左代节点全部入栈。
* **关键点**：入栈顺序是父节点先入，子节点后入。

#### 4. 弹出与转向

* `curr = stack.pop()`：当左边没路了，弹出栈顶。此时弹出的节点是目前最左的，直接存入 `result`。
* `curr = curr.right`：转向右子树。如果右子树存在，它会在下一轮循环中再次尝试“一路向左”；如果不存在，下一轮循环会直接继续弹栈。

---

### 三、 过程模拟 (`1 -> null -> 2 -> 3`)

1. **初始**：`curr = 1`, `stack = []`。
2. **一路向左**：`1` 入栈，`curr` 移向 `1.left` (None)。
3. **弹出转向**：
* 弹 `1`。`result = [1]`。
* 转向 `1.right`，即 `curr = 2`。


4. **一路向左**：
* `2` 入栈。
* `2.left` 是 `3`，`3` 入栈。
* `curr` 移向 `3.left` (None)。


5. **弹出转向**：
* 弹 `3`。`result = [1, 3]`。转向 `3.right` (None)。
* 弹 `2`。`result = [1, 3, 2]`。转向 `2.right` (None)。


6. **结束**：`curr` 为空且栈为空。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 每个节点都会入栈一次、出栈一次，且访问一次。


* **空间复杂度：$O(H)$**
* $H$ 是树的高度。栈中最多存储从根到最深叶子节点的路径。最坏情况下（树退化成链表），空间复杂度为 $O(N)$。



---

### 五、 总结金句

> **“这叫‘身先士卒，底蕴深厚’。迭代法的中序遍历通过一个显式栈，完美还原了递归的‘回溯’本质。内层循环展现了算法对‘左’的极致追求，而外层循环则掌控着全局的‘进退’。这种将抽象的递归过程物理化为栈操作的思路，不仅避开了栈溢出的风险，更让我们看清了二叉树遍历在内存中真实的舞步。”**

---

### 💡 深度思考

这道题还有一种更牛的 **莫里斯遍历（Morris Traversal）**。它利用叶子节点的空指针指向中序后继，从而将空间复杂度降到惊人的 **$O(1)$**。你觉得，在面试中，是这种稳健的栈迭代法更容易打动面试官，还是那种“破坏树结构再恢复”的莫里斯法更具杀伤力？
