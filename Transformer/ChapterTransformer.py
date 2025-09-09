import re


def refine_header_string(header):
    # Remove "Chapter <number>" at the beginning
    return re.sub(r'^chapter\s+\d+\s*', '', header, flags=re.IGNORECASE)

def break_keywords(toc_object):
    toc_return = []
    for header_object in toc_object:
        new_header_object = []
        for content_line in header_object:
            by_keyword_match = re.search(r'\bby\b.*', content_line, flags=re.IGNORECASE)
            if by_keyword_match:
                parts = re.split(r'(\bby\b)', content_line, flags=re.IGNORECASE)
                first_part = parts[0].strip()
                second_part = ''.join(parts[1:]).strip()  # everything after, including "by"
                if first_part:
                    new_header_object.append(first_part)
                new_header_object.append(second_part)
            else:
                new_header_object.append(content_line)
        toc_return.append(new_header_object)

    return toc_return

# test = [
#     ['Preface'],
#     ['Chapter 1 Something Here', 'by Random Author'],
#     ['Chapter 2 Something Here By random author'],
#     ['Chapter 3 including by with author name', 'by Random Author'],
#     ['Chapter 4 including by without author name'],
#
# ]
# result = break_keywords(test)
# print()