def is_possible(books, n, m, curr_min):
    students_required = 1
    current_sum = 0

    for i in range(n):
        # If a single book has more pages than curr_min, it's not possible
        if books[i] > curr_min:
            return False
        
        # Check if adding this book to current student's allocation exceeds curr_min
        if current_sum + books[i] > curr_min:
            # Allocate books to next student
            students_required += 1
            current_sum = books[i]
            
            # If more students are required than available, return False
            if students_required > m:
                return False
        else:
            current_sum += books[i]

    return True

def find_min_pages(books, n, m):
    if n < m:
        return -1  # Not enough books to allocate one to each student

    total_pages = sum(books)
    start = max(books)
    end = total_pages
    result = float('inf')

    while start <= end:
        mid = (start + end) // 2
        
        if is_possible(books, n, m, mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1

    return result
