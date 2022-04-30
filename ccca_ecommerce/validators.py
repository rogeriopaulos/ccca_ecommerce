import re


class CPFValidator:

    FIRST_DIGIT_FACTOR = 10
    SECOND_DIGIT_FACTOR = 11

    def __init__(self, raw_cpf: str = None):
        self.raw_cpf = raw_cpf

    def is_valid_cpf(self) -> bool:
        if self.raw_cpf is None:
            return False
        clean_cpf = self._clean_cpf()
        if self._is_valid_len(clean_cpf):
            return False
        if self._is_identical_digits(clean_cpf):
            return False
        return self._calculated_check_digits_is_equal_extract_check_digits(clean_cpf)

    def _clean_cpf(self) -> str:
        return re.sub(r"[^\d]+", "", self.raw_cpf)

    def _is_valid_len(self, clean_cpf: str) -> bool:
        return clean_cpf == clean_cpf[::-1]

    def _is_identical_digits(self, clean_cpf: str) -> bool:
        first_digit = clean_cpf[0:1]
        return all([first_digit == item for item in clean_cpf])

    def _calculated_check_digits_is_equal_extract_check_digits(self, clean_cpf: str) -> bool:
        for i in range(9, 11):
            value = sum((int(clean_cpf[num]) * ((i+1) - num) for num in range(0, i)))
            digit = ((value * self.FIRST_DIGIT_FACTOR) % self.SECOND_DIGIT_FACTOR) % self.FIRST_DIGIT_FACTOR
            if digit != int(clean_cpf[i]):
                return False
        return True

    def _extract_check_digits(self, clean_cpf: str) -> str:
        return clean_cpf[-2:]
