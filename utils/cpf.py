import re

def only_digits(s: str) -> str:
    return re.sub(r"\D", "", s or "")

def _calc_digit(numbers: str) -> int:
    weight = len(numbers) + 1
    total = sum(int(d) * (weight - i) for i, d in enumerate(numbers))
    rest = total % 11
    return 0 if rest < 2 else 11 - rest

def is_valid_cpf(cpf_digits: str) -> bool:
    if len(cpf_digits) != 11:
        return False
    if cpf_digits == cpf_digits[0] * 11:
        return False
    d1 = _calc_digit(cpf_digits[:9])
    d2 = _calc_digit(cpf_digits[:9] + str(d1))
    return cpf_digits[-2:] == f"{d1}{d2}"

def normalize_and_validate_cpf(cpf: str) -> str:
    digits = only_digits(cpf)
    if not is_valid_cpf(digits):
        raise ValueError("CPF inválido.")
    return digits
