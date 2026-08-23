# List Comprehensions

## Task
Let's learn about list comprehensions! You are given three integers $x$, $y$, and $z$ representing the dimensions of a cuboid along with an integer $n$. Print a list of all possible coordinates given by $(i, j, k)$ on a 3D grid where the sum of $i + j + k$ is not equal to $n$. Here, $0 \le i \le x; 0 \le j \le y; 0 \le k \le z$. Please use list comprehensions rather than multiple loops, as a learning exercise.

## Input Format
Four integers $x, y, z,$ and $n$, each on a separate line.

## Constraints
Print the list in lexicographic increasing order.

## Sample Input 0
```text
1
1
1
2
```

## Sample Output 0
```text
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

## Explanation 0
Each variable $i, j,$ and $k$ will have values of $0$ or $1$. All permutations of lists in the form $[i, j, k]$ that do not sum to $2$ are printed.

## Sample Input 1
```text
2
2
2
2
```

## Sample Output 1
```text
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
```

---
