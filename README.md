 <h1 align="center">
<img src="https://raw.githubusercontent.com/numpy/numpy/main/branding/logo/primary/numpylogo.svg" width="300">
</h1><br>

<h2>What is Numpy?</h2>
 NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
NumPy stands for Numerical Python.


### Why use numpy?
In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
Arrays are very frequently used in data science, where speed and resources are very important.


<h1 align='center'>Overview of NumPy Features </h1>

**1. ndarray:** The core data structure of NumPy is the `ndarray` , which is a multi-dimensional array
object that provides efficient storage and operations for large data sets.

**2. Array** Creation: NumPy provides various functions for creating arrays (e.g., np.array() ,
`np.zeros()` , `np.ones()` , `np.arange()` , `np.linspace() )`.

**3. Array Manipulation:** You can reshape, transpose, slice, index, and concatenate arrays.

**4. Mathematical Operations:** NumPy provides mathematical functions like element-wise
operations, reductions (e.g., sum, mean, min, max), and broadcasting.

**5. Linear Algebra:** Includes matrix multiplication, determinants, eigenvalues, etc.

**6. Random Number Generation:** NumPy has functions to generate random numbers from various
distributions.

**7. Fourier Transforms:** Includes functions for discrete Fourier transforms and related operations.

**8. Integration with Other Libraries:** NumPy arrays are the backbone of many scientific computing
libraries, such as Pandas, SciPy, and TensorFlow.

### Key NumPy Modules and Functions:
#### 1. Array Creation
- `np.array() :` Create an array from a Python list or tuple.
- `np.zeros() :` Create an array filled with zeros.
- `np.ones() :` Create an array filled with ones.
- `np.full() :` Create an array filled with a specified value.
- `np.arange() :` Create an array with a range of values (like Python's range() ).
- `np.linspace() :` Create an array with a specified number of evenly spaced values.
np.random.random() : Generate an array of random floats in the range [0.0, 1.0].
#### 2. Array Operations
- `np.add()` , `np.subtract()` , `np.multiply()` , `np.divide() :` Element-wise arithmetic operations.
- `np.dot()` : Matrix multiplication.
- `np.sum()` , `np.mean()` , np.std() :` Basic aggregation functions.
- `np.reshape()` : Change the shape of an array without changing its data.
- `np.transpose() :` Transpose of an array.
- `np.concatenate()` ,` np.vstack()` , `np.hstack() :` Join arrays along different axes.
#### 3. Linear Algebra
- `np.linalg.inv() :` Matrix inverse.
- `np.linalg.det() :` Determinant of a matrix.
- `np.linalg.eig() :` Eigenvalues and eigenvectors of a matrix.
- `np.linalg.solve() :` Solve a system of linear equations.
#### 4. Statistical Functions
- `np.min()` , `np.max() :` Find the minimum and maximum values in an array.
- `np.median()` , `np.percentile() :` Median and percentile functions.
- `np.corrcoef() :` Compute the correlation coefficient matrix.
##### 5. Random Module
- `np.random.seed() :` Set the seed for the random number generator.
- `np.random.rand() :` Generate an array of random values between 0 and 1.
- `np.random.randint() :` Generate an array of random integers.
#### 6. FFT (Fast Fourier Transform)
`np.fft.fft() :` Compute the one-dimensional n-point discrete Fourier Transform.
`np.fft.ifft() :` Compute the inverse of the Fourier Transform.
#### 7. File I/O
- `np.save() :` Save an array to a binary file in .npy format.
- `np.load() :` Load an array from a binary .npy file.
### Official Documentation:
For the full and up-to-date NumPy documentation, you can visit the official NumPy website:
- **NumPy Documentation:** ( https://numpy.org/doc/stable/)

This site includes comprehensive explanations, tutorials, and example code for all NumPy functions,
classes, and modules.
### NumPy Quick Reference:
NumPy also provides a quick reference guide that can be handy for developers:
- **Quick Reference:** [NumPy Quickstart Tutorial](https://numpy.org/devdocs/user/quickstart.html)

This quickstart is a great resource for getting started with basic array creation and manipulation.




## For more informations

- **Website:** https://www.numpy.org
- **Documentation:** https://numpy.org/doc
- **Mailing list:** https://mail.python.org/mailman/listinfo/numpy-discussion
- **Source code:** https://github.com/numpy/numpy
- **Contributing:** https://www.numpy.org/devdocs/dev/index.html
- **Bug reports:** https://github.com/numpy/numpy/issues
- **Report a security vulnerability:** https://tidelift.com/docs/security
 

 
 
