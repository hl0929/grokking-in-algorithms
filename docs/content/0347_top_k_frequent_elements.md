
[0347 Top K Frequent Elements](https://leetcode.cn/problems/top-k-frequent-elements)

[0347_top_k_frequent_elements](./html/0347_top_k_frequent_elements.html ":include :type=iframe")

<a href="./content/html/0347_top_k_frequent_elements.html" target="_blank">点击此处在新窗口打开</a>

```python
def topk_frequent(nums, k):
    freq_dict = dict()
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_dict.items():
        buckets[freq].append(num)
    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res
        
    
nums = [1,1,1,2,2,3] 
k = 2 # [1,2]
result = topk_frequent(nums, k)
print(result)
```

这道题目（LeetCode 347. 前 K 个高频元素）的核心思想是 **“桶排序（Bucket Sort）”**。如果说前面的题目是在找位置或者收割，这道题更像是在做一个 **“人气选秀排行榜”**。

通常找前 K 个我们会想到排序（$O(N \log N)$），但通过桶排序，我们可以实现惊人的 **$O(N)$ 线性时间复杂度**。


### 一、 核心思想：频率即坐标

这道题最巧妙的地方在于：它把**“出现的次数”**直接当成了**“数组的下标”**。

1.  **票数统计**：先用一个哈希表（`freq_dict`）统计每个数字一共出现了几次。
2.  **按票入座**：创建一个大列表 `buckets`，里面有 `len(nums) + 1` 个桶。如果数字 `1` 出现了 `3` 次，就把 `1` 扔进 `buckets[3]` 这个桶里。
3.  **降序开奖**：从最大的桶（出现次数最多的）开始往回倒着数，直到凑够 $k$ 个明星数字为止。

---

### 二、 算法逻辑：三步走

以 `nums = [1, 1, 1, 2, 2, 3], k = 2` 为例：

#### 1. 计票：谁人气最高？
* 扫描数组，记录每个人的得票数。
* 结果：`{1: 3票, 2: 2票, 3: 1票}`。

#### 2. 分桶：相同票数的站在一起
* 准备好一排桶，索引表示票数。
* **关键点**：票数最多也就是数组的长度（即所有人都是同一个数）。
* `buckets[3]` 里放入 `[1]`
* `buckets[2]` 里放入 `[2]`
* `buckets[1]` 里放入 `[3]`



#### 3. 截取：从高到低取前 K 名
* 从 `buckets` 的最右端（票数最高端）开始遍历。
* 先看 `buckets[3]`，拿到 `1`，此时结果集 `res = [1]`。
* 再看 `buckets[2]`，拿到 `2`，此时结果集 `res = [1, 2]`。
* **判断**：已经凑够 $k=2$ 个了，直接收工返回。

---

### 三、 过程模拟 (`nums = [1,1,1,2,2,3], k = 2`)

1.  **哈希表阶段**：得到 `1 -> 3, 2 -> 2, 3 -> 1`。
2.  **创建桶**：`buckets = [[], [], [], [], [], [], []]`（长度为 7 的列表）。
3.  **填装桶**：
    * `buckets[3].append(1)`
    * `buckets[2].append(2)`
    * `buckets[1].append(3)`
4.  **倒序提取**：
    * 从索引 6 扫到 1。
    * 碰到 `buckets[3]`，拿到 `1`。
    * 碰到 `buckets[2]`，拿到 `2`。
    * 满足 `len(res) == 2`，结束。

---

### 四、 复杂度分析

* **时间复杂度：$O(N)$**
    * 计票 $O(N)$，填桶 $O(N)$，最后倒序看一眼桶也是 $O(N)$。完美避开了排序的 $O(N \log N)$。
* **空间复杂度：$O(N)$**
    * 我们用了哈希表和桶列表，它们的大小都与原始数组的长度 $N$ 成正比。

---

### 五、 总结金句

> **“普通排序是让所有人排成一队比身高，而桶排序是直接在地上画好‘身高刻度’，让大家站到对应的刻度线上。最后我们只需要从最高的那条线往回看，谁站得最高一目了然。”**
