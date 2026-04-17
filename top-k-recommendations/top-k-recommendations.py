def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    scores_with_index = [(x, i) for i, x in enumerate(scores)]
    rated_set = set(rated_indices)
    candidates = [(score, i) for i, score in enumerate(scores) if i not in rated_set]
    if len(set(s for s, _ in candidates)) == 1:
      unrated_scores = candidates
    else:
      unrated_scores = sorted(candidates, reverse=True)
    answer = [i[1] for i in unrated_scores]
    return answer if len(scores) < k else answer[:k]