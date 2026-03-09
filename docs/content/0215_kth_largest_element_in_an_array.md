
[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

[0215-kth-largest-element-in-an-array](./html/0215_kth_largest_element_in_an_array.html ':include :type=iframe')

```python
import random

def find_kth_largest(nums, k):
    pivot = random.choice(nums)
    
    left = [i for i in nums if i > pivot]
    mid = [i for i in nums if i == pivot]
    right = [i for i in nums if i < pivot]
    
    if len(left) >= k:
        return find_kth_largest(left, k)
    elif len(left) + len(mid) >= k:
        return pivot
    else:
        return find_kth_largest(right, k - len(left) - len(mid))

        
nums = [1, 2, 4, 3, 5] 
k = 2
result = find_kth_largest(nums, k)
print(result)
```


这道题目（LeetCode 215. 数组中的第 K 个最大元素）所使用的算法被称为 快速选择算法（Quick Select）。它是快速排序（Quick Sort）的一个变种，核心思想是 “分治法（Divide and Conquer）” 和 “减而治之（Decrease and Conquer）”。


### 一、 核心思想：二分剪枝 (Binary Pruning)

快速选择的核心思想可以总结为：**“只管目标所在的区域，不管其他人的顺序。”**

* **对比排序**：如果你使用快速排序，你会递归地处理基准点（Pivot）的两侧，因为你需要整个数组都有序。
* **快速选择**：你只需要找到那个“特定位置”的数。通过分区（Partition），你可以确定第 $K$ 大的数是在基准点的左边还是右边。一旦确定，你就**彻底抛弃**不包含目标的另一半。

这种“剪枝”行为将平均时间复杂度从排序的 $O(N \log N)$ 降低到了线性级别的 **$O(N)$**。

---

### 二、 逻辑步骤分解

代码中的逻辑可以分为三个阶段：

#### 1. 选取基准与分区 (Pivot & Three-Way Partition)

算法首先随机选取一个数作为 `pivot`。随机化非常重要，它可以防止算法在处理特殊输入（如已排序数组）时退化。

* `left`: 收集所有 **大于** `pivot` 的数。
* `mid`: 收集所有 **等于** `pivot` 的数。
* `right`: 收集所有 **小于** `pivot` 的数。

#### 2. 三路区间判定

现在数组被切成了三块。我们根据 $K$ 的落点来做决策：

* **情况 A：`len(left) >= k**`
* 意味着比 `pivot` 大的数字已经超过（或等于） $K$ 个。
* **结论**：我们要找的目标一定在 `left` 这一堆里。
* **动作**：递归进入 `left`，继续找第 $K$ 大。


* **情况 B：`len(left) + len(mid) >= k**`
* 意味着 `left` 里的数不够 $K$ 个，但加上和 `pivot` 相等的数（`mid`）就够了。
* **结论**：既然 `left` 里的数都比 `pivot` 大，且加上 `mid` 后正好覆盖了第 $K$ 位。
* **动作**：找到了！结果就是 `pivot` 本身。


* **情况 C：`k > len(left) + len(mid)**`
* 意味着前两部分加起来都不到 $K$ 个，说明第 $K$ 大的数在更小的 `right` 区里。
* **动作**：递归进入 `right`。**注意：** 此时目标变为找 `right` 里的第 $K - (\text{len(left)} + \text{len(mid)})$ 大，因为我们已经跳过了前面那些更大的数。



---

### 三、 算法性能深度解析

1. **平均时间复杂度：$O(N)$**
* 数学模型：$N + N/2 + N/4 + \dots \approx 2N$。
* 每次迭代平均排除了一半的数据，工作量呈几何级数递减。


2. **最坏时间复杂度：$O(N^2)$**
* 如果运气极差，每次选的基准都是最大或最小值（导致每次只排除了一个元素）。但在使用了 `random.choice` 后，这种情况发生的概率在概率论上可以忽略不计。


3. **空间复杂度：$O(N)$**
* 这个具体的 Python 实现使用了列表推导式创建新列表，直观但耗费空间。
* *进阶提示*：在工业级实现中（如 C++ 的 `std::nth_element`），通常使用“原地交换”（In-place）的方法，将空间复杂度降至 $O(1)$。



---

### 四、 核心思想总结（金句）

> **“通过一次分区确定一个位置，通过位置判断方向，通过方向剪掉一半负担。”**

它就像在图书馆找一本编号为 500 的书：如果你随机抽出的一本是 400 号，你直接扔掉 400 以前的所有书架，只在后半段找。这种“目的一致性”让它在处理海量数据寻找 Top-K 时，具有无与伦比的效率。