
[34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

[0034_find_first_and_last_position_of_element_in_sorted_array](./html/0034_find_first_and_last_position_of_element_in_sorted_array.html ':include :type=iframe')

<a href="./content/html/0034_find_first_and_last_position_of_element_in_sorted_array.html" target="_blank">点击此处在新窗口打开</a>

```python
def find_range(nums, target):
    def binary_search(nums, find_left):
        left, right = 0, len(nums) - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                pos = mid
                if find_left:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return pos
    
    left = binary_search(nums, find_left=True)
    right = binary_search(nums, find_left=False)
    return [left, right]


nums = [1, 2, 3, 3, 4]  
target = 3
result = find_range(nums, target)
print(result)
```

这道题目（LeetCode 34. 在排序数组中查找元素的第一个和最后一个位置）的核心思想是 **“二分查找的边界收缩”**。

普通的二分查找（Binary Search）在找到目标值 `target` 时会立即返回，而这道题要求我们找到一个**连续区间的起点和终点**。

### 一、 核心思想：不要停下来

该算法最精妙的地方在于：**即便找到了目标值，也不停止搜索，而是继续向边缘“挤压”。**

1. **寻找左边界（First Position）**：
* 当 `nums[mid] == target` 时，我们记录下当前位置 `pos`。
* 但我们不确定左边是否还有相同的 `target`。
* **核心逻辑**：令 `right = mid - 1`。这强迫搜索区间继续向左半部分收缩，直到找不动为止。


2. **寻找右边界（Last Position）**：
* 当 `nums[mid] == target` 时，同样记录 `pos`。
* **核心逻辑**：令 `left = mid + 1`。这强迫搜索区间向右半部分收缩，去探测最右侧的边界。



---

### 二、 算法逻辑拆解

我们可以把这个过程想象成两把“钳子”：

#### 1. 第一把钳子：定起点 (`find_left=True`)

* **目标**：把搜索范围尽可能向左推。
* **过程**：
* 如果 `nums[mid]` 太大或者刚好等于 `target`，我们就把右边界 `right` 往左移。
* 这样最后留下的 `pos` 一定是最靠左的那个。



#### 2. 第二把钳子：定终点 (`find_left=False`)

* **目标**：把搜索范围尽可能向右推。
* **过程**：
* 如果 `nums[mid]` 太小或者刚好等于 `target`，我们就把左边界 `left` 往右移。
* 这样最后留下的 `pos` 一定是最靠右的那个。



---

### 三、 为什么这么做高效？

* **时间复杂度：$O(\log N)$**
* 虽然我们调用了两次二分查找，但常量倍数在算法复杂度中被忽略。
* 相比于先找到一个 `target` 再用线性扫描（左右各走一步）的 $O(N)$ 做法，这种纯二分法在处理**含有大量重复元素**的超长数组（例如 `[3, 3, 3, ..., 3]`）时，性能优势是巨大的。


* **空间复杂度：$O(1)$**
* 只使用了几个指针变量，没有开启额外的内存空间。



---

### 四、 总结（金句）

> **“二分查找不仅能找一个点，还能通过控制区间的收缩方向，‘挤’出目标的边界。”**

通过传入一个布尔值 `find_left` 来复用同一套二分逻辑，既体现了代码的简洁性（DRY原则），又精准地利用了二分搜索的区间收缩特性。