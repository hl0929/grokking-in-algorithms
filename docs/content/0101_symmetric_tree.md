
[101. Symmetric Tree](https://leetcode.cn/problems/symmetric-tree)

[0101_symmetric_tree](./html/0101_symmetric_tree.html ":include :type=iframe")

<a href="./content/html/0101_symmetric_tree.html" target="_blank">点击此处在新窗口打开</a>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def is_symmetric(root):
    queue = [(root.left, root.right)]
    while queue:
        left, right = queue.pop(0)
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
    return True
    
    
# root = [1,2,2,3,4,4,3] #true 
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
root.left = a
root.right = b
a.left = c
a.right = e
b.left = f
b.right = d
# root = [1,2,2,null,3,null,3] #false
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(3)
root.left = a
root.right = b
a.right = c
b.right = d
result = is_symmetric(root)
print(result)
```

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def is_symmetric(root):
    def _symmetric(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return _symmetric(left.left, right.right) and _symmetric(left.right, right.left)
    return _symmetric(root.left, root.right)
    
    
# root = [1,2,2,3,4,4,3] #true 
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
root.left = a
root.right = b
a.left = c
a.right = e
b.left = f
b.right = d
# root = [1,2,2,null,3,null,3] #false
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(3)
root.left = a
root.right = b
a.right = c
b.right = d
result = is_symmetric(root)
print(result)
```

这道题目（LeetCode 101. 对称二叉树）的核心思想是 **“双向镜像同步校验（Synchronous Mirror Validation）”**。

这不仅是二叉树的遍历，更像是在做一次 **“找茬游戏”**：我们同时观察左子树和右子树，看它们是否像照镜子一样完全吻合。

---

### 一、 核心思想：镜像的奥秘

要判断一棵树是否对称，不能只看它的值，要看它的结构：

1. **成对比较**：我们不再是遍历一个节点，而是每次从队列里取出一**对**节点（左树的一个，右树的一个）。
2. **内外对应**：
* 左树的**左**孩子，必须对应右树的**右**孩子（最外侧）。
* 左树的**右**孩子，必须对应右树的**左**孩子（最内侧）。


3. **同时坍缩**：只要任何一对节点不满足“镜像相等”，整个结论就瞬间坍缩为 `False`。

---

### 二、 算法逻辑：迭代的同步感

#### 1. 初始化“双哨兵”

* `queue = [(root.left, root.right)]`：我们将左、右子树的根节点作为第一对“待检选手”放入队列。

#### 2. 逻辑审判（While 循环）

每次弹出两个节点 `left` 和 `right`，进入三重判定：

* **判定一：双空即真**
* `if not left and not right: continue`
* 如果两边都是空的，说明这对位置是对称的，直接看下一对。


* **判定二：单空即假**
* `if not left or not right: return False`
* 如果一个有一份，另一个是空的，镜像破碎，直接返回 `False`。


* **判定三：数值对齐**
* `if left.val != right.val: return False`
* 值不一样，照镜子失败。



#### 3. 交叉入队（最精妙的一步）

* `queue.append((left.left, right.right))`：把最外侧的两个入队。
* `queue.append((left.right, right.left))`：把最内侧的两个入队。
* 这种成对入队的策略，保证了下一次循环弹出的依然是对应的镜像位置。

---

### 三、 过程模拟 (`[1, 2, 2, 3, 4, 4, 3]`)

1. **初始**：`queue = [(L2, R2)]`。
2. **第一轮**：
* 取出 `(L2, R2)`，值相等。
* 入队外侧：`(L3, R3)`，入队内侧：`(L4, R4)`。


3. **第二轮**：
* 取出 `(L3, R3)`，值都是 3，相等。入队它们的子节点（均为 None）。


4. **第三轮**：
* 取出 `(L4, R4)`，值都是 4，相等。


5. **结束**：队列清空，返回 `True`。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 我们需要遍历树中所有的节点对。


* **空间复杂度：$O(N)$**
* 在最坏情况下（完美二叉树），队列中存储的节点数与树的宽度成正比。



---

### 五、 总结金句

> **“这叫‘左顾右盼，内外兼修’。对称二叉树的迭代解法将单一的 BFS 转化为了双轴并行的同步检测。通过将镜像位置的节点成对存入队列，我们把一个复杂的结构对称问题简化为了连续的对等判定。这种‘成对入队、交叉匹配’的技巧，是处理所有‘镜像’或‘双树对比’问题的核心逻辑。”**

---

### 💡 深度思考

这段代码中 `queue.pop(0)` 在 Python 的 `list` 上是 $O(N)$ 的操作，如果追求极致性能，应该使用 `collections.deque` 来实现真正的 $O(1)$ 出队。但在面试时，这种逻辑的表达远比数据结构的选型更重要。

你觉得，这种**迭代法**和**递归法**（即 `check(p, q)`）相比，哪一个在理解“镜像”这个物理过程上更直观？
