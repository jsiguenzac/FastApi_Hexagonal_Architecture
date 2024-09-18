# REGION: Formato JSON para salida standar de los endpoints
from src.schemas.base_out import BaseM, Salida

def exit_json(state: int, data: dict) -> BaseM:
    if state < 0 or state > 1:
        raise ValueError("El estado de salida debe ser 1 o 0")
    msg = "success" if state == 1 else "error"
    exit_json = Salida(state=state, msg= msg)
    exit_json.data = data
    salida_model = BaseM(**exit_json.__dict__)
    return salida_model
# END REGION