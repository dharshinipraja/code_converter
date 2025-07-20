import re
import textwrap


def read_multiline_input():
    print("Paste your code below (Python 2 / Java / C++ / SQL).")
    print("➡ Press Enter twice (empty line) to finish input.\n")

    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        except (EOFError, OSError):
            print("\n  Input interrupted or not supported in this environment.")
            break
    return "\n".join(lines)


def convert_code(code):
    # Convert Python 2 to Python 3
    code = re.sub(r'print\s+"([^"]*)"', r'print("\1")', code)
    code = re.sub(r"print\s+'([^']*)'", r'print("\1")', code)
    code = re.sub(r'print\s+([^\n]+)', r'print(\1)', code)
    code = code.replace('xrange', 'range')
    code = code.replace('raw_input', 'input')

    # Convert basic Java/C++ syntax to Python
    code = re.sub(r'int\s+(\w+)\s*=\s*(\d+);', r'\1 = \2', code)
    code = re.sub(r'String\s+(\w+)\s*=\s*"(.*?)";', r'\1 = "\2"', code)
    code = re.sub(r'for\s*\((int|var)?\s*(\w+)\s*=\s*(\d+);\s*\2\s*<\s*(\d+);\s*\2\+\+\)', r'for \2 in range(\3, \4):', code)

    # Convert SQL SELECT statements to pseudo Python (pandas-style)
    code = re.sub(r'SELECT\s+\*\s+FROM\s+(\w+);?', r'print(\1)', code, flags=re.IGNORECASE)
    code = re.sub(r'SELECT\s+(.*?)\s+FROM\s+(\w+);?', r'print(\2[[\1]])', code, flags=re.IGNORECASE)

    return textwrap.dedent(code)


def main():
    print("\U0001F501 Code Converter: Python 2 / Java / C++ / SQL \u2794 Python 3\n")
    code = read_multiline_input()
    if not code.strip():
        print(" No input provided. Please paste some code.")
        return

    converted_code = convert_code(code)
    print("\n Converted Code:\n")
    print(converted_code)


if __name__ == "__main__":
    main()
