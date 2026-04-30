
[912. Sort an Array](https://leetcode.cn/problems/sort-an-array)

[0912_sort_an_array](./html/0912_sort_an_array.html ":include :type=iframe")

<a href="./content/html/0912_sort_an_array.html" target="_blank">点击此处在新窗口打开</a>

```python
def sort_array(nums):
    return _quick_sort(nums)


def _quick_sort(nums):
    if len(nums) < 2:
        return nums
    mid = nums[0]
    left = [i for i in nums if i < mid]
    middle = [i for i in nums if i == mid]
    right = [i for i in nums if i > mid]
    return _quick_sort(left) + middle + _quick_sort(right)


nums = [5, 1, 1, 2, 0, 0] 
result = sort_array(nums)
print(result)
```

这道题目（LeetCode 912. 排序数组）展示的是 **快速排序（Quick Sort）** 的最直观实现，核心思想是 **“分而治之与基准分区（Divide and Conquer & Partitioning）”**。

虽然这段代码使用了 Python 特有的列表推导式（List Comprehension），让逻辑变得像诗一样简洁，但它背后蕴含的是计算机科学中最伟大的排序思想之一。

---

### 一、 核心思想：寻找“绝对坐标”

快速排序的精髓在于：**选一个基准点（Pivot），然后让全世界围着它转。**
1.  **选定基准**：随机或固定选一个数（代码里选了 `nums[0]`）。
2.  **三军对垒**：
    *   **左军 (left)**：所有比基准小的数字，去左边排队。
    *   **中军 (middle)**：所有等于基准的数字，原地待命。
    *   **右军 (right)**：所有比基准大的数字，去右边排队。
3.  **递归制胜**：此时，`middle` 已经在它最终排序后该在的位置上了。我们只需要对 `left` 和 `right` 重复上述过程，直到每个数字都找到自己的位置。



---

### 二、 算法逻辑：递归的优雅

#### 1. 递归出口（Base Case）
*   `if len(nums) < 2: return nums`
    *   当数组只剩一个数字或者为空时，它天生就是有序的，不需要再折腾了。

#### 2. 基准分区（Partitioning）
*   这段代码采用了 **“三路划分（Three-way Partition）”** 的变体：
    *   它不仅分出了比基准大和小的，还专门把**相等的**提炼了出来。
    *   **优势**：处理包含大量重复数字的数组（如 `[0, 0, 1, 1, 5, 5]`）时，这种方法极其高效，因为它能一次性搞定所有相同的数字。

#### 3. 组合还原
*   `return _quick_sort(left) + middle + _quick_sort(right)`
    *   这是典型的后序遍历思想：先解决子问题，再把结果拼接起来。

---

### 三 : 过程模拟 (`nums = [5, 1, 2, 0]`)

1.  **第一层递归**：基准 `mid = 5`。
    *   `left = [1, 2, 0]`, `middle = [5]`, `right = []`。
    *   等待 `_quick_sort([1, 2, 0])` 的结果。
2.  **第二层递归**：处理 `[1, 2, 0]`，基准 `mid = 1`。
    *   `left = [0]`, `middle = [1]`, `right = [2]`。
3.  **第三层递归**：处理 `[0]` 和 `[2]`。
    *   触发出口，直接返回 `[0]` 和 `[2]`。
4.  **回溯合并**：
    *   第二层返回 `[0] + [1] + [2] = [0, 1, 2]`。
    *   第一层返回 `[0, 1, 2] + [5] + [] = [0, 1, 2, 5]`。

---

### 四、 复杂度分析

*   **时间复杂度：平均 $O(N \log N)$**
    *   理想情况下，每次基准都能把数组平分，递归深度就是 $\log N$。
    *   **最坏情况 $O(N^2)$**：如果数组已经有序，且每次都选第一个数做基准，递归就会退化成单链表。
*   **空间复杂度：$O(N)$**
    *   注意：这种写法为了简洁，每次递归都创建了新的列表。在追求极致性能的面试中，通常要求使用 **“原地排序（In-place）”** 的双指针写法来达到 $O(\log N)$ 的空间复杂度。

---

### 五、 总结金句

> **“这叫‘定点爆破，层层包围’。快速排序的魅力在于它不急于调整所有数字的顺序，而是每一次都致力于让‘一部分人’先归位。通过基准点的不断确立，混乱的数组被切割成越来越小的有序碎片。这种‘我命由我不由天’的基准选择逻辑，配合递归的自我调用，构建了工业界最常用的排序基石。”**

---

### 💡 深度思考
这段代码虽然美，但在遇到**已经排好序**的大数组时会因为递归太深而崩溃（Stack Overflow）。如果想让它更强健（Robust），你觉得把 `mid = nums[0]` 改成什么样会更好呢？（提示：随机化是算法的护身符！）