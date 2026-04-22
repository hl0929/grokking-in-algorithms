
[33. Search in Rotated Sorted Array](https://leetcode.cn/problems/search-in-rotated-sorted-array/)

[0033_search_in_rotated_sorted_array](./html/0033_search_in_rotated_sorted_array.html ":include :type=iframe")

<a href="./content/html/0033_search_in_rotated_sorted_array.html" target="_blank">点击此处在新窗口打开</a>

```python
def search_rotated_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


nums = [4,5,6,7,0,1,2] 
target = 0 #4
result = search_rotated_sorted(nums, target)
print(result)
```

这道题目（LeetCode 33. 搜索旋转排序数组）的核心思想是 **“局部有序性（Partial Order）”**。如果说普通的二分查找是在一条笔直的路上找人，那么这道题就像是在一条 **“断掉并错位”** 的山路上找人。

虽然数组被旋转了，但只要切一刀，**左半部分或右半部分，一定有一边是保有序的**。

---

### 一、 核心思想：先选平路，再定范围

在旋转数组中，`mid` 会把数组分成两部分。因为只旋转了一次，所以这两部分里**至少有一部是递增的**。

1.  **分清虚实**：二分查找的第一步不是直接比数字，而是先判断：**“哪一边是正常的升序排列？”**
2.  **圈地自省**：
    * 如果左边是升序，且 `target` 刚好在这个范围内，我们就去左边找。
    * 否则，`target` 肯定在右边（那个包含断层的一边）。
3.  **排除法**：每一次循环都能砍掉一半的搜索区间，保持了二分查找的高效性。

---

### 二、 算法逻辑：先断是非，再定去留

以 `nums = [4, 5, 6, 7, 0, 1, 2], target = 0` 为例：

#### 1. 确定基准
* 设定 `left` 和 `right`。计算 `mid` 指向的数值。
* 如果 `nums[mid]` 刚好是 `target`，直接收工。

#### 2. 情况 A：左半段是有序的 (`nums[left] <= nums[mid]`)
* **判断**：`target` 是否在 `[left, mid]` 之间？
    * **是**：把范围缩小到左边（`right = mid - 1`）。
    * **否**：那只能去右边那个“有断层”的区域碰碰运气（`left = mid + 1`）。

#### 3. 情况 B：右半段是有序的 (`nums[mid] < nums[right]`)
* **判断**：`target` 是否在 `[mid, right]` 之间？
    * **是**：把范围缩小到右边（`left = mid + 1`）。
    * **否**：那只能回左边那个“有断层”的区域找（`right = mid - 1`）。



---

### 三、 过程模拟 (`nums = [4,5,6,7,0,1,2], target = 0`)

1.  **第一轮**：`left=0, right=6, mid=3` (数字 7)。
    * **看左边**：`nums[0](4) <= nums[3](7)`，左半段 `[4,5,6,7]` 是有序的。
    * **查范围**：`target(0)` 在 `4` 到 `7` 之间吗？**不在。**
    * **去哪找**：去右边。`left = 4`。

2.  **第二轮**：`left=4, right=6, mid=5` (数字 1)。
    * **看左边**：`nums[4](0) <= nums[5](1)`，左半段 `[0,1]` 是有序的。
    * **查范围**：`target(0)` 在 `0` 到 `1` 之间吗？**在！** (注意 `0 <= 0 < 1`)
    * **去哪找**：收缩右边界。`right = 4`。

3.  **第三轮**：`left=4, right=4, mid=4` (数字 0)。
    * **匹配**：`nums[4] == 0`，**找到！** 返回索引 4。

---

### 四、 复杂度分析

* **时间复杂度：$O(\log N)$**
    * 虽然数组被旋转了，但我们依然每次排除了二分之一的区域，完美保留了二分查找的精髓。
* **空间复杂度：$O(1)$**
    * 只用了 `left`, `right`, `mid` 三个指针变量。

---

### 五、 总结金句

> **“旋转数组就像是一根折断的竹竿。虽然它不再是一条直线，但折断后的每一截单独看依然是直的。我们二分查找时，先找到那截‘直’的，看看人在不在里面；不在，就去另一截‘断’的里面继续找。这叫：‘借序识路，断处求真’。”**
