import TkEasyGUI as eg

eg.theme("default")

class Interface:
    def __init__(self):
        self.input_frame = [eg.Frame("Input Matrix", [
                [eg.Multiline(size=(30, 20), key="-Matrix-", font=("Monospace 12")), eg.Button("calculate", key="-Calculate-")]
            ], font=("Monospace 18"))]
        
        self.result_frame = [eg.Frame("matrix calculate result", [
                [eg.Text("inverse", font=("Monospace 12")), eg.Text("", key="-Inverse-", font=("Monospace 12"))],
                [eg.Text("transpose", font=("Monospace 12")), eg.Text("", key="-Transpose-", font=("Monospace 12"))],
                [eg.Text("determinant", font=("Monospace 12")), eg.Text("", key="-Determinant-", font=("Monospace 12"))],
                [eg.Text("eigenvalues", font=("Monospace 12")), eg.Text("", key="-Eigenvalues-", font=("Monospace 12"))],
                [eg.Text("rank", font=("Monospace 12")), eg.Text("", key="-Rank-", font=("Monospace 12"))],
                [eg.Text("diag", font=("Monospace 12")), eg.Text("", key="-Diag-", font=("Monospace 12"))]
            ], font=("Monospace 18")), eg.Button("hoge", key="-ExitApp-")]
        
        self.layout = [
                self.input_frame,
                self.result_frame
            ]
        
        self.window = eg.Window(title="Matrix Calculator", layout=self.layout)

    def close(self):
        self.window.close()