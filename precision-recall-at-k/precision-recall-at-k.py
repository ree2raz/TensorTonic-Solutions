def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    numerator = set(recommended[:k]).intersection(set(relevant))
    precision_k = len(numerator) / k
    recall_k = len(numerator) / len(relevant)

    return [precision_k, recall_k]