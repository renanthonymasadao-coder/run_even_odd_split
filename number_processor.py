class NumberProcessor:
    def __init__(self, file_name):
        self.file_name = file_name

    def process_numbers(self):
        with open(self.file_name, 'r') as file:
            numbers = list(map(int, file.read().split()))

        even_numbers = [n for n in numbers if n % 2 == 0]
        odd_numbers = [n for n in numbers if n % 2 != 0]

        with open("even.txt", 'w') as even_file:
            even_file.write(" ".join(map(str, even_numbers)))

        with open("odd.txt", 'w') as odd_file:
            odd_file.write(" ".join(map(str, odd_numbers)))
