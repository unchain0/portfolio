class BaseCustomError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class LenError(BaseCustomError):
    """Erro personalizado para tratar problemas de comprimento."""


class AddressFormatError(BaseCustomError):
    """Erro personalizado para tratar problemas no formato do endereço."""


class DuplicateError(BaseCustomError):
    """Erro personalizado para tratar duplicidade."""


class FutureDateError(BaseCustomError):
    """Erro personalizado para tratar datas futuras."""
