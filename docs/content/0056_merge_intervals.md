
[56. Merge Intervals](https://leetcode.com/problems/merge-intervals)

[0056_merge_intervals](./html/0056_merge_intervals.html ":include :type=iframe")

<a href="./content/html/0056_merge_intervals.html" target="_blank">点击此处在新窗口打开</a>

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    lst = [intervals[0]]
    for interval in intervals[1:]:
        if lst[-1][1] >= interval[0]:
            lst[-1][1] = max(lst[-1][1], interval[1])
        else:
            lst.append(interval)
    return lst


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(intervals)
print(result)
```

这道题目（LeetCode 56. 合并区间）的核心思想是利用**排序**来简化“重叠判定”，并配合**贪心策略**进行单次扫描合并。

它的逻辑可以总结为：**“先排序对齐起点，再顺序滚雪球”。**

### 一、 核心思想：消除乱序的干扰

区间重叠问题的难点在于，区间可能以任何顺序出现。如果你直接处理，你无法确定当前区间是否会与数组末尾的某个区间合并。

1. **排序（核心灵魂）**：我们按照区间的**起点 (start)** 进行升序排列。
* **排序后的好处**：一旦排序完成，我们就保证了如果两个区间发生重叠，它们在数组中一定是**相邻**的。
* **逻辑简化**：当我们处理到第 $i$ 个区间时，我们只需要关心它是否能与“当前已经合并好的最后一个区间”相交，而不需要去回溯之前的历史。


2. **贪心策略**：我们总是尝试将当前区间合并到现有的“最长结果”中。如果不能合并，则说明产生了一个新的独立区间。

---

### 二、 算法逻辑：三步走

以 `intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]` 为例：

#### 1. 预处理：按起点排序

排序后，我们确保了：如果 `A` 在 `B` 之前，那么 `A.start <= B.start`。

#### 2. 初始化结果集

取出第一个区间 `[1, 3]` 放入结果集 `merged`。

#### 3. 顺序扫描与判定

遍历后续每一个区间 `curr`，将其与 `merged` 中最后一个区间 `last` 进行比较：

* **情况 A：发生重叠（`last.end >= curr.start`）**
* 既然 `curr.start` 已经落在了 `last` 的范围内，它们必须合并。
* **更新动作**：将 `last` 的终点更新为 `max(last.end, curr.end)`。
* *例如：`[1, 3]` 和 `[2, 6]` 重叠，合并后变为 `[1, 6]`。*


* **情况 B：完全断开（`last.end < curr.start`）**
* 由于我们是按起点排序的，既然 `curr.start` 已经超过了 `last.end`，后面所有的区间起点只会更大。
* 这说明 `last` 已经“彻底定型”，再也不会有区间能与它合并了。
* **更新动作**：将 `curr` 作为一个新的独立区间存入 `merged`。
* *例如：`[1, 6]` 和 `[8, 10]` 之间有空隙，直接加入。*



---

### 三、 复杂度分析

* **时间复杂度：$O(N \log N)$**
* 最耗时的步骤是排序，需要 $O(N \log N)$。
* 随后的单次遍历只需要 $O(N)$。


* **空间复杂度：$O(\log N)$ 或 $O(N)$**
* 取决于排序算法本身的辅助空间开销。



---

### 四、 总结金句

> **“排序定先后，终点决去留。”** >
> 这个算法的巧妙之处在于：通过一次排序，将一个复杂的二维覆盖问题（起点和终点）降维成了一维的线性扫描问题。只要当前区间的起点能够“接上”上一个区间的终点，雪球就能继续滚大；接不上，就开启一个新的雪球。