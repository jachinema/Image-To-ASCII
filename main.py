import cv2 as cv
from tkinter import Tk, filedialog, Button, Label


def average(nums):
    nums = list(nums)
    return sum(nums) / len(nums)


def get_ascii(brightness):
    base = 40
    increment = 30

    table = {
        brightness < base: "█",
        base <= brightness < base + (increment * 1): "▓",
        base + (increment * 1) <= brightness < base + (increment * 2): "▒",
        base + (increment * 2) <= brightness < base + (increment * 3): "░",
        base + (increment * 3) <= brightness < base + (increment * 4): "::::",
        base + (increment * 4) <= brightness < base + (increment * 5): "....",
        brightness >= base + (increment * 5): "    "
    }

    return table[True]


def make_ascii(image):
    
    image = cv.imread(image)
    string = '\t\t\t\t\t\t\t\t'
    for row in range(0, height):
        for col in range(0, width):
            section = average(image[row, col])
            string += get_ascii(section)
            
        string += '\n'
        string += '\n\t\t\t\t\t\t\t\t'

    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(string)


def run(master):
    path = filedialog.askopenfilename()
    make_ascii(path)
    Label(master, text='Done! You can find the output.txt in this directory.', font=('Arial', 24)).pack()


if __name__ == '__main__':
    root = Tk()

    Label(root, text='Image -> Ascii Converter', font=("Courier", 24)).pack()
    Label(root, text='(Note: output file will extract into the same directory this is run in)', font=('Courier', 12)).pack()
    Button(root, text='Choose input path', font=('Courier', 16), command=lambda: run(root)).pack()

    root.mainloop()
