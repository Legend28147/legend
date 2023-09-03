import re

file_path = 'file_to_read.txt'
output_path = 'result.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

terrible_count = len(re.findall(r'\bterrible\b', content, flags=re.IGNORECASE))
print(f"Total count of 'terrible': {terrible_count}")

def replace_terrible(match):
    global count
    if count % 2 == 1:
        count += 1
        return 'marvellous'
    else:
        count += 1
        return 'pathetic'

count = 1
content = re.sub(r'\bterrible\b', replace_terrible, content, flags=re.IGNORECASE)

with open(output_path, 'w', encoding='utf-8') as result_file:
    result_file.write(content)

print("New file saved as result.txt")



