class Scanner:
    def __init__(self, input):
        self.input = input
        self.char = 0
        self.len = len(input)
        self.sum = 0

    def read_num(self):
        num_str = ""
        while self.input[self.char] in "0123456789":
            num_str = num_str + self.input[self.char]
            self.char += 1

        return int(num_str)

    def read_string(self, string):
        for char in string:
            if self.input[self.char] != char:
                return False
            self.char += 1

        return True

    def read_mul(self):
        if not self.read_string("mul("):
            return

        if self.input[self.char] not in "0123456789":
            return
        num1 = self.read_num()

        if not self.read_string(","):
            return

        if self.input[self.char] not in "0123456789":
            return
        num2 = self.read_num()

        if self.input[self.char] != ')':
            return

        self.sum += num1 * num2

    def read_input(self):
        while(self.char < self.len):
            curr = self.input[self.char]
            if curr == 'm':
                self.read_mul()
            else:
                self.char += 1

with open("input.txt", "r") as f:
    ip_text = f.read()

scanner = Scanner(ip_text)
scanner.read_input()

print(scanner.sum)
