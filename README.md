# Day-54-Sum-of-Factorial-Series

Day 54/100 - Python Program to Find Sum of Series 1/1!+1/2!+1/3!....1/N!

# Find Sum of Factorial Series

A program to calculate the cumulative sum of a mathematical series involving the reciprocals of factorials up to a user-defined integer $N$.

## 📝 Description

This program computes the sum of the specific series: $1/1! + 1/2! + 1/3! + \dots + 1/N!$.

To handle the complex math efficiently, it imports Python's built-in `math` module, utilizing the `math.factorial()` function to rapidly determine the denominator for each term. The core logic lives in the `sum_of_series(n)` function, which initializes a `total_sum` at `0` and employs a `for` loop to iterate from $1$ up to $N$ (`range(1, n + 1)`). During each step, it calculates $1$ divided by the factorial of the current index `i`, adding the result to the running total.

Additionally, the script features robust input validation. It uses a `try-except` block to intercept non-numeric `ValueError` exceptions, and explicitly checks if the entered integer is less than or equal to $0$ to ensure only valid, positive numbers are processed. The final sum is then formatted to precisely six decimal places.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A single positive integer $N$ provided via terminal prompt.



### Output:

* If valid: A formatted string stating: "The sum of the series for N = [N] is: [result]".


* If invalid (zero or negative): "Please enter a positive integer.".


* If invalid (non-numeric): "Invalid input! Please enter a positive integer.".



### Rules:

1. The program must prompt the user for an input and cast it to an integer inside a `try` block.


2. The program must catch any `ValueError` and print the designated error message.


3. The driver code must evaluate if $N \le 0$; if true, it must reject the input and bypass the calculation.


4. Valid inputs must be passed to the `sum_of_series(n)` function.


5. Inside the function, iterate from $1$ to $N$, computing $1 / \text{math.factorial}(i)$ and accumulating the values.


6. Return the total and print it formatted to 6 decimal places (`{result:.6f}`).



---

## 💡 Examples

### Example 1 (Small Series)

**Input:**

```
2

```

**Output:**

```
The sum of the series for N = 2 is: 1.500000

```

**Explanation:** The program calculates $1/1! + 1/2!$. This translates to $1/1 + 1/2$, resulting in exactly $1.5$, which is padded with trailing zeros to meet the 6-decimal requirement.

### Example 2 (Approaching Euler's Number)

**Input:**

```
5

```

**Output:**

```
The sum of the series for N = 5 is: 1.716667

```

**Explanation:** The program computes $1/1! + 1/2! + 1/3! + 1/4! + 1/5!$. This is $1 + 0.5 + 0.166666... + 0.041666... + 0.008333...$, summing to approximately $1.716667$. (Mathematically, as $N$ approaches infinity, this specific series converges to $e - 1$).

### Example 3 (Negative Value Handling)

**Input:**

```
-3

```

**Output:**

```
Please enter a positive integer.

```

**Explanation:** Factorials for negative numbers are undefined in this context. The condition `if N <= 0:` successfully catches the negative input and halts execution, displaying the error message.

### Example 4 (String Error Handling)

**Input:**

```
ten

```

**Output:**

```
Invalid input! Please enter a positive integer.

```

**Explanation:** The text "ten" cannot be cast into an integer. The `try-except` structure intercepts the `ValueError`, preventing the Python script from crashing.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-54-Sum-of-Factorial-Series.git
cd sum-of-factorial-series

```

2. **Run the program**:

```bash
python main.py

```

Enter a positive integer when prompted to calculate the precise fractional sum of its factorial sequence.
