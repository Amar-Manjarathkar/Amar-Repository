def minProduct(arr, k):
    # Sort array in ascending order
    arr.sort()
    
    # Take the first k elements
    product = 1
    for i in range(k):
        product *= arr[i]
    
    return product

# Example usage
arr = [10, 2, 3, 5, 7]
k = 3
print(minProduct(arr, k))  # Output = 30  (2*3*5)
