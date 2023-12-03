import random

class ABTest:
    def __init__(self, version_a, version_b):
        self.version_a = version_a
        self.version_b = version_b
        self.results = {'A': 0, 'B': 0}

    def run_test(self, user):
        chosen_version = random.choice(['A', 'B'])
        # Simulate user interaction
        user_experience = self.simulate_user_interaction(user, chosen_version)
        self.results[chosen_version] += user_experience

    def simulate_user_interaction(self, user, version):
        # Simulate interaction and return user experience score
        # For simplicity, returning a random score
        return random.randint(1, 10)

    def get_results(self):
        return self.results

# Example usage
if __name__ == "__main__":
    test = ABTest('Version A', 'Version B')
    for i in range(100):  # Simulate 100 users
        test.run_test(f'User {i+1}')
    print(test.get_results())
