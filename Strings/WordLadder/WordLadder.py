from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        print(all_combo_dict)

        queue = deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = set(beginWord)
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited.add(beginWord)
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []

        return 0