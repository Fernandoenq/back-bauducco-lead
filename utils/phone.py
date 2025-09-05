import re

def normalize_and_validate_phone(phone: str) -> str:
    digits = re.sub(r"\D", "", phone or "")
    # Brasil: 10 (fixo) ou 11 (celular). Aceitamos 10-13 caso venha com país/DDD, mas guardamos DIGITOS.
    if len(digits) < 10 or len(digits) > 13:
        raise ValueError("Celular/telefone inválido.")
    return digits
