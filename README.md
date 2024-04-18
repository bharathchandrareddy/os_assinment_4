# os_assinment_4

This assignment focuses on three algorithms
1.LRU aloritm
2. optimal aloritm
3. FIFO algorithm

# LRU algorithm
The Least Recently Used (LRU) algorithm is a common page replacement strategy used in operating systems to manage memory, particularly in the context of virtual memory systems.
The LRU algorithm works under the premise of replacing the page in memory that has been used least recently when a new page needs to be loaded into memory, and there is no free space available.
This approach is based on the idea that pages that have been used most recently are likely to be used again soon, while those that have not been used for a long time may not be needed in the near future

# optimal algorithm
The Optimal algorithm operates under the premise of preemptively knowing the entire sequence of pages that will be requested in the future. Using this information, it decides which page to replace when a page fault occurs and there is no free space left in memory
The Optimal algorithm serves as a useful theoretical benchmark for studying memory management algorithms. It helps in understanding the potential limitations of practical algorithms and in measuring how far off from "optimal" they are.

# THe FIFO algorithm
The FIFO (First In, First Out) algorithm is a classical page replacement strategy used in operating systems to manage memory, particularly in virtual memory systems.
It's one of the simplest page replacement algorithms to understand and implement, functioning similarly to a basic queue structure.


# Explanation
**FIFO Algorithm**: This function simulates the First In First Out replacement method. Pages are added to a list until it's full, then pages are replaced in the order they were added.

**LRU Algorithm**: Least Recently Used pages are replaced first. This is implemented by moving a page to the end of the list each time it's referenced, which keeps recently used pages at the end and least recently used at the start.

**Optimal Algorithm**: This algorithm looks ahead in the input page list to decide which existing page in the memory will not be used for the longest period. It requires knowing the future requests and is typically used for comparative performance analysis as it is not implementable in typical systems without prior knowledge of the page request sequence.
Each function returns a list of descriptions of what happened at each step and the total number of page faults.

# steps to run this assignment
1. download the file
2. run the algorithm
3. you can observe the output in required format

# output
![image](https://github.com/bharathchandrareddy/os_assinment_4/assets/51413287/ced0d941-c9cf-466e-9140-5a349caf48fa)

![image](https://github.com/bharathchandrareddy/os_assinment_4/assets/51413287/8b5a4a20-02da-4fb9-8014-7e1881df9956)


