from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count character frequencies
        freq = Counter(s)
        
        # Sort characters by frequency (descending)
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        # Build result string
        # result = ""
        # for char, count in sorted_chars:
        #     result += char * count
        
        return sorted_chars
