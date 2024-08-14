# 1342. Number of Steps to Reduce a Number to Zero

### Instructions, Examples & Constraints

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

#### Example 1:

Input: num = 14  
Output: 6  
Explanation:   
- Step 1) 14 is even; divide by 2 and obtain 7. 
- Step 2) 7 is odd; subtract 1 and obtain 6.
- Step 3) 6 is even; divide by 2 and obtain 3. 
- Step 4) 3 is odd; subtract 1 and obtain 2. 
- Step 5) 2 is even; divide by 2 and obtain 1. 
- Step 6) 1 is odd; subtract 1 and obtain 0.

#### Example 2:

Input: num = 8  
Output: 4  
Explanation:   
- Step 1) 8 is even; divide by 2 and obtain 4. 
- Step 2) 4 is even; divide by 2 and obtain 2. 
- Step 3) 2 is even; divide by 2 and obtain 1. 
- Step 4) 1 is odd; subtract 1 and obtain 0.

#### Example 3:

Input: num = 123  
Output: 12

### Constraints:

$0 <= num <= 10^6$

## My Solution:

- Initialize number of steps to 0
- While loop runs while current number > 0
- If num % 2 != 0, subtract 1 from num and increment steps by 1
- Else (num is even), divide num by 2 and increment steps by 1
- Loop breaks when num less than or equal to 0
- Return value of steps

### Time Complexity:

$O(log(n))$

### Space Complexity:

$O(1)$
