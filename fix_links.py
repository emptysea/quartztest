import os

def fix_links_run(path):
    for item in os.walk(path):
        for filename in item[2]:
            filesplit = os.path.splitext(filename)

            if filesplit[1] == ".md":
                relfilepath = str(item[0]) + "/" + filename
                #print ("Will process " + relfilepath)
                process_file(relfilepath)

def process_file(filename):

    try:
        with open(filename, 'r') as file:
            content = file.readlines()

        new_content = []
        new_line = ""

        for line in content:
            new_line = line
            if "![[" in line:
                pass
            elif "[[" in line:

                #print ("Need to modify " + new_line)
                index_start = 0
                index_start = new_line.find("[[", index_start)
                index_end = new_line.find("]]", index_start)
                while(index_end > 0):
                    if "|" not in new_line[index_start:index_end] and index_start >= 0:
                        old_text = new_line[index_start:index_end+2]
                        new_text = old_text[:-2] + "|" + old_text[2:]
                        print ("Need to modify " + old_text + " with " + new_text)
                        new_line = new_line.replace(old_text, new_text, 1)
                    index_start = index_end
                    index_start = new_line.find("[[", index_start)
                    index_end = new_line.find("]]", index_start)
            new_content.append(new_line)


        #modified_content = content.replace(old_text, new_text)

        with open(filename, 'w') as file:
            for lines in new_content:
                file.write(lines)
        #print(f"Successfully replaced '{old_text}' with '{new_text}' in '{filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
   fix_links_run("content")
