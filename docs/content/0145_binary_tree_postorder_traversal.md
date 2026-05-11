
[0145. Binary Tree Postorder Traversal](https://leetcode.cn/problems/binary-tree-postorder-traversal)

[0145_binary_tree_postorder_traversal](./html/0145_binary_tree_postorder_traversal.html ":include :type=iframe")

<a href="./content/html/0145_binary_tree_postorder_traversal.html" target="_blank">点击此处在新窗口打开</a>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root):
    result = []
    def _postorder(root):
        if root:
            _postorder(root.left)
            _postorder(root.right)
            result.append(root.val)
    _postorder(root)
    return result


# root = [1,null,2,3] #[3,2,1]
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
root.right = a
a.left = b
result = postorder_traversal(root)
print(result)
```

这道题目（LeetCode 145. 二叉树的后序遍历）的核心思想是 **“子树优先与根节点的收尾工作（Subtree-First & Root Post-Processing）”**。

如果说前序遍历是“落地生根”，那么后序遍历就是“大后方清扫”。它是二叉树遍历中最具“责任感”的一种，因为只有当所有的孩子都安顿好了，根节点才最后现身。

---

### 一、 核心思想：深藏不露的压轴

在后序遍历中，我们严格执行 **“左 -> 右 -> 根”** 的准则：

1. **左翼深挖**：先彻底解决左子树的所有问题。
2. **右翼挺进**：再彻底解决右子树的所有问题。
3. **最后总结**：只有左、右两个战场都清理完毕，才记录当前根节点的值。

这种顺序在**销毁一棵树**或者**计算子树大小**时非常有用——你必须先处理掉子节点，才能处理父节点。

---

### 二、 算法逻辑：递归的“延迟满足”

#### 1. 递归函数 `_postorder(root)`

* 这依然是一个自相似的递归结构，但关键在于 `append` 动作的位置。
* **终止条件**：`if root:` 是所有递归的基准，确保我们不会对空气（None）进行操作。

#### 2. 三步走指令

* **左突围**：`_postorder(root.left)`。递归进入左深处。
* **右扫尾**：`_postorder(root.right)`。紧接着扫荡右深处。
* **记功碑**：`result.append(root.val)`。**压轴登场**。
* *注：这一行放在了最后，意味着当前的 `root` 必须等待它的左右子树递归全部返回后，才会被加入 `result`。*



---

### 三、 过程模拟 (`1 -> null -> 2 -> 3`)

1. **从 1 开始**：
* 先去 `1.left` (None) -> 直接返回。
* 再去 `1.right` (2) -> 进入节点 2 的递归。


2. **在 2 里面**：
* 先去 `2.left` (3) -> 进入节点 3 的递归。


3. **在 3 里面**：
* 先看左 (None)，再看右 (None)，都没了。
* **终于**记录 `3`。`result = [3]`。


4. **回到 2**：
* 左边（3）搞定了，右边是 None。
* **终于**记录 `2`。`result = [3, 2]`。


5. **回到 1**：
* 左边是 None，右边（2）搞定了。
* **最后**记录 `1`。`result = [3, 2, 1]`。



---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 每个节点都被“路过”三次（左、右、根），但只会被记录一次。


* **空间复杂度：$O(H)$**
* 取决于递归调用栈的深度。在最坏的链表结构中，深度为 $N$。



---

### 五、 总结金句

> **“这叫‘蓄势待发，完美收官’。后序遍历的精髓在于它的‘滞后性’：它是所有遍历中最后才处理根节点的。这种‘先解决子问题，再汇总父问题’的特质，使其天然适合处理需要依赖子树结果的场景（如计算树的高度、判断平衡树等）。在递归的精密循环中，每一个根节点都扮演了‘守门员’的角色，确保在它入队之前，脚下的世界已经井然有序。”**

---

### 💡 深度思考

后序遍历的迭代法（非递归）通常被认为是三种遍历中最难写的，因为你需要判断是从左子树回溯回来的，还是从右子树回溯回来的。但有一个“偷懒”的技巧：先写一个“根 -> 右 -> 左”的遍历，然后把结果 **反转（Reverse）** 一下。你觉得这种“镜像前序再反转”的思路，在逻辑上严谨吗？