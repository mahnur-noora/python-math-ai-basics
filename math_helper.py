# Simple Python Tool for Mathematical Logic & AI Fundamentals

def calculate_matrix_2x2_determinant(a, b, c, d):
    """Calculates the determinant of a 2x2 matrix: [[a, b], [c, d]]"""
    return (a * d) - (b * c)

def linear_activation_step(x, threshold=0):
    """Simulates a basic step function used in early artificial neural networks."""
    return 1 if x >= threshold else 0

if __name__ == "__main__":
    print("--- Matrix Determinant Calculator ---")
    det = calculate_matrix_2x2_determinant(4, 2, 1, 5)
    print(f"Determinant of [[4,2],[1,5]]: {det}")
    
    print("\n--- Basic AI Step Function ---")
    inputs = [-2.5, 0.0, 1.8]
    for val in inputs:
        print(f"Input: {val} -> Activated Output: {linear_activation_step(val)}")
