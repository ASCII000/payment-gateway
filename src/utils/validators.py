"""
Module contains utils validators
"""
import re


def validate_cpf_cnpj(value: str) -> bool:
    """
    Validate CPF or CNPJ

    Args:
        value (str): CPF or CNPJ

    Returns:
        bool: True or False is a valid CPF or CNPJ
    """

    # Verify if value contains specifc characters and length
    # for cpf 11 and cnpj 14
    if re.match(r"^\d{11}$", value) or re.match(r"^\d{14}$", value):
        return True

    return False
