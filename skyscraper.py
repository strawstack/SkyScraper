import sys
import re

if len(sys.argv) < 2:
    print("skyscraper.py [doc] [code] [output]")

else:
    doc_path  = sys.argv[1]
    code_path = sys.argv[2]

    out_file = "output"
    if len(sys.argv) == 4:
        out_file = sys.argv[3]

    doc  = open(doc_path, 'r').read()
    code = open(code_path, 'r').readlines()

    # Blocks is a map from tag to code block
    blocks = {}
    shouldCollect = False
    collection = []

    # For each line, toggle on/off collector
    # push blocks of lines to Blocks
    p = re.compile('.+\[[\+-]\](.+)')
    for line in code:
        m = p.match(line)
        if m:
            shouldCollect = not shouldCollect
            if not shouldCollect:
                blocks[m.group(1)] = "".join(collection)
                collection = []
        else:
            collection.append(line)

    # Replace tags in doc with code blocks
    p = re.compile('\[\+\](\w+)')
    tags = p.findall(doc)
    for tag in tags:
        doc = doc.replace("[+]" + tag, blocks[tag].strip())

    ext = doc_path[doc_path.rfind("."):]

    with open(out_file + ext, 'w') as out:
        out.write(doc)
