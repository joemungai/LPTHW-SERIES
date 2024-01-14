import sys
script,input_encoding,error = sys.argv

def main (languages_file,encoding,errors):
    line = languages_file.readline()
    if line :
        print_line (line,encoding,errors)
        return main (languages_file,encoding,error)

def print_line(line,encoding,errors):
     strip_line = line.strip()
     encode_line = strip_line.encode(encoding,errors=errors)
     decode_line = encode_line.decode(encoding,errors=errors)

     print(decode_line,"<=====>",encode_line)

language = open ("languages.txt",encoding = "utf-8")
main(language,input_encoding,error)
