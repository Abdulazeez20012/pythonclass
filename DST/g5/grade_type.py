from enum import Enum
class GradeType(Enum):
    A = 4.0
    B = 3.0
    C = 2.0
    D = 1.0
    F = 0.0
    NONE = -1.0

    @staticmethod
    def from_numeric(numeric_grade: float) -> 'GradeType':
        if numeric_grade >= 90:
            return GradeType.A
        elif numeric_grade >= 80:
            return GradeType.B
        elif numeric_grade >= 70:
            return GradeType.C
        elif numeric_grade >= 60:
            return GradeType.D
        else:
            return GradeType.F
