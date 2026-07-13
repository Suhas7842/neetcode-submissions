from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Quick check: if hand cannot be divided evenly into groups, return False
        if len(hand) % groupSize != 0:
            return False
        # Step 1: Count frequency of each card
        card_counts = Counter(hand)
        # Step 2: Sort the unique cards to process from smallest to largest
        unique_cards = sorted(card_counts.keys())
        # Step 3: Iterate and try to form groups
        for card in unique_cards:
            count = card_counts[card]
            if count > 0:
                # This card must start 'count' number of groups
                for i in range(groupSize):
                    next_card = card + i
                    # If any required consecutive card doesn't have enough count, fail
                    if card_counts[next_card] < count:
                        return False     
                    # Deduct the used cards from our inventory
                    card_counts[next_card] -= count 
        return True