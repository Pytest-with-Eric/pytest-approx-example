# Introduction
As a Python developer striving for accurate and efficient testing, you will likely encounter scenarios where verifying floating-point values or approximate comparisons presents challenges. 

Precision matters, but so does practicality. This is where the "pytest approx" module comes into play. 

Just as software testing is vital for ensuring your code functions as intended, handling numerical approximations is crucial for maintaining robust test suites.

In this article, we will discuss what is pytest approx, its purpose, its functionality, and how it can alleviate the intricacies of dealing with floating-point approximations in your tests. 

<!-- More -->

We'll start with discussing the importance of precision in approximate testing and where pytest approx fit it.

Then we will discuss the syntax of pytest approx using some sample code and then move on to implementing pytest approx on complex data structures.

By examining this module, we aim to empower you with the knowledge needed to make informed decisions about incorporating "pytest approx" into your testing toolkit, ultimately enhancing the reliability of your Python projects.

Let's get started, shall we?

Link to GitHub repo

## Overview of Pytest
Pytest is a widely-used and highly flexible testing framework in the Python ecosystem. 

It offers a simple and intuitive approach to writing and executing tests, making it a preferred choice for developers seeking efficient testing solutions. 

Its extensive plugin ecosystem further enhances its capabilities, enabling developers to tailor their testing workflow to specific project needs. 

