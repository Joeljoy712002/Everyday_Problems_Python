# Question: Allocate Minimum Pages Challenge

    Given that there are N books and M students. Also given are the number of pages in each book in ascending order. The task is to
    assign books in such a way that the maximum number of pages assigned to a student is minimum, with the condition that every student 
    is assigned to read some consecutive books. Print that minimum number of pages.

### Task

Write a Python program that:
- Takes a list of integers `books` where each integer represents the number of pages in a book.
- Takes two integers `n` (the number of books) and `m` (the number of students).
- Allocates books to students such that the maximum number of pages assigned to a student is minimized.
- Returns the minimized maximum number of pages.


### Constraints

- Ensure the program handles cases where the number of books is less than the number of students by returning -1.
- The program should efficiently find the optimal way to allocate books using a binary search approach on the possible number of pages.
- Ensure the program handles edge cases such as books with a very large number of pages or scenarios where each student must receive at least one book.

### Note

The function `is_possible(books, n, m, curr_min)` helps in determining if a given maximum page allocation (`curr_min`) is feasible with `m` students.


