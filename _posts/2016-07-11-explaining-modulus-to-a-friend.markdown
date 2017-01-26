---
layout: post
title: 'Explaining modulus to a friend'
date: 2016-07-11
tags: ["Math"]
---

Last semester, a friend and I were taking Discrete Math (counting, sets, logic, etc.), and he asked me a question about how modulus worked with negative numbers. It took me a bit to come up with a good answer, and I think it provides a nice framework for understanding how that operation works as a whole, so here goes.

When someone’s asked to calculate $$a \bmod b$$ , they’re being asked what the remainder would be when dividing $$a$$ by $$b$$. For example, calculating $$7 \bmod 3$$ would be $$1$$, since $$3$$ can only “go into” $$7$$ twice, and there will be $$1$$ left over $$(7 - (3 * 2) = 1$$.

We can make this a little more mathematical (it comes in handy when extending this to negative numbers): when calculating $$a \bmod b$$, you’re trying to find the value $$c$$ such that $$c = a - (b * k)$$, where $$k$$ is the largest possible integer such that $$a$$ is greater than $$(b * k)$$.  Again, consider calculating $$7 \bmod 3$$: here, we’re trying to find the largest $$k$$ that when multiplied by $$3$$, is still less than $$7$$. If $$k = 3$$, then $$(b * k)$$ equals $$9$$, and $$7$$ is not greater than $$9$$. However, if $$k = 2$$, then $$(b * k)$$ equals $$6$$, and $$7$$ is greater than $$6$$.  Plugging this into our equation, we find that $$c = 7 - (3 * 2)$$, which means $$c$$ equals $$1$$.

To understand where that model came from, think about what divisibility means. If 2 numbers, $$a$$ and $$b$$ are divisible, it means that $$a / b$$ yields no remainder; in other words, there is some integer $$k$$ such that $$a = (b * k)$$. Using that same model, we can calculate the remainder of any division by taking $$a$ - (b * k)$$, since this tells us how far
$$a$$ was from $$b * k$$.

Now to answer the question: how do we calculate $$-a \bmod b$$? Our model remains the same; we’re still trying to find $$c$$ using the equation above, and $$k$$ should still be the largest possible integer so that $$-a > (b * k)$$.  The key is in this last expression; for a negative integer $$x$$ to be greater than another integer $$y$$, $$y$$ should be negative but have a larger absolute value. For example, $$-1$$ is larger than all the integers in the range $$-2$$ to $$-\infty$$, but all those numbers have a larger absolute value than $$1$$ ($$2  > 1, 3 > 1, … \infty > 1$$). With negative numbers, larger absolute values mean the number gets smaller – exactly the opposite of what happens with positive numbers.

Taking this into account, consider $$7 \bmod 3$$ versus $$-7 \bmod 3$$. The largest $$k$$ that can be multiplied by $$3$$ to be less than 7 is $$k = 2$$, giving us $$7 - (3 * 2) = 1$$. But the largest $$k$$ that can be multiplied by $$2$$ and be less than $$-7$$ is $$k = -3$$, since $$-7$$ is greater than $$-9$$ ($$-3 * 3$$), so our answer becomes $$-7 - (-3 * 3) = -7 - (-9) = -7 + 9 = 2$$.  From this, we can see that there is no shortcut like: calculate $$a \bmod b$$ and then multiply it by $$-1$$.

This is a lot of math to do a basic operation, so here’s a shortcut. When calculating $$a \bmod b$$, and $$a$$ is positive, you can simply find the closest multiple of $$b$$ that is still less than $$\lvert a \rvert$$(absolute value of $$a$$), call it $$d$$, and do $$a - d$$ to get your answer. When $$a$$ is negative however, you should still find the closest multiple of $$b$$ that is less than $$\lvert a \rvert$$, call it $$d$$, but then do $$a + (d + b)$$ to get your answer. This just comes from applying the above model.

You can also think of this in terms of going "under" and "over"; with $$a \bmod b$$, you’re going "under" $$\lvert a \rvert$$ to find $$k$$, and taking the difference $$a - (b * k)$$. With $$-a \bmod b$$, you’re going "over" $$\lvert a \rvert$$ to find $$k$$, and again taking the difference $$a - (b * k)$$.

Hopefully I managed to articulate all of that well!
