from sys import argv

if len(argv) < 2:
    print("provide a filename")
else:
    file = open(argv[1])
    lines = file.read()

    lines = lines.split("\n")
    word_count = 0
    letters_count = 0
    for line in lines:
        words = line.split(" ")
        word_count += len(words)
        letters_count += len(line)
    line_count = len(lines) - 1

    print(f"line count is :{line_count}")
    print(f"word count is :{word_count}")
    print(f"letters count is :{letters_count}")