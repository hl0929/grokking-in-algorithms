
[85. Maximal Rectangle](https://leetcode.cn/problems/maximal-rectangle)

[0085_maximal_rectangle](./html/0085_maximal_rectangle.html ":include :type=iframe")

<a href="./content/html/0085_maximal_rectangle.html" target="_blank">点击此处在新窗口打开</a>

```python
def maximal_rectangle(matrix):
    if not matrix:
        return 0
    n = len(matrix[0])
    heights = [0] * n
    max_area = 0
    for row in matrix:
        for j in range(n):
            if row[j] == "1":
                heights[j] += 1
            else:
                heights[j] = 0
        area = largest_rectangle_area(heights)
        max_area = max(max_area, area)
    return max_area


def largest_rectangle_area(heights):
    heights = [0] + heights + [0]
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]  # 6
result = maximal_rectangle(matrix)
print(result)
```

这道题目（LeetCode 85. 最大矩形）的核心思想是 **“降维打击与复用（Reduction to Subproblem）”**。

它是上一题“柱状图中最大的矩形”的**终极进化版**。如果你已经掌握了如何处理一排柱子，那么面对一个二维矩阵，你只需要学会如何“变出一排排柱子”。

---

### 一、 核心思想：化面为线

我们要在一个由 `0` 和 `1` 组成的矩阵中找最大的全 `1` 矩形：
1.  **逐行扫描**：我们将矩阵的每一行作为“底边”。
2.  **累加高度**：对于每一行，我们计算每一个位置向上连续出现的 `1` 的个数。这就像是在这一行上筑起了一排“柱子”。
3.  **调用模板**：一旦有了这一行的柱子高度数组 `heights`，问题就瞬间退化成了我们刚学过的 **“柱状图中最大的矩形”**。



---

### 二、 算法逻辑：动态的直方图

#### 1. 变量分工
* `heights`：一个一维数组，记录当前行及其上方连续 `1` 的高度。
* `max_area`：全局最大矩形面积。

#### 2. 状态更新（每一行的洗牌）
* 遍历矩阵的每一行：
    * **如果是 "1"**：高度在上一行的基础上 `+1`。
    * **如果是 "0"**：地基断了，高度直接 **归零**。这一点非常关键，因为矩形必须是连续的。

#### 3. 借力打力
* 每更新完一行的 `heights`，就立刻丢给 `largest_rectangle_area` 函数算一把。
* 随着行数向下推移，这个虚拟的“直方图”在不断变幻形状，我们记录下在这个过程中出现过的所有矩形里的最大值。

---

### 三、 过程模拟 (`matrix` 示例)

1.  **第一行** `["1","0","1","0","0"]`:
    * `heights = [1, 0, 1, 0, 0]` -> 算面积：1
2.  **第二行** `["1","0","1","1","1"]`:
    * `heights = [2, 0, 2, 1, 1]`（第一列 1+1=2，第三列 1+1=2）-> 算面积：2
3.  **第三行** `["1","1","1","1","1"]`:
    * `heights = [3, 1, 3, 2, 2]` -> **重点！** 这排柱子能算出的最大面积是 **6**（由最后三列构成的 $3 \times 2$ 或 $2 \times 3$ 的一部分）。
4.  **第四行** `["1","0","0","1","0"]`:
    * `heights = [4, 0, 0, 3, 0]`（中间两个 0 让高度瞬间清零） -> 算面积：4

---

### 四、 复杂度分析

* **时间复杂度：$O(R \times C)$**
    * $R$ 是行数，$C$ 是列数。我们遍历了每个格子来更新高度，每一行调用单调栈的代价是 $O(C)$。总时间极其高效。
* **空间复杂度：$O(C)$**
    * 我们只需要一个长度为列数的数组 `heights` 来实时维护当前行的高度信息。

---

### 五、 总结金句

> **“这叫‘步步为营，借力打力’。最大矩形问题向我们展示了算法中‘复用’的最高境界：通过逐行扫描，我们将一个复杂的二维空间搜索，拆解成了若干个一维的单调栈问题。每一行都是一个全新的战场，而我们手中那把名为‘单调栈’的利剑，在每一层地基上都能划出最优的领地。这种将高维问题降维解决的思考方式，是掌握高级算法的必经之路。”**

---

### 💡 深度总结
至此，你已经完整走过了 **栈（Stack）** 的整个进阶路径：
1.  **基础栈**：有效括号（匹配与抵消）。
2.  **辅助栈**：最小栈（保存历史状态）。
3.  **单调栈**：每日温度（找下一个更大）、接雨水（找左右边界）、柱状图最大矩形（区间最大化）。
4.  **单调栈+降维**：最大矩形（二维转一维）。

这一套组合拳打下来，所有的“区间”、“边界”、“匹配”类问题在你面前都将无所遁形！准备好开启下一个专题了吗？

