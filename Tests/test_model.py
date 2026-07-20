from anypytools import AnyPyProcess, macro_commands as mc

from pathlib import Path

model_path = (
    Path(__file__).parent.parent
    / "Anybody_model"
    / "Application"
    / "Examples"
    / "ThoracicModel"
    / "biplanar-spinal-alignment-reconstruction-method.main.any"
)


def test_model():
    app = AnyPyProcess()

    macro = [
        mc.Load(model_path),
        mc.OperationRun("Main.RunApplication"),
    ]

    result = app.start_macro(macro)[0]

    if "ERROR" in result:
        raise RuntimeError("Model simulation failed: " + str(result["ERROR"]))
