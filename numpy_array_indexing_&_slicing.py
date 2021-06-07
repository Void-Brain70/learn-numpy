# -*- coding: utf-8 -*-
"""NumPy_Array_Indexing_&_Slicing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h7ZS6WmPyj65ilxwlrRaN73zSQGGOypR

Access Array Elements
"""

#Array indexing
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a[3])

#Get third and fourth elements from the following array and add them.
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a[2] + a[3]) #a[2] = 3, a[3] = 4, 3+4=7

#2-D Arrays indexing
import numpy as np
a = np.array([[10,20,30],[70,73,79]])
print(a[1,1])

#3-D arrays indexing
import numpy as np
a = np.array([
              [[10,20,30],[70,73,79]],
              [[1,2,3],[4,5,6]]
            ])
print(a[1,1,1])
print(a[0,1,0])

#Negative Indexing
import numpy as np
a = np.array([[10,20,30],[70,73,79]])
print(a[1,-3])

"""NumPy Array Slicing

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].
"""

#Slice elements from index 2 to index 6 from the following array
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[2:6])

#Slice elements from index 3 to the end of the array
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[3:])

#Slice elements from the beginning to index 6 (not included)
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[:6])

#Negative Slicing

#Slice from the index 4 from the end to index 1 from the end

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[-4:-1])

#STEP

#Return every even other element from index 0 to index 11

import numpy as np
a = np.array([0,1,2,3,4,5,6,7,8,9,10])
print(a[0:11:2])

#Slicing 2-D Arrays

import numpy as np
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a[0,0:3])

#From both elements, return index 2

import numpy as np
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(a[0:2, 2])

#From both elements, slice index 1 to index 3 (not included), this will return a 2-D array

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:3])