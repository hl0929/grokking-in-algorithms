
[199. Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view)

[0199_binary_tree_right_side_view](./html/0199_binary_tree_right_side_view.html ":include :type=iframe")

<a href="./content/html/0199_binary_tree_right_side_view.html" target="_blank">点击此处在新窗口打开</a>

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
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
        result.append(part[-1])
        queue = level_queue
    return result


# rroot = [1,2,3,null,5,null,4] #[1,3,4]
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(5)
d = TreeNode(4)
root.left = a
root.right = b
a.right = c
b.right = d
result = right_side_view(root)
print(result)
```

这道题目（LeetCode 199. 二叉树的右视图）的核心思想是 **“层序抽样与侧缘捕获（Level-wise Sampling & Rightmost Edge Capture）”**。

这题就像是你在树的右侧放了一台相机，每一层只有最靠右的那个节点能被拍进镜头里。

---

### 一、 核心思想：每一层的“谢幕者”

右视图的逻辑建立在层序遍历（BFS）的基础之上：

1. **层级隔离**：我们必须准确知道每一层有哪些节点。
2. **末位选取**：在每一层的节点序列中，我们只关心最后出现的那个。
3. **视觉遮挡**：即使左子树再深，只要右子树在同一高度有节点，左边的就会被“挡住”；只有当右边空出来时，左边的末尾节点才会露面。

---

### 二、 算法逻辑：捕捉地平线的最后一道光

#### 1. 沿用分层模板

* 代码依然使用了经典的 `while queue` 加 `for node in queue` 的双重循环结构。
* 这种结构保证了 `part` 列表里存放的是当前这一层**从左到右**排列的所有节点值。

#### 2. 精确切片 `part[-1]`

* `result.append(part[-1])`：这是整段代码的灵魂。
* 既然 `part` 是按从左到右顺序收集的，那么索引 `-1` 对应的就是该层最右侧的节点。它是该层唯一有资格进入“右视图”名单的代表。

#### 3. 换代更新

* `queue = level_queue`：像接力赛一样，处理完这一层的“最右”，立刻投身于下一层的孕育中。

---

### 三、 过程模拟 (`1 -> [2, 3], 2 -> [null, 5], 3 -> [null, 4]`)

1. **第一层 (`level 0`)**：
* `queue = [1]`。
* `part = [1]`。
* **取末尾**：`1` 加入 `result`。
* `level_queue = [2, 3]`。


2. **第二层 (`level 1`)**：
* `queue = [2, 3]`。
* `part = [2, 3]`。
* **取末尾**：`3` 加入 `result`。
* `level_queue = [5, 4]`（2 产生 5，3 产生 4）。


3. **第三层 (`level 2`)**：
* `queue = [5, 4]`。
* `part = [5, 4]`。
* **取末尾**：`4` 加入 `result`。


4. **最终结果**：`[1, 3, 4]`。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
* 每个节点都要入队出队一次，尽管我们只取每层的一个，但为了找到它，必须遍历所有节点。


* **空间复杂度：$O(N)$**
* 最坏情况下（完全二叉树），队列和 `part` 列表需要存储最底层的所有节点。



---

### 五、 总结金句

> **“这叫‘去粗取精，边缘聚焦’。右视图算法是层序遍历的高级变体，它利用了 BFS 的空间秩序感，通过对每一层结果进行‘末位采样’，巧妙地模拟了人类视觉中的遮挡效应。这种‘全量遍历、定向提取’的思路，不仅能解决右视图，只需微调下标（如 `part[0]`），左视图也同样手到擒来。”**

---

### 💡 深度思考

这段代码先用 `part` 收集了整层的所有值，最后才取 `part[-1]`。如果考虑到空间效率，我们能不能在 `for` 循环中，通过判断 `node` 是否是当前循环的最后一个元素，直接把值填入 `result`，从而省掉这个临时的 `part` 列表呢？
