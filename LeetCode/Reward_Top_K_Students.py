# Leetcode
# https://leetcode.com/problems/reward-top-k-students/

import heapq

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_words = set(positive_feedback)
        negative_words = set(negative_feedback)
        score = []
        for item, student in zip(report, student_id):
            curr_score = 0
            for word in item.split():
                if word in positive_words:
                    curr_score += 3
                if word in negative_words:
                    curr_score -= 1
            score.append((-curr_score, student))
        heapq.heapify(score)
        return [i[1] for i in heapq.nsmallest(k, score)]