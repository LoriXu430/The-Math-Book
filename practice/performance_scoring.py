class PerformanceScorer:
    def __init__(self):
        self.scores = []

    def evaluate(self, system_output, ground_truth):
        score = self.calculate_score(system_output, ground_truth)
        self.scores.append(score)
        return score

    def calculate_score(self, system_output, ground_truth):
        # Implement scoring logic here
        # For simplicity, returning a random score
        return random.uniform(0, 100)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

# Example usage
if __name__ == "__main__":
    scorer = PerformanceScorer()
    for i in range(10):  # Simulate 10 evaluations
        scorer.evaluate('system output', 'ground truth')
    print(f'Average Score: {scorer.get_average_score()}')
