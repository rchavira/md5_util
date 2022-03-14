import hashlib
import argparse


def generate_md5(fname):
    with open(fname, 'rb') as myfile:
        data = myfile.read()

    return hashlib.md5(data).hexdigest()

def compare_md5(fname, md5):
    h = generate_md5(fname)
    if md5 == h:
        return True
    else:
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="MD5 hash generator/checker",
        usage='%(prog)s [options] file',
        description="MD5",
        epilog='Meta Copyright 2022'
    )
    parser.add_argument('--md5', help='compare md5 to one generated on file')
    parser.add_argument('--input', help='input file with md5 hash to compare with one generated on file')
    parser.add_argument('--output', help='output file to store MD5', action="store_true")
    parser.add_argument('--output_file', help='output file to store MD5')
    parser.add_argument('file', help='The name of the file to use')
    args = parser.parse_args()

    # generate md5
    md5_generated = generate_md5(args.file)

    if args.output:
        if args.output_file is not None:
            fname = args.output_file
        else:
            fname = f"{args.file}.md5"

        with open(fname, "w") as o_file:
            o_file.write(md5_generated)
        print(f"MD5 hash: {md5_generated} saved to {fname}")
    else:
        print(f"Resulting MD5: {md5_generated}")

    md5_compare = ""
    if args.input is not None:
        with open(args.input, 'r') as i_file:
            md5_compare=i_file.read()
    elif args.md5 is not None:
        md5_compare=args.md5

    if md5_compare != "":
        if compare_md5(args.file, md5_compare):
            print(f"MD5 Verified")
        else:
            print(f"MD5 does not match with {md5_compare}")
