
[146. LRU Cache](https://leetcode.cn/problems/lru-cache/)

[0146_lru_cache](./html/0146_lru_cache.html ":include :type=iframe")

<a href="./content/html/0146_lru_cache.html" target="_blank">点击此处在新窗口打开</a>


```python
from collections import OrderedDict


class LRUCache:
    def __init__(self, capability):
        self.cache = OrderedDict()
        self.capability = capability
        
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capability:
            self.cache.popitem(last=False)


lru = LRUCache(2)

lru.put(1, 1)  # 缓存: {1=1}
lru.put(2, 2)  # 缓存: {1=1, 2=2}
print(lru.get(1))  # 返回 1，顺序变为: {2=2, 1=1}

lru.put(3, 3)  # 淘汰 key=2，缓存: {1=1, 3=3}
print(lru.get(2))  # 返回 -1

lru.put(4, 4)  # 淘汰 key=1，缓存: {3=3, 4=4}
print(lru.get(1))  # 返回 -1
print(lru.get(3))  # 返回 3
print(lru.get(4))  # 返回 4
```

```python
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """哈希表+双端链表"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 哈希表：key -> Node
        
        # 创建虚拟头尾节点
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 将节点添加到链表头部（表示最近使用）
    def _add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 从链表中移除某个节点
    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # 将节点移动到链表头部
    def _move_to_head(self, node: Node):
        self._remove_node(node)
        self._add_to_head(node)

    # 移除尾部节点（最近最少使用）
    def _remove_tail(self) -> Node:
        node = self.tail.prev
        self._remove_node(node)
        return node

    # 获取缓存
    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        # 移动到头部，表示最近使用
        self._move_to_head(node)
        return node.value

    # 插入或更新缓存
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            # 更新值并移动到头部
            node.value = value
            self._move_to_head(node)
        else:
            # 新建节点
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

            # 如果超过容量，移除尾部节点
            if len(self.cache) > self.capacity:
                tail = self._remove_tail()
                del self.cache[tail.key]


lru = LRUCache(2)

lru.put(1, 1)  # 缓存: {1=1}
lru.put(2, 2)  # 缓存: {1=1, 2=2}
print(lru.get(1))  # 返回 1，顺序变为: {2=2, 1=1}

lru.put(3, 3)  # 淘汰 key=2，缓存: {1=1, 3=3}
print(lru.get(2))  # 返回 -1

lru.put(4, 4)  # 淘汰 key=1，缓存: {3=3, 4=4}
print(lru.get(1))  # 返回 -1
print(lru.get(3))  # 返回 3
print(lru.get(4))  # 返回 4
```


这道题目（LeetCode 146. LRU 缓存）的核心思想是 **“喜新厌旧（Freshness Prioritization）”**。

LRU 的全称是 *Least Recently Used*（最近最少使用）。它模仿了人类的记忆机制：空间有限，如果一个信息很久没被提起了，它就会被新信息挤出大脑。在 Python 中，`collections.OrderedDict` 简直就是为这道题量身定做的“神兵利器”。

---

### 一、 核心思想：有序的记忆碎片



你可以把 LRU 想象成一个有容量限制的 **“传送带”**：

1.  **越新越靠后**：不管是新加入的数据，还是刚刚被查看过（`get`）的老数据，都要重新放到传送带的 **末尾**（最新使用区）。
2.  **越旧越靠前**：那些长期没人理会的数据，会自动慢慢滑向传送带的 **最前端**（久未使用区）。
3.  **满员淘汰**：当传送带满了（超出 `capability`），最前端那个“落灰”最久的数据就会掉下去，给新人腾位子。

---

### 二、 算法逻辑：利用 OrderedDict 的天赋

Python 的 `OrderedDict` 结合了 **哈希表** 的查找速度（$O(1)$）和 **双向链表** 的顺序记录能力。

#### 1. 初始容量
* `self.capability`：设定了大脑能记多少东西。

#### 2. 读取（get）：刷新存在感
* 如果 `key` 不在缓存里，直接返回 `-1`。
* 如果在，利用 `move_to_end(key)`。这一步是灵魂：它就像是把一件旧衣服从衣柜深处拿出来穿了一下，然后重新叠好放在了**最显眼（末尾）**的位置。

#### 3. 写入（put）：新陈代谢
* **更新**：如果 `key` 已存在，先更新它的值，并同样把它推到末尾（`move_to_end`）。
* **新增**：如果是个新面孔，直接插到末尾。
* **淘汰**：做完上面的操作后，如果发现缓存超标了，就执行 `popitem(last=False)`。这里的 `last=False` 代表弹出 **最早进入** 的那一项（即传送带最前面的倒霉蛋）。

---

### 三、 过程模拟 (`capacity = 2`)

1.  **put(1, 1)**: 传送带 `[1]`。
2.  **put(2, 2)**: 传送带 `[1, 2]`。
3.  **get(1)**: 1 被提拔，顺序变为 `[2, 1]`（2 变成了最老的）。
4.  **put(3, 3)**:
    * 3 进场：`[2, 1, 3]`。
    * 超标！踢掉最老（头部）的 2。
    * 结果：`[1, 3]`。
5.  **put(4, 4)**:
    * 4 进场：`[1, 3, 4]`。
    * 超标！踢掉最老的 1。
    * 结果：`[3, 4]`。

---

### 四、 复杂度分析

* **时间复杂度：$O(1)$**
    * `OrderedDict` 的 `get`、`put`、`move_to_end` 和 `popitem` 全部都是常数级操作。这是缓存设计最硬核的指标。
* **空间复杂度：$O(C)$**
    * $C$ 是缓存的容量。我们只占用规定大小的空间，非常节约。

---

### 五、 总结金句

> **“LRU 算法就是一套‘职场升迁机制’。经常被‘点名’（get/put）的员工总是能留在核心圈并排在升迁前列；而那些长期被冷落、默默无闻的员工，则会在新人入职时，第一个领到离职补偿包。这种有序字典的设计，让‘谁最该走’和‘谁最新鲜’一目了然。”**

---

### 💡 进阶思考
虽然 Python 的 `OrderedDict` 很爽，但在硬核面试中，面试官经常会要求你 **“手动实现”**。那时你就不能作弊了，需要手写一个 **“HashMap + 双向链表”**。你想了解一下，如果不依赖内置库，如何用最原始的指针连接去构建这台“记忆传送带”吗？

