
[4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)

[0004_median_of_two_sorted_arrays](./html/0004_median_of_two_sorted_arrays.html ":include :type=iframe")

<a href="./content/html/0004_median_of_two_sorted_arrays.html" target="_blank">点击此处在新窗口打开</a>

```python
def median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    lo, hi = 0, m
    while lo <= hi:
        mid_1 = (lo + hi) // 2
        mid_2 = (m + n + 1) // 2 - mid_1
        left_1 = nums1[mid_1 - 1] if mid_1 > 0 else float("-inf")
        right_1 = nums1[mid_1]    if mid_1 < m else float("inf")
        left_2 = nums2[mid_2 - 1] if mid_2 > 0 else float("-inf")
        right_2 = nums2[mid_2]    if mid_2 < n else float("inf")
        if left_1 < right_2 and left_2 < right_1:
            if (m + n) % 2 == 1:
                return max(left_1, left_2)
            return (max(left_1, left_2) + min(right_1, right_2)) / 2
        elif left_1 > right_2:
            hi = mid_1 - 1
        else:
            lo = mid_1 + 1
            
            
nums1 = [1, 2]
nums2 = [3, 4]
nums1 = [1, 3] 
nums2 = [2]
result = median_sorted_arrays(nums1, nums2)
print(result)
```

这道题目（LeetCode 4. 寻找两个正序数组的中位数）被公认为二分查找技巧的巅峰之作。它的核心思想是**从“合并数组”的思维跳出，转而利用“空间切分”来实现对数级的时间复杂度。**

以下是该算法的深度逻辑解析：

### 一、 核心思想：寻找“黄金分割线”

中位数的本质是将一组数划分为**数量相等**的两部分，且**左半部分的所有数 $\le$ 右半部分的所有数**。

对于两个数组 `nums1` 和 `nums2`，我们要在两个数组中各画一刀（切分点），把它们分别分成左右两段：

* **左半堆**：`nums1` 的左段 + `nums2` 的左段
* **右半堆**：`nums1` 的右段 + `nums2` 的右段

我们要寻找的那个完美位置，必须满足两个硬性条件：

1. **个数平衡**：左半堆的总个数 = 右半堆的总个数（总数为奇数时，左半堆多一个）。
2. **值的大小有序**：左半堆的**最大值** $\le$ 右半堆的**最小值**。

---

### 二、 算法逻辑：二分查找切分点

为了达到 $O(\log(min(m, n)))$ 的复杂度，算法采用了以下逻辑：

#### 1. 为什么在短数组上二分？

算法第一步通常是 `if len(nums1) > len(nums2): swap(nums1, nums2)`。

* **速度更快**：在较短的数组上搜索，查找范围更小。
* **防止越界**：一旦短数组的切分点 `mid1` 确定，长数组的切分点 `mid2` 会自动计算出来（为了满足个数平衡）。如果我们在长数组上搜，算出来的 `mid2` 可能会超出短数组的范围。

#### 2. 切分点的“此消彼长”

* 设定短数组切分点为 `mid1`，长数组切分点为 `mid2`。
* 由于总左半堆个数固定，`mid1` 增加，`mid2` 必然减少；`mid1` 向右移，`mid2` 必然向左移。

#### 3. 完美的判定条件（十字交叉检查）

由于 `nums1` 和 `nums2` 各自是有序的，我们只需要检查交叉位置：

* **条件 1**：`nums1[mid1-1] (L1) <= nums2[mid2] (R2)`
* **条件 2**：`nums2[mid2-1] (L2) <= nums1[mid1] (R1)`
* 如果这两个条件同时满足，恭喜你，这道“金线”找到了！

#### 4. 修正方向

* 如果 `L1 > R2`：说明 `nums1` 的左边拿多了，`mid1` 需要左移（`hi = mid1 - 1`）。
* 如果 `L2 > R1`：说明 `nums1` 的左边拿少了，`mid1` 需要右移（`lo = mid1 + 1`）。

---

### 三、 边界处理的智慧：无穷大与无穷小

当切分点落在数组的最左边或最右边时（比如某个数组完全被分到了右半堆），为了代码逻辑的统一，我们引入了“虚拟值”：

* **左边界越界**：认为 `L = -∞`（负无穷），它一定小于任何右边的数。
* **右边界越界**：认为 `R = +∞`（正无穷），它一定大于任何左边的数。

---

### 四、 结果计算

一旦找到切分点：

* **总数为奇数**：中位数就是左半堆里最大的那个：`max(L1, L2)`。
* **总数为偶数**：中位数是左边最大值和右边最小值的平均数：`(max(L1, L2) + min(R1, R2)) / 2`。

---

### 五、 总结

| 维度 | 描述 |
| --- | --- |
| **空间复杂度** | $O(1)$：只用了几个索引变量。 |
| **时间复杂度** | $O(\log(\min(m,n)))$：极度高效。 |
| **核心策略** | 将中位数问题转化为**两个数组同步二分切分**的问题。 |

**一句话总结：**
这套算法不是在找那个“数”，而是在找那道“线”。通过在短数组上二分，长数组像影子一样随之联动，直到左右两边的数值关系达成完美的平衡。