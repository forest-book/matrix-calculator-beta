import TkEasyGUI as eg

eg.theme("default")

class Interface:
    def __init__(self):
        self.input_frame = [eg.Frame("Input Matrix", [
                [eg.Multiline(size=(30, 20), key="-Matrix-"), eg.Button("calculate", key="-Calculate-")]
            ], font=("Monospace 18"))]
        
        self.result_frame = [eg.Frame("matrix calculate result", [
                [eg.Text("inverse"), eg.Text("", key="-Inverse-")],
                [eg.Text("transpose"), eg.Text("", key="-Transpose-")],
                [eg.Text("determinant"), eg.Text("", key="-Determinant-")],
                [eg.Text("eigenvalues"), eg.Text("", key="-Eigenvalues-")],
                [eg.Text("rank"), eg.Text("", key="-Rank-")],
                [eg.Text("diag"), eg.Text("", key="-Diag-")]
            ], font=("Monospace 18")), eg.Button("hoge", key="-ExitApp-")]
        
        self.layout = [
                self.input_frame,
                self.result_frame
            ]
        
        self.window = eg.Window(title="Matrix Calculator", layout=self.layout)

    def close(self):
        self.window.close()