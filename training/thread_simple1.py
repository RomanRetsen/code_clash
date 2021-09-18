from threading import Thread


class InputReader(Thread):
    def run(self) -> None:
        self.line_of_text = input()

print("Enter some text and press enter ", end="")
my_thread = InputReader()
my_thread.start()

count = result = 1
while my_thread.is_alive():
    result = count * count
    count += 1

print("Calculated squares up to {0} * {0} = {1}".format
      (count, result)
      )
print(f"While you typed {my_thread.line_of_text}")