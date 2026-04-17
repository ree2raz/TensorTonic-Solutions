def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    if len(recommendations) == 0: return 0.0
    hit_count = 0
    for user_idx in range(len(recommendations)):
        if recommendations[user_idx] and ground_truth[user_idx] and ground_truth[user_idx][0] in recommendations[user_idx][:k]:
            hit_count += 1
    return hit_count / len(recommendations)
            
        