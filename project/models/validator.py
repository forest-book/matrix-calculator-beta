import numpy as np

class Validator:
  
  @staticmethod
  def convert_to_npmatrix(matrix_str):
    tmp = matrix_str
    multiline_list = tmp.splitlines() #listになることで、何行あるかは分かる
    matrix_list = []
    for multiline in multiline_list:
        #print(multiline.split())
        #matrix_list.append(multiline.split())
        matrix_list.append([float(num) for num in multiline.split()])  # 各要素をfloatに変換
    matrix_np = np.array(matrix_list)
    print(matrix_np)
    return matrix_np
