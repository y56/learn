# Software Engineer Coding Challenge

For rendered Markdown, please read
https://hackmd.io/@y56/B1fDgAu3r

## Question 1: Complexity of `binarytree.printtree()`

### Time

The time complexity is $\Theta(n)$, where $n$ is the number of nodes in the tree (which is also the number of times executing the while-loop).

### Space

The space complexity is $O(n)$, where $n$ is the number of nodes in the tree.

The maximum memory usage occurs when the length of `fifoqueue` reach its peak. This happens when the function is printing/about to print the level with most nodes.

Recall that for a complete tree with $n$ nodes, the number of nodes in the deepest full level is $2^{\lfloor log(n+1) \rfloor - 1}$.

Also, for a tree with $n$ nodes to have a maximum number in a single level, we shall construct the tree to be complete, and the desired level will be either the deepest full level or the deepest level. 

So the maximum number of nodes in one level is between $2^{\lfloor log(n+1) \rfloor - 1}$ and $2^{\lfloor log(n+1) \rfloor}$. Since ${\lfloor log(n+1) \rfloor \leq log(n+1) }$, it is safe to remove the floor function in big-O notation. Finally, the space complexity is $O(\frac{n+1}{2}) = O(n+1)=O(n)$ 

#### Example 1
```
      [1]
  [2]     [3]
[4] [5] [6]
```
Max length of `fifoqueue` is 3, when the function is about to print `[4]`.
#### Example 2
```
             [1]
      [2]           [3]
  [4]     [5]     [6] [7]
[8][9]  [10][11]
```
Max length of `fifoqueue` is 6, , when the function is about to print `[6]`. Note that the max number of nodes in one level is 4. 

## Question 2: Complexity of `binarysearch.binarysearch()`

### Time

The time complexity is $O(log(n))$.

The worst-case happens when we have to go to the deepest level of the binary search tree. 
The best case happens when we find the target in the first middle position.

### Space

The space complexity is $O(log(n))$. 



Each function call will grow the OS stack. Fortunately, in each call, sizes of all local variables and pointers are constant to the input size.

Since Python is [pass-by-object-reference](https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/), `sortedlist` and `target` in `binarysearchhelper()` are passed by reference in recursive calls and will only need space for references in the stack for a single function call. However, new indices `mid` and `mid+1` as new `low` (or `mid-1` as new `high`) do need new extra (but constant) space in memory (which is outside the stack) in each recursive call. To sum up, the space complexity is still determined by the number of calls. It is $O(log(n))$.

We can run `space_binarysearch.py` to look at memory usage.




## Style for Python Code

PEP8

## Environment 

Python 3.6.8

## Unit Test

Run

`python3 -m unittest test_binarytree`  
`python3 -m unittest test_binarysearch`

Or to be verbose,

`python3 -m unittest -v test_binarytree`  
`python3 -m unittest -v test_binarysearch`

### Reference
https://docs.python.org/3.6/library/unittest.html
