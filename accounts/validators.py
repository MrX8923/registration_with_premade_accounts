from django.core.exceptions import ValidationError


def age_validator(val: str):
    if not 0 < int(val) < 130:
        raise ValidationError('Возраст должен быть в пределах от 0 до 130 лет')
    