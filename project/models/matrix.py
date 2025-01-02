import numpy as np

matrix = np.array([[1, 2], [0, 2]])


class CalcMatrix:
    # 逆行列の計算
    @staticmethod
    def calculate_inverse(matrix):
        try:
            return np.linalg.inv(matrix)
        except np.linalg.LinAlgError:
            return "逆行列が存在しない行列です。"
        except Exception as e:
            print(e)

    # 転置行列の計算
    @staticmethod
    def calculate_transpose(matrix):
        return matrix.T

    # 行列式の計算
    @staticmethod
    def calculate_determinant(matrix):
        return np.linalg.det(matrix)

    # 固有値の計算
    @staticmethod
    def calculate_eigenvalues(matrix):
        try:
            eigenvalues, _ = np.linalg.eig(matrix)
            return eigenvalues
        except np.linalg.LinAlgError:
            return "固有値の計算に失敗しました。"

    # ランクの計算
    @staticmethod
    def calculate_rank(matrix):
        return np.linalg.matrix_rank(matrix)

    #対角行列
    @staticmethod
    def calculate_diag(matrix):
        return np.diag(matrix)


# print("\n逆行列:")
# print(calculate_inverse(matrix))

# print("\n転置行列:")
# print(calculate_transpose(matrix))

# print("\n行列式:")
# print(calculate_determinant(matrix))

# print("\n固有値:")
# print(calculate_eigenvalues(matrix))

# print("\nランク:")
# print(calculate_rank(matrix))

# print("\n対角行列:")
# print(calculate_diag(matrix))