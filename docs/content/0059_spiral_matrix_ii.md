
[59. Spiral Matrix II](https://leetcode.cn/problems/spiral-matrix-ii)

[0059_spiral_matrix_ii](./html/0059_spiral_matrix_ii.html ":include :type=iframe")

<a href="./content/html/0059_spiral_matrix_ii.html" target="_blank">点击此处在新窗口打开</a>

```python
def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        # 上边：从左往右
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1
        # 右边：从上往下
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        # 下边：从右往左
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
        # 左边：从下往上
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    return matrix


n = 3 # [[1,2,3],[8,9,4],[7,6,5]]
result = generate_spiral_matrix(n)
print(result)
```

这道题目（LeetCode 59. 螺旋矩阵 II）的核心思想是 **“边界收缩（Boundary Shrinking）”**。如果说前面的题目是在找规律或做标记，这道题更像是在指挥一辆 **“带有自动刹车系统的铺路机”**。

你可以把这个算法想象成一个 **“围城铺路”** 的过程。

---

### 一、 核心思想：不断缩小的包围圈

我们要把 $1$ 到 $n^2$ 的数字填进矩阵，顺序是先往右、再往下、再往左、再往上。

1.  **设立四面城墙**：我们给矩阵设定了四个“边界指针”：`top`（上）、`bottom`（下）、`left`（左）、`right`（右）。
2.  **步步为营**：每铺完一面墙，我们就把这面墙向内推进一步。随着墙的不断靠拢，铺路机走过的路径自然就形成了一个螺旋形。

---

### 二、 算法逻辑：四部曲循环



#### 1. 铺上边：从左往右
* 在 `top` 这一行，从 `left` 铺到 `right`。
* **结算**：最上面这排铺完了，`top` 往下移（`top += 1`）。

#### 2. 铺右边：从上往下
* 在 `right` 这一列，从现在的 `top` 铺到 `bottom`。
* **结算**：最右边这列铺完了，`right` 向左移（`right -= 1`）。

#### 3. 铺下边：从右往左（**关键判断**）
* **判断**：`if top <= bottom`。
* **原因**：因为刚才 `top` 刚往下移了，如果此时它已经超过了 `bottom`，说明中间已经没位子了，必须立刻“刹车”。
* **动作**：在 `bottom` 这一行，倒着走回去。随后 `bottom` 向上收缩。

#### 4. 铺左边：从下往上（**关键判断**）
* **判断**：`if left <= right`。
* **原因**：刚才 `right` 往左移了，如果它已经跑到了 `left` 的左边，说明左右已经闭合。
* **动作**：在 `left` 这一列，向上走回去。随后 `left` 向右收缩。

---

### 三、 过程模拟 ($n = 3$)

1.  **初始状态**：`top=0, bottom=2, left=0, right=2`, `num=1`
2.  **向右铺**：填充 `(0,0), (0,1), (0,2)` 为 `1, 2, 3`。`top` 变 1。
3.  **向下铺**：填充 `(1,2), (2,2)` 为 `4, 5`。`right` 变 1。
4.  **向左铺**：检查 `1 <= 2` 成立。填充 `(2,1), (2,0)` 为 `6, 7`。`bottom` 变 1。
5.  **向上铺**：检查 `0 <= 1` 成立。填充 `(1,0)` 为 `8`。`left` 变 1。
6.  **开启新轮次**：`while` 条件依然成立。
    * **再次向右铺**：填充 `(1,1)` 为 `9`。`top` 变 2。
    * **此时检查**：`top(2) > bottom(1)`，后续判断失败，全线刹车。

---

### 四、 复杂度分析

* **时间复杂度：$O(n^2)$**
    * 矩阵中每一个格子都恰好被访问并填入了一个数字，格子总数是 $n \times n$。
* **空间复杂度：$O(1)$**
    * 除了存储结果的矩阵外，我们只用了 4 个边界变量，空间消耗不随 $n$ 的增大而指数级增长。

---

### 五、 总结金句

> **“如果不加那两行 `if`，铺路机就像是一个没有传感器的扫地机器人，即便房间已经扫完了，它还会对着墙根惯性冲刺，把已经铺好的路重新弄乱。有了 `if` 刹车，它才真正拥有了‘见好就收’的智慧。”**
