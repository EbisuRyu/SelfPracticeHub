def calculate_f1_score(tp: int, fp: int, fn: int):
    """
    This function calculates Precision, Recall, and F1-score based on the number of true positives (tp),
    false positives (fp), and false negatives (fn).

    Args:
    tp (int): Number of true positives
    fp (int): Number of false positives
    fn (int): Number of false negatives

    Returns:
    int: Always returns 0, only to display the values of precision, recall, and f1-score
    """

    # Check condition 1: Parameters must be integers
    if not isinstance(tp, int):
        print('tp must be an integer')
        return 0
    if not isinstance(fp, int):
        print('fp must be an integer')
        return 0
    if not isinstance(fn, int):
        print('fn must be an integer')
        return 0

    # Check condition 2: Parameters must be greater than 0
    if (tp <= 0) or (fp <= 0) or (fn <= 0):
        print('tp, fp, and fn must be greater than 0')
        return 0

    # Calculate precision, recall, and f1-score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)

    # Print results
    print(f'Precision is {precision:.2f} \nRecall is {recall:.2f} \nF1-score is {f1_score:.2f}')
    return 0

# Test cases
calculate_f1_score(tp=2, fp=3, fn=4)
calculate_f1_score(tp='a', fp=3, fn=4)
calculate_f1_score(tp=2, fp='a', fn=4)
calculate_f1_score(tp=2, fp=3, fn='a')
calculate_f1_score(tp=2, fp=3, fn=0)
calculate_f1_score(tp=2.1, fp=3, fn=0)