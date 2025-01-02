import TkEasyGUI as eg

from models.matrix import CalcMatrix
from models.validator import Validator

class Presenter:
  def __init__(self, window: eg.Window):
    self.window = window
    self.calculator = CalcMatrix()
    self.validator = Validator()

  def get_npmatrix(self, values):
    data = values["-Matrix-"]
    npmatrix = self.validator.convert_to_npmatrix(data)
    return npmatrix

  def matrix_calc(self, matrix_np):
    inverse_result = self.calculator.calculate_inverse(matrix_np)
    transpose_result = self.calculator.calculate_transpose(matrix_np)
    determinant_result = self.calculator.calculate_determinant(matrix_np)
    eigenvalues_result = self.calculator.calculate_eigenvalues(matrix_np)
    rank_result = self.calculator.calculate_rank(matrix_np)
    diag_result = self.calculator.calculate_diag(matrix_np)
    results = {}
    results.update(inverse_result=inverse_result)
    results.update(transpose_result=transpose_result)
    results.update(determinant_result=determinant_result)
    results.update(eigenvalues_result=eigenvalues_result)
    results.update(rank_result=rank_result)
    results.update(diag_result=diag_result)
    #print(results)
    return results

  def update_view(self, results):
    self.window["-Inverse-"].update(str(results['inverse_result']))
    self.window["-Transpose-"].update(str(results['transpose_result']))
    self.window["-Determinant-"].update(str(results['determinant_result']))
    self.window["-Eigenvalues-"].update(str(results['eigenvalues_result']))
    self.window["-Rank-"].update(str(results['rank_result']))
    self.window["-Diag-"].update(str(results['diag_result']))

  def finish_popup(self):
    eg.popup("finish calculate")

  def calculate_event(self, values):
    matrix = self.get_npmatrix(values)
    results = self.matrix_calc(matrix)
    self.finish_popup()
    self.update_view(results)
    

  def hoge_event(self, _):
    eg.popup("hoge")