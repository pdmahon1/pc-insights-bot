from src.main.models.model import Model
from src.main.models.ssd_model import SsdModel


class ModelFactory:
    def __init__(self):
        self._models = {
            "ssd":SsdModel()
        }

    def get(self, model_type:str) -> Model:
        return self._models[model_type] if model_type in self._models else None