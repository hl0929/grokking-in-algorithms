
[42. Trapping Rain Water](https://leetcode.cn/problems/trapping-rain-water/)

[0042_trapping_rain_water](./html/0042_trapping_rain_water.html ":include :type=iframe")

<a href="./content/html/0042_trapping_rain_water.html" target="_blank">点击此处在新窗口打开</a>

```python
def trapping(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    total = 0
    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            total += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            total += right_max - height[right]
    return total


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] # 6
result = trapping(height)
print(result)
```

这道题目（LeetCode 42. 接雨水）的核心思想是 **“木桶效应与双向夹击（Two Pointers & Buckets Effect）”**。

在算法的世界里，这是一个关于“边界决定上限”的经典案例。我们不需要关心水坑到底有多宽，只需要关心每一根柱子上方能接多少水。

---

### 一、 核心思想：短板理论



想象你在一个高低不平的地形上：
1.  **谁决定水位？** 对于任何一个位置，它能接多少水，取决于它左边最高的柱子和右边最高的柱子中，**较矮的那一个**。
2.  **局部确定性**：如果你知道左边的最大高度 `left_max` 小于右边的最大高度 `right_max`，那么无论中间还有多少高耸入云的柱子，当前左侧位置的水位高度就已经被 `left_max` 锁死了。
3.  **双指针博弈**：我们从两头向中间靠拢，谁矮就移动谁，并更新那一侧的“最高峰”。

---

### 二、 算法逻辑：双指针的优雅

#### 1. 变量分工
* `left`, `right`：两个勤奋的探测员，从阵地两头出发。
* `left_max`, `right_max`：记录到目前为止，左边和右边分别出现过的“最高海拔”。
* `total`：我们的水库总量。

#### 2. 核心逻辑：哪边矮，走哪边
* **比较 `height[left]` 和 `height[right]`**：
    * 如果左边比较矮，我们就往右挪一步（`left += 1`）。因为我们确定，右边至少有一个比当前左边更高的“墙”能挡住水。
    * 此时，如果 `left_max` 大于当前的 `height[left]`，多出来的部分就是这一格接的水：`left_max - height[left]`。
    * 反之，如果右边比较矮，我们就往左挪一步（`right -= 1`），逻辑同理。

#### 3. 无需额外空间
* 相比于动态规划需要两个 $O(N)$ 数组记录左右最高点，双指针法在移动过程中实时更新 `max`，将空间优化到了极致。

---

### 三、 过程模拟 (`height = [0, 1, 0, 2]`)

1.  **初始**：`left=0, right=3`, `left_max=0, right_max=2`。
2.  **第一步**：`height[left](0) < height[right](2)`，左指针右移。
    * `left=1`, `height[1]=1`, `left_max` 更新为 1。
    * 接水：`1 - 1 = 0`。
3.  **第二步**：`height[left](1) < height[right](2)`，左指针再右移。
    * `left=2`, `height[2]=0`, `left_max` 还是 1。
    * **接水！** `1 - 0 = 1`。这一滴水被成功捕捉。
4.  **第三步**：`left` 和 `right` 相遇，战斗结束。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 两个指针各走半程，加起来正好遍历一遍数组。
* **空间复杂度：$O(1)$**
    * 只用了几个变量。在处理海量地形数据时，这种空间节省简直是艺术。

---

### 五、 总结金句

> **“这叫‘知彼知己，随遇而安’。接雨水的精髓在于：我们并不需要纵观全局去寻找每一个水洼，而是利用双指针的对峙，在每一个局部瞬间锁定了水位上限。当一侧的‘最高峰’确定弱于另一侧时，所有的不确定性都消失了，剩下的只是简单的减法。这种利用短板效应将复杂地形降维成单点计算的思路，是双指针算法的巅峰之作。”**

---

### 💡 深度思考
这道题还有一种解法是使用 **“单调栈”**。单调栈是按“行”来计算水量的（找凹槽），而双指针是按“列”来计算水量的。你觉得如果地形非常极端（比如只有两根巨高的柱子在两头，中间全是矮柱子），哪种解法在直观感受上更符合你对“装满水”的直觉？