import TkEasyGUI as eg
import numpy as np

from models.matrix import CalcMatrix

#print(eg.get_tnemes())
eg.theme("default")

input_frame = [eg.Frame("Input Matrix", [
    [eg.Multiline(size=(30, 20), key="-Matrix-"), eg.Button("calculate")]
], font=("Monospace 18"))]

result_frame = [eg.Frame("matrix calculate result", [
    [eg.Text("inverse"), eg.Text("", key="-Inverse-")],
    [eg.Text("transpose"), eg.Text("", key="-Transpose-")],
    [eg.Text("determinant"), eg.Text("", key="-Determinant-")],
    [eg.Text("eigenvalues"), eg.Text("", key="-Eigenvalues-")],
    [eg.Text("rank"), eg.Text("", key="-Rank-")],
    [eg.Text("diag"), eg.Text("", key="-Diag-")]
], font=("Monospace 18"))]

layout = [
    input_frame,
    result_frame
]

window = eg.Window("Hello App", layout)
calculator = CalcMatrix()

while True:
    event, values = window.read()
    
    if event == eg.WIN_CLOSED:
        eg.popup("close")
        break
    
    if event == "calculate":
        tmp = values["-Matrix-"]
        multiline_list = tmp.splitlines() #listになることで、何行あるかは分かる
        matrix_list = []
        for multiline in multiline_list:
            #print(multiline.split())
            #matrix_list.append(multiline.split())
            matrix_list.append([float(num) for num in multiline.split()])  # 各要素をfloatに変換
        matrix_np = np.array(matrix_list)
        #print(matrix_np)

        #行列計算処理
        inverse_result = calculator.calculate_inverse(matrix_np)
        transpose_result = calculator.calculate_transpose(matrix_np)
        determinant_result = calculator.calculate_determinant(matrix_np)
        eigenvalues_result = calculator.calculate_eigenvalues(matrix_np)
        rank_result = calculator.calculate_rank(matrix_np)
        diag_result = calculator.calculate_diag(matrix_np)

        #print(inverse_result)
        #print(matrix_list)
        #print("-----")
        #print(type(matrix_np))
        #print(matrix_np.shape)
        eg.popup("done calculation")
        #結果をGUIに反映
        window["-Inverse-"].update(str(inverse_result))
        window["-Transpose-"].update(str(transpose_result))
        window["-Determinant-"].update(str(determinant_result))
        window["-Eigenvalues-"].update(str(eigenvalues_result))
        window["-Rank-"].update(str(rank_result))
        window["-Diag-"].update(str(diag_result))
    
window.close()