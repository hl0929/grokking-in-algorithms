
[155. Min Stack](https://leetcode.cn/problems/min-stack)

[0155_min_stack](./html/0155_min_stack.html ":include :type=iframe")

<a href="./content/html/0155_min_stack.html" target="_blank">点击此处在新窗口打开</a>

```python
class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val):
        self.stack.append(val)
        cur_min = val
        if self.min_stack:
            cur_min = min(self.min_stack[-1], val)
        self.min_stack.append(cur_min)
        
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # -3
minStack.pop()
print(minStack.top())  # 0
print(minStack.getMin())  # -2
```

这道题目（LeetCode 155. 最小栈）的核心思想是 **“同步辅助（Synchronized Support）”**。

在普通栈的基础上，我们要实现一个能在 $O(1)$ 时间获取最小值的 `getMin` 功能。这看起来很矛盾：栈在不停变动，最小值也在变，怎么可能不遍历就立刻知道谁最小？

答案就是：**给主栈配一个“影子卫士”。**

---

### 一、 核心思想：时刻记录的“历史快照”

普通的栈只记得“现在有什么”，却不记得“过去谁最小”。如果我们想在弹出一个元素后立刻知道剩下的谁最小，我们就必须在**每个元素入栈时**，顺便记下“到目前为止，见过的最小值是谁”。

1.  **数据栈（stack）**：老老实实存入每一个数据。
2.  **最小栈（min_stack）**：存入对应的“当前全局最小值”。
3.  **同步性**：两个栈同生共死。每入栈一个元素，最小栈就多存一个当前的最小值；每弹出一个元素，最小栈也跟着弹出一个。

---

### 二、 算法逻辑：双栈合璧



#### 1. 初始化
* 我们准备了两个列表。`self.stack` 是本体，`self.min_stack` 是我们专门请来的“账本”。

#### 2. 入栈（push）
* 主栈照常添加 `val`。
* **计算当前最小值**：如果最小栈不为空，我们就拿 `val` 跟最小栈的“栈顶”（也就是上一步的最小值）比一比，谁小存谁。
* **同步入栈**：把计算出的 `cur_min` 存入 `min_stack`。
* **意义**：最小栈的每一个位置，都对应着主栈在该高度时，其下方所有元素的最小值。

#### 3. 出栈（pop）
* 既然是同步录入的，那出栈也必须同步。
* 当主栈弹出元素时，对应的“历史最小值”也失去了意义，所以 `min_stack` 也要跟着 `pop`。

#### 4. 获取最小值（getMin）
* 不需要任何计算，直接翻开“账本”的最后一页（`self.min_stack[-1]`），那里面存的就是当前主栈里的最优解。

---

### 三、 过程模拟 (`push(-2), push(0), push(-3)`)

1.  **push(-2)**:
    * `stack = [-2]`
    * `min_stack = [-2]`（第一个数，它就是最小）
2.  **push(0)**:
    * `stack = [-2, 0]`
    * `min_stack = [-2, -2]`（0 和 -2 比，-2 胜出，继续记下 -2）
3.  **push(-3)**:
    * `stack = [-2, 0, -3]`
    * `min_stack = [-2, -2, -3]`（-3 和 -2 比，-3 胜出）
4.  **getMin()**: 直接看 `min_stack` 栈顶，得到 **-3**。
5.  **pop()**: 两个栈同步弹出末尾。
    * `stack = [-2, 0]`
    * `min_stack = [-2, -2]`
6.  **getMin()**: 看 `min_stack` 栈顶，瞬间找回了之前的最小值 **-2**。

---

### 四、 复杂度分析

* **时间复杂度：$O(1)$**
    * 无论是 `push`、`pop` 还是 `getMin`，全部都是常数级操作。这完美解决了普通栈查找最小值需要 $O(N)$ 的痛点。
* **空间复杂度：$O(N)$**
    * 我们牺牲了一倍的空间（额外的 `min_stack`）来换取时间上的极速。

---

### 五、 总结金句

> **“这叫‘空间换时间，影子记历史’。最小栈就像是一个忠诚的记录官，它并不干涉主栈的进出，只是在每一个时刻都默默记下当时的全局最低点。这种‘同步增长、同步消亡’的策略，让复杂的全局搜索变成了简单的‘翻看旧账’，极简而优雅。”**

---

### 💡 深度思考
如果你的面试官是个“极简主义者”，他问你：**“能不能只用一个栈就实现 MinStack？”** 其实是可以的，你可以每次入栈一个 `(值, 当前最小值)` 的元组。虽然形式变了，但核心逻辑依然是“保存历史快照”。你觉得如果我们要实现一个 **MaxStack**（最大栈），逻辑会有什么不同吗？

