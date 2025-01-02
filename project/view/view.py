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
    [eg.Text("transpose"), eg.Text("", key="-Transpose-")]
], font=("Monospace 18"))]

layout = [
    input_frame,
    result_frame
]

window = eg.Window("Hello App", layout)

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
            print(multiline.split())
            matrix_list.append(multiline.split())
        matrix_np = np.array(matrix_list)

        inverse_result = CalcMatrix.calculate_inverse(matrix_np)
        #print(matrix_list)
        #print("-----")
        #print(type(matrix_np))
        #print(matrix_np.shape)
        eg.popup("input")
        window["-Inverse-"].update(str(matrix_np))
    
window.close()