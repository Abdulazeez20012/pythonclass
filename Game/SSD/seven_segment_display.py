class SevenSegmentDisplay:
    @staticmethod
    def get_seven_segment_display(digit):
        segment_patterns = {
            0: [
                ['#', '#', '#', '#'],
                ['#', ' ', ' ', '#'],
                ['#', ' ', ' ', '#'],
                ['#', ' ', ' ', '#'],
                ['#', '#', '#', '#']
            ],
            1: [
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', '#'],
                [' ', ' ', ' ', '#'],
                [' ', ' ', ' ', '#'],
                [' ', ' ', ' ', '#']
            ],
            2: [
                ['#', '#', '#', '#'],
                [' ', ' ', ' ', '#'],
                ['#', '#', '#', '#'],
                ['#', ' ', ' ', ' '],
                ['#', '#', '#', '#']
            ],
            3: [
                ['#', '#', '#', '#'],
                [' ', ' ', ' ', '#'],
                ['#', '#', '#', '#'],
                [' ', ' ', ' ', '#'],
                ['#', '#', '#', '#']
            ],
            4: [
                [' ', ' ', ' ', ' '],
                ['#', ' ', ' ', '#'],
                ['#', '#', '#', '#'],
                [' ', ' ', ' ', '#'],
                [' ', ' ', ' ', ' ']
            ],
            5: [
                ['#', '#', '#', '#'],
                ['#', ' ', ' ', ' '],
                ['#', '#', '#', '#'],
                [' ', ' ', ' ', '#'],
                ['#', '#', '#', '#']
            ],
            6: [
                ['#', '#', '#', '#'],
                ['#', ' ', ' ', ' '],
                ['#', '#', '#', '#'],
                ['#', ' ', ' ', '#'],
                ['#', '#', '#', '#']
            ],
            7: [
                ['#', '#', '#', '#'],
                [' ', ' ', ' ', '#'],
                [' ', ' ', ' ', '#'],
                [' ', ' ', ' ', '#'],
                [' ', ' ', ' ', '#']
            ],
            8: [
                ['#', '#', '#', '#'],
                ['#', ' ', ' ', '#'],
                ['#', '#', '#', '#'],
                ['#', ' ', ' ', '#'],
                ['#', '#', '#', '#']
            ],
            9: [
                ['#', '#', '#', '#'],
                ['#', ' ', ' ', '#'],
                ['#', '#', '#', '#'],
                [' ', ' ', ' ', '#'],
                ['#', '#', '#', '#']
            ]
        }

        if 0 <= digit <= 9:
            return segment_patterns[digit]
        return None


def display_number_on_seven_segment(number_str):
    rows = ['' for _ in range(5)]
    for char in number_str:
        if char.isdigit():
            display = SevenSegmentDisplay.get_seven_segment_display(int(char))
            if display:
                for i in range(5):
                    rows[i] += ' '.join(display[i]) + '   '
            else:
                print(f"Invalid digit: {char}")
                return
        else:
            print(f"Invalid input: {char}. Please enter digits only.")
            return

    for row in rows:
        print(row)


def main():
    print("Welcome to the Seven Segment Display!")
    while True:
        number_input = input("Enter a number to display (or 'q' to quit): ")

        if number_input.lower() == 'q':
            print("Goodbye!")
            break

        display_number_on_seven_segment(number_input)


if __name__ == "__main__":
    main()
