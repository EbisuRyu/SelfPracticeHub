def max_sliding_window(num_list: list, window_size: int):
    """
    Calculate the maximum value in each sliding window of the given size over the num_list.
    
    Args:
    num_list (list): List of integers over which the sliding window will move.
    window_size (int): Size of the sliding window.
    
    Returns:
    list: A list of the maximum values in each sliding window.
    """
    # Initialize an empty list to store the maximum values for each window
    window_max_value = []

    # Loop through the list from the start to the point where the window can fully fit
    for index in range(0, len(num_list) - window_size + 1):
        # Find the maximum value in the current window
        max_value = max(num_list[index:index + window_size])
        # Append the maximum value to the result list
        window_max_value.append(max_value)
    
    return window_max_value

# Test Cases:
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
window_size = 3
print(max_sliding_window(num_list, window_size))  # Output: [5, 5, 5, 10, 12, 33, 33])