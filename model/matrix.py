import numpy as np

matrix = np.array([[1, 2], [0, 2]])

# 逆行列の計算
def calculate_inverse(matrix):
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return "逆行列が存在しない行列です。"
    
# 転置行列の計算
def calculate_transpose(matrix):
    return matrix.T
    
print("\n逆行列:")
print(calculate_inverse(matrix))

print("\n転置行列:")
print(calculate_transpose(matrix))