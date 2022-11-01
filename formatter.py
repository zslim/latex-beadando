import re


def read_file(path):
    with open(path) as file:
        content = file.read()
    return content


def break_sentences(content):
    # '. ' if it's not after 'pl' and not before newline:
    pattern = r"(?<!pl)\. (?!\n)"
    replacement = ".\n"
    result = re.sub(pattern, replacement, content)
    return result


def write_file(path, content):
    with open(path, "w") as file:
        file.write(content)


if __name__ == '__main__':

    in_path = "beadando_feladat.tex"
    out_path = "tordelt.tex"
    content = read_file(in_path)
    newlined = break_sentences(content)
    write_file(out_path, newlined)
