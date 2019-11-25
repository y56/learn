# Assesment for 

## Naming Style

Follow PEP8.

## Environment 

Python 3.6.8

## To run unit test



## Complexity of `binarytree.printtree()`

### Time

The time complexity is $\Theta(n)$, where $n$ is the number of nodes in the tree (which is also the number of times executing the while-loop).

### Space

The space complexity is $O(n)$, where $n$ is the number of nodes in the tree.

The maximum memory usage occurs when the function is printing/about to print the level with most nodes.

Recall that for a complete tree with $n$ nodes, the number of nodes in the deepest full level is $2^{\lfloor log(n+1) \rfloor - 1}$.

Also, for a tree with $n$ nodes, the level having most nodes is either the deepest full level or the deepest level. 

So the maximum number of nodes is between $2^{\lfloor log(n+1) \rfloor - 1}$ and $2^{\lfloor log(n+1) \rfloor}$. Since ${\lfloor log(n+1) \rfloor \leq log(n+1) }$, it is safe to remove the floor function in big-O notation. Finally, the space complexity is $O(\frac{n+1}{2}) = O(n+1)=O(n)$ 

#### Example 1
```
      [1]
  [2]     [3]
[4] [5] [6] [7]
```
Max length of `fifoqueue` is 4
#### Example 2
```
             [1]
      [2]           [3]
  [4]     [5]     [6] [7]
[8][9]  [10][11]
```
Max length of `fifoqueue` is 6, while the max number of nodes in a level is 4. 





## Complextity of bunary search


