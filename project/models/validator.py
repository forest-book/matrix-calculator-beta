import numpy as np

class Validator:
  
  @staticmethod
  def convert_to_npmatrix(matrix_str):
    tmp = matrix_str
    multiline_list = tmp.splitlines() #listになることで、何行あるかは分かる
    matrix_list = []
    for multiline in multiline_list:
        matrix_list.append([float(num) for num in multiline.split()])  # 各要素をfloatに変換
    try:
      matrix_np = np.array(matrix_list)
    except Exception as e:
      print(e)
      return e
    else:
      print(matrix_np)
      return matrix_np
