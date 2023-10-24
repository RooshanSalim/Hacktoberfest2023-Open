def exponential_search(array, target):
  """Searches for an element in a sorted array using exponential search.

  Args:
    array: A sorted array.
    target: The element to search for.

  Returns:
    The index of the target element in the array, or -1 if the element is not found.
  """

  # If the target element is present at the first location itself.
  if array[0] == target:
    return 0

  # Find range for binary search by repeated doubling.
  i = 1
  while i < len(array) and array[i] <= target:
    i *= 2

  # Call binary search for the found range.
  return binary_search(array, i // 2, min(i, len(array) - 1), target)


def binary_search(array, low, high, target):
  """Performs a binary search on the given array for the target element.

  Args:
    array: A sorted array.
    low: The lower bound of the search range.
    high: The upper bound of the search range.
    target: The element to search for.

  Returns:
    The index of the target element in the array, or -1 if the element is not found.
  """

  if high >= low:
    mid = (low + high) // 2

    # If the element is present at the middle itself.
    if array[mid] == target:
      return mid

    # If the element is smaller than the middle element, it can only be present
    # in the left subarray.
    elif array[mid] > target:
      return binary_search(array, low, mid - 1, target)

    # Else the element can only be present in the right subarray.
    else:
      return binary_search(array, mid + 1, high, target)

  else:
    # The target element is not found in the array.
    return -1


# Example usage:

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
target = 19

index = exponential_search(array, target)

if index != -1:
  print(f"The target element {target} is found at index {index}.")
else:
  print(f"The target element {target} is not found in the array.")
