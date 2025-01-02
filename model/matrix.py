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
    
# 行列式の計算
def calculate_determinant(matrix):
    return np.linalg.det(matrix)

# 固有値の計算
def calculate_eigenvalues(matrix):
    try:
        eigenvalues, _ = np.linalg.eig(matrix)
        return eigenvalues
    except np.linalg.LinAlgError:
        return "固有値の計算に失敗しました。"


print("\n逆行列:")
print(calculate_inverse(matrix))

print("\n転置行列:")
print(calculate_transpose(matrix))

print("\n行列式:")
print(calculate_determinant(matrix))

print("\n固有値:")
print(calculate_eigenvalues(matrix))