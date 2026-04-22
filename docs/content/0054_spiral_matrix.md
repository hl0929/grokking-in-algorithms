
[54. Spiral Matrix](https://leetcode.cn/problems/spiral-matrix/)

[0054_spiral_matrix](./html/0054_spiral_matrix.html ":include :type=iframe")

<a href="./content/html/0054_spiral_matrix.html" target="_blank">点击此处在新窗口打开</a>

```python
def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    res = []
    while top <= bottom and left <= right:
        # 上边：从左到右
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1
        # 右边：从上往下
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        # 下边：从右往左
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
        # 左边：从下往上
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res
    
    
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] #[1,2,3,4,8,12,11,10,9,5,6,7]
result = spiral_matrix(matrix)
print(result)
```

这道题目（LeetCode 54. 螺旋矩阵）是按照螺旋路径**“收割”**。

它的核心思想是 **“边界收缩（Boundary Shrinking）”**。


### 一、 核心思想：层层剥开的洋葱

面对一个二维矩阵，我们要像剥洋葱一样，从最外层开始，顺时针一圈一圈地提取数字。

1.  **设立四极：** `top`, `bottom`, `left`, `right` 就像四面活动的墙。
2.  **收割即压缩：** 每当我们的视线扫过一行（或一列），这面墙就立刻向内推进一步，缩小搜索范围。
3.  **生存检查：** 相比正方形矩阵，长方形矩阵（如 $3 \times 4$）更容易出现“路已走完，但循环未停”的情况，因此那两行 `if` 判断是绝对的核心。

---

### 二、 算法逻辑：顺时针收割



#### 1. 收割顶行（从左到右）
* **动作：** 采集 `top` 这一行的所有果实。
* **压缩：** `top += 1`。最上面这行已经空了，墙向下移。

#### 2. 收割右列（从上往下）
* **动作：** 采集 `right` 这一列的剩余果实。
* **压缩：** `right -= 1`。最右边这列扫完了，墙向左移。

#### 3. 收割底行（从右到左）—— **强制刹车 1**
* **关键判断：** `if top <= bottom`。
* **原理：** 在长方形矩阵中，可能收割完顶行后，`top` 已经压过了 `bottom`。如果不检查，收割机就会在同一行里“折返跑”，重复读入数据。
* **动作：** 采集 `bottom` 这一行。随后 `bottom -= 1`。

#### 4. 收割左列（从下往上）—— **强制刹车 2**
* **关键判断：** `if left <= right`。
* **原理：** 防止左右边界已经交汇甚至错位时，收割机再次垂直扫过已经读过的区域。
* **动作：** 采集 `left` 这一列。随后 `left += 1`。

---

### 三、 过程模拟 (`matrix` = 3行4列)

1.  **初始状态：** `top=0, bottom=2, left=0, right=3`
2.  **第一圈：**
    * **向右：** 读 `[1,2,3,4]`。`top` 变 1。
    * **向下：** 读 `[8,12]`。`right` 变 2。
    * **向左：** 检查 `1 <= 2` 成立。读 `[11,10,9]`。`bottom` 变 1。
    * **向上：** 检查 `0 <= 2` 成立。读 `[5]`。`left` 变 1。
3.  **第二圈开始：**
    * **向右：** 此时 `top=1, bottom=1, left=1, right=2`。读入 `[6,7]`。`top` 变 2。
    * **向后判断：** `top(2) > bottom(1)`，`if` 判断全部失效，**循环结束**。

---

### 四、 复杂度分析

* **时间复杂度：$O(M \times N)$**
    * 矩阵里的每一个元素都被恰好“访问”并“收割”了一次。
* **空间复杂度：$O(1)$**
    * 除了存储答案的 `res` 列表外，我们只使用了 4 个边界指针。即使矩阵变成一万行，指针也就这 4 个。

---

### 五、 总结金句

> **“这叫‘走过的路不走第二次’。每一面墙的推进，都代表着矩阵领土的永久缩减。那两行 `if` 就是收割机的红外传感器，一旦发现上下或左右已经重叠，就说明果实已尽，必须立刻停机。”**
