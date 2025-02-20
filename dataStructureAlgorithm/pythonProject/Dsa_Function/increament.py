class Increament:

    def increment(digits):
        if digits[-1] < 9:
            digits [-1] += 1
        else:
            digits[-1] = 0
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits

