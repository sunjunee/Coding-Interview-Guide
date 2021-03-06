# -*- coding: utf-8 -*-
"""
@ Author: Jun Sun {Python3}
@ E-mail: sunjunee@qq.com
@ Date:   2018-06-02 20:30:45
"""

# T1-6 用栈来求解汉诺塔问题
# 汉诺塔问题比较经典，这里修改一下游戏规则：现在限制不能从最左侧的
# 塔移动到最右侧的塔，也不能从最右侧直接移动到最左侧，而是必须经过
# 中间。求当塔有N层的时候，打印最优移动过程和最优移动总步数。

# 思路：递归求解，经典解法
# 对于两层（A、B）的情况，从塔1移动到塔3共需要8步
# - B: 1 -> 2 (递归)
# - B: 2 -> 3 (递归)
# - A：1 -> 2
# - B: 3 -> 2 (递归)
# - B: 2 -> 1 (递归)
# - A: 2 -> 3
# - B: 1 -> 2 (递归)
# - B: 2 -> 3 (递归)
# 对于n层(A)的移动，可以将上面n-1层看做B，n > 1
# 需要解决： B从不同位置移动

# ......