Whether you're a beginner or an experienced developer, Pytest's user-friendly design and robust functionality make it a versatile tool for ensuring the reliability and quality of Python code. Make sure to visit the [homepage](https://pytest-with-eric.com/) to explore more about pytest!

## Importance of Approximations in Testing

Let's consider a financial application responsible for calculating interest rates on loans. The precision of these calculations directly impacts the financial decisions of both institutions and individuals. 

Imagine a scenario where the application reports slightly inaccurate interest rates for specific loan terms because it couldn't handle floating-point approximations effectively. 

These minute discrepancies might seem trivial on the surface, but they can accumulate over time, potentially leading to significant financial differences for borrowers and lenders alike.

As you can see in this context, the importance of approximations in testing becomes evident. Without a robust mechanism to account for slight variations in floating-point calculations, the testing process could fail to pinpoint these subtle inaccuracies. 

As a result, test cases might pass when they shouldn't, giving a false sense of security that the application is functioning correctly. 

You need to acknowledge the critical role of approximations in testing and implement solutions like the "pytest approx" module to strike a balance between precision and practicality. 

## What problem does Pytest Approx solve?

Minor discrepancies can arise due to the inherent nature of floating-point representation, though small, can lead to failed test cases or false positives. 

Pytest Approx offers a solution by allowing developers to assert approximate equality, meaning that values are considered equal as long as they are within a specified tolerance of each other. 

This approach acknowledges the practical need for slight variations in calculations while ensuring that tests remain effective and reliable. 

Rather than unpacking floating-point numbers during calculation or approximate comparison, you can go for a neater and more effective method of pytest approx.

## Objectives
By the end of this tutorial, you should be able to:

- Understand the importance of approximations in testing and the potential challenges they pose.

- Understand the purpose of Pytest Approx in accommodating acceptable differences in calculations.

- Familiarize yourself with the syntax of Pytest Approx.

- Debug any `TypeError` for certain comparisons.

- Implement approximation techniques for lists, arrays, dictionaries, and nested data structures.

- Compare Pytest Approx with other approximation modules like Numpy's `assert_allclose`.

# Prerequisites
The project has the following structure: (I'll add with the final touches)

To get started, clone the repo here, or you can create your own repo by creating a folder and running `git init` to initialise it.

## Set-up and Installations
In this project, we’ll be using Python 3.10. 

All you need is Python 3.10, an IDE, and pytest framework installed in your local machines

If you don't already have these installed, then read this [step-by-step guide](https://pytest-with-eric.com/introduction/how-to-run-pytest-in-vscode/) to set up your pyest module!

## Understanding Tolerance Levels
Understanding tolerance levels is crucial when dealing with numerical approximations in testing. 

Tolerance determines the acceptable deviation between two numbers for them to be considered practically equal. 

Imagine you're a chef following a recipe to bake a cake. The recipe calls for 1 cup of flour and 2/3 cup of sugar. However, due to variations in measuring techniques and ingredient densities, your cup of flour might not be the exact same size as the author's cup, and the amount of sugar might not be perfectly aligned with the intended measurement.

In this baking scenario, the concept of tolerance becomes relevant. A small variation in the amount of flour or sugar might not drastically affect the final cake's taste or texture. As long as the measurements are close enough, the cake is likely to turn out delicious. 

Applying this idea to software testing, tolerance levels allow us to consider two numbers as "close enough" to be treated as equal, accommodating minor discrepancies that don't impact the overall functionality of the code.

# Basic Use of Pytest Approx
Now we will implement the functionality of pytest approx. Let's discuss the syntax and semantic of this function before we jump into it's more complex implementations.

## Syntax of Pytest Approx
The syntax for using the "pytest approx" functionality in Pytest is quite straightforward. You can use it to perform approximate comparisons between numerical values, accounting for the inherent imprecision of floating-point calculations. 

Here's the basic syntax:

    assert actual_value == pytest.approx(expected_value, rel=relative_tolerance, abs=absolute_tolerance)

-   `actual_value`: The computed value that you want to test.
-   `expected_value`: The expected value that the `actual_value` should be approximately equal to.
-   `rel`: (Optional) Relative tolerance as a float. Specifies the relative tolerance level for the comparison.
-   `abs`: (Optional) Absolute tolerance as a float. Specifies the absolute tolerance level for the comparison.

Both `rel` and `abs` are optional arguments, and you can choose to use one or both of them depending on your testing requirements. 

The `pytest.approx` function will perform the comparison and determine whether the `actual_value` is within the specified tolerances of the `expected_value`.

## Example code to test Pytest Approx
Here's a simple example to implement pytest approx:
(path to test_python_approx_1.py)

    import  pytest
    
    def  divide(a, b):
       return  a  /  b
    
    def  test_exact_comparison():
	   result  =  divide(1, 3)
	   assert  result  ==  0.3333333333333333  # Exact value
  
    def  test_approximate_comparison():
	   result  =  divide(1, 3)
	   assert  result  ==  pytest.approx(0.3333333333333333) # Approximate value

    @pytest.mark.xfail(reason="This test is currently expected to fail")
    
    def  test_approximation_failure():
		result  =  divide(1, 3)
		assert  result  ==  pytest.approx(0.333) # This test will fail due to approximation

1.  **test_exact_comparison**: Comparing the result of the `divide(1, 3)` function call, which computes `1 / 3`, with the exact value `0.3333333333333333`. Since the comparison is exact, the test passes.
    
2.  **test_approximate_comparison**: This test also compares the result of `divide(1, 3)` with the value `0.3333333333333333`, but this time using `pytest.approx`. This test passes because `pytest.approx` considers the small variations due to floating-point imprecision.
    
3.  **test_approximation_failure**: Here we compare the result of `divide(1, 3)` with the value `0.333` using `pytest.approx`. This test is marked as expected to fail (`@pytest.mark.xfail`) because the approximation tolerance (`0.01` by default) is too strict, and the floating-point imprecision exceeds this tolerance. Therefore, this test does fail as expected.

## Tedious method to assert that two floating-point numbers are equal

Imagine having to do multiple floating-point number comparison using the traditional method, like this:

    assert  abs(result - expected_result) < 1e-6

Now, imagine using the more flexible pytest approx approach:

    assert result == pytest.approx(expected_result, abs=1e-6, rel=1e-9)

You will soon realize that traditional method is both cumbersome and less reliable. The lack of a universally applicable tolerance value makes it problematic, as varying scenarios might necessitate different tolerances to account for precision variations.

Absolute comparisons struggle to address the inherent imprecision of floating-point arithmetic consistently. 

Recognizing this, Pytest offers a more flexible and recommended solution through the "pytest.approx" module. 

Its approach is better suited to handling the challenges posed by floating-point comparisons, promoting accuracy and reducing the likelihood of false negatives or positives in test outcomes.

## How to handle the "TypeError" when testing Pytest Approx function?
When working with the Pytest Approx function, it's essential to handle the "TypeError" that can arise in certain comparisons. 

To ensure consistent behavior, Pytest raises a `TypeError` when using the comparison operators `>`, `>=`, `<`, and `<=` in conjunction with `pytest.approx`. 

These operators don't align well with the concept of tolerance-based comparisons, as they introduce ambiguity in deciding whether values are practically equal within the specified tolerances. 

To learn more about how to navigate this aspect of Pytest Approx refer to https://happytest-apidoc.readthedocs.io/en/latest/api/pytest/

# Different Approaches to Approximation 
Different approaches to approximation are needed to provide a flexible and adaptable way of comparing floating-point values in various testing scenarios.
We will use the following code snippet to elaborate the different approaches to approximation that are commonly used: 

(path to test_pytest_approx_2.py)

    import  pytest
    
    @pytest.mark.xfail(reason="This test is currently expected to fail")
    
    def  test_approx_syntax():
	    # Test case 1: Using default tolerance
	    actual_value_1  =  10.5
	    expected_value_1  =  10.0
	    assert  actual_value_1  ==  pytest.approx(expected_value_1)
	    
	    # Test case 2: Using relative tolerance
	    actual_value_2  =  200.0
	    expected_value_2  =  205.0
	    assert  actual_value_2  ==  pytest.approx(expected_value_2, rel=0.02)
	    
	    # Test case 3: Using absolute tolerance
	    actual_value_3  =  15.0
	    expected_value_3  =  15.5
	    assert  actual_value_3  ==  pytest.approx(expected_value_3, abs=0.6)
	    
	    # Test case 4: Handling NaN values
	    nan_value  =  float("nan")
	    assert  nan_value  ==  pytest.approx(nan_value, nan_ok=True)

	    # Test case 5: Using custom error message
	    actual_value_5  =  3.14159
	    expected_value_5  =  3.14
	    assert  actual_value_5  ==  pytest.approx(expected_value_5, abs=0.01, msg="Values not approximately equal")

## Absolute Tolerance: 
Developers can set an absolute tolerance level to accept results within a certain range, ignoring minor differences.
    
## Relative Tolerance: 
Relative tolerance allows for variations relative to the magnitude of the values being compared. This approach is useful for testing large and small values together.
    
## Scaling Factors: 
Pytest Approx supports applying scaling factors to adjust tolerances dynamically based on the input data.
    
##  Using Custom Comparators: 
Developers can define custom comparators for specific data types or classes, allowing fine-grained control over the approximation process. This approach offers flexibility in managing complex data structures or unique situations where standard tolerance levels may not suffice

# Handling Complex Data Structures with Pytest Approx
Pytest Approx provides a robust solution for accurate testing. Whether it's lists, arrays, dictionaries, or nested data, Pytest Approx ensures that the intricacies of floating-point approximations don't compromise your testing.

## Approximating Lists and Arrays
When comparing a list of calculated values with expected results, Pytest Approx simplifies the process, allowing you to assert approximate equality without manually addressing each element's precision. 

Similarly, when you are comparing arrays you can employ `pytest.approx` to verify their equality within specified tolerances.

Let's look at an example of how array calculation is handled precisely using pytest approx:
(path to test_pyest_approx_3.py)

    import  pytest
    import numpy as  np

    # Function to calculate the element-wise square of a list or array
    def  calculate_square_elements(data):
	    return [x  **  2  for  x  in  data]

    def  test_list_comparison():
	    expected_result  = [1, 4, 9, 16]
	    input_data  = [1, 2, 3, 4]
	    calculated_result  =  calculate_square_elements(input_data)
	    assert  calculated_result  ==  pytest.approx(expected_result)

    def  test_numpy_array_comparison():
	    expected_result  =  np.array([0.1, 0.2, 0.3])
	    input_data  =  np.array([0.31622776601683794, 0.4472135954999579, 0.5477225575051661])
	    calculated_result  =  calculate_square_elements(input_data)
	    assert  calculated_result  ==  pytest.approx(expected_result, abs=1e-6)

Both tests demonstrate how `pytest.approx` can be used to handle numerical comparisons, even when dealing with arrays or lists that might have slight variations due to floating-point precision. 

This approach ensures accurate testing without being overly strict in requiring exact matches.

## Approximating Dictionaries 
For dictionaries, Pytest Approx handles key-value pairs with precision. 

In scenarios where you're comparing calculated dictionary values with expected outcomes, Pytest Approx lets you assert approximate equality while accounting for floating-point discrepancies.

## Python Approx and NaN entries
Pytest Approx also handles special cases like NaN (Not-a-Number) entries. When dealing with situations where calculations might yield NaN values, Pytest Approx ensures that comparisons remain accurate even in such scenarios.

# Use Cases of Pytest Approx
You are all now well familiar with the versatitality of Pytest approx and how it is used for a variety of testing scenarios where precise numerical comparisons are challenging due to floating-point imprecision. From scientific calculations, to numerical libraries and regression testing, you can use Pytest Approx anywhere!
## What is the difference between `approx` and `assert_approx_equal`? 
The `approx` function in Pytest is used within assertions to check if values are approximately equal. 

On the other hand, `assert_approx_equal` is used to explicitly assert the equality between two values using `pytest.approx`. 

The distinction lies in how the tests are expressed. The pytest appprox module is more succinct and follows the pattern of other Pytest assertions, while the other method provides a more direct way to assert the approximation.

Let's look at an example to better understand the difference:
(path to test_pytest_approx_4.py)

    import  pytest
    import numpy as  np

    def  divide(a, b):
	    return  a  /  b

    def  test_pytest_approx():
	    result  =  divide(1, 3)
	    assert  result  ==  pytest.approx(0.3333333333333333)

    def  test_assert_approx_equal():
	    result  =  divide(1, 3)
	    np.testing.assert_approx_equal(result, 0.3333333333333333, significant=6)

This code comprises two test functions that verify the behavior of the `divide` function using different approaches for approximate comparisons.

The first test uses the Pytest framework's built-in `pytest.approx` function, while the second test utilizes NumPy's `assert_approx_equal` function to achieve the same outcome.

## How to handle dynamic or changing data in approx tests?
When dealing with dynamic data, like timestamps or computed values, it's essential to incorporate appropriate tolerances that account for variability. This prevents false test failures due to slight fluctuations in the data.
## Can I use Pytest Approx with non-numeric data types?
Pytest Approx is designed for numerical comparisons and is not suitable for non-numeric data types. Attempting to use it with non-numeric data can lead to unexpected behavior or errors.

## Pytest Approx vs. Numpy's `assert_allclose`
While both Pytest Approx and Numpy's `assert_allclose` serve similar purposes, they differ in syntax and ecosystem integration. 

Numpy's function is more focused on NumPy arrays and offers additional options, while Pytest Approx provides a unified approach for all data types and integrates seamlessly with the Pytest framework.

We will look at a sample code to highlight the difference in syntax of both these methods:

    import  pytest
    import numpy as  np

    # A function that calculates the square root of a number
    def  calculate_square_root(x):
	    return  np.sqrt(x)

    def  test_pytest_approx():
	    result  =  calculate_square_root(2)
	    expected_result  =  1.41421356
	    assert  result  ==  pytest.approx(expected_result, rel=1e-5)

    def  test_numpy_assert_allclose():
	    result  =  calculate_square_root(2)
	    expected_result  =  1.41421356
	    np.testing.assert_allclose(result, expected_result, rtol=1e-5)
The above code, as you can see, consists of two test functions that assess the behavior of the `calculate_square_root` function using different techniques for approximate comparisons. 

You will notice that both these methods produce the same result and the test cases will pass.

## Limitations of Pytest Approx
While Pytest Approx is powerful, it's important to note its limitations. It might not be suitable for all scenarios, especially when dealing with extremely small or large numbers where relative tolerances can become impractical. 

As you might have read above, it's also not designed for comparisons involving non-numeric data types.

## Floating Point Arithmetic: Issues and Limitations
Floating-point numbers are encoded in computer hardware using base 2 (binary) fractions. 
You know that the decimal fraction 0.125 can be written as 1/10 + 2/100 + 5/1000. Similarly, the binary fraction 0.001 corresponds to 0/2 + 0/4 + 1/8. 

Do you notice a difference in both the above representations? Well, the key distinction lies in the representation: the first employs base 10 fractional notation, while the second employs base 2.

As you may already know that the majority of decimal fractions cannot be precisely represented as binary fractions. Consequently, the decimal floating-point numbers you input are inherently approximated by the binary floating-point numbers stored within the machine.

This issue is easier to grasp when considered in base 10. Take the example of the fraction 1/3. It can be approximated in base 10 as follows:
0.3, or 0.33 or even better 0.333 and so on.

Irrespective of the number of digits you employ, the outcome will never be an exact match for 1/3; instead, it will perpetually improve as a closer approximation of 1/3. 

Just remember, even though the printed result may look somewhat similar to 1/3, the actual stored value is the nearest representable binary fraction.

# Conclusion and Learnings
After reading the article, you agree with me when I say that Pytest Approx's benefits are multifaceted. It will help you to validate floating-point calculations without being hindered by minute numerical differences, thus preventing unnecessary test failures. 

The framework's simplicity and integration within the Pytest ecosystem streamline the testing process, fostering more efficient and dependable test suites.

Conclusively, by understanding and applying the various strategies offered by Pytest Approx, you can bolster the effectiveness of their tests, ultimately contributing to the stability and quality of their software projects.

# Additional Learning
https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest-approx
https://happytest-apidoc.readthedocs.io/en/latest/api/pytest/
https://docs.python.org/3/library/unittest.html







