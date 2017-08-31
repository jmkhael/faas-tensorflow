from http_parser.pyparser import HttpParser
import sys
from function import handler


def read_body(content_length):
    return sys.stdin.read(content_length)

def read_head():
    buf = ""
    while(True):
        line = sys.stdin.readline()
        buf += line

        if line == "\r\n":
            break
#        elif line == "":
#            break #exit(1)

    return buf

def main():

    p = HttpParser()
    while True:
        header = read_head()

        res = p.execute(header, len(header))
        result = None
        length_key = "content-length"
        content_length = p.get_headers()[length_key]
        if content_length != None:
            body = read_body(int(content_length))
            result = handler.handle(body)
        else:
            result = handler.handle(None)

        out_buffer = "HTTP/1.1 200 OK\r\n"
        out_buffer += "Content-Length: "+str(len(result))+"\r\n"
        out_buffer += "\r\n"
        out_buffer += result

        sys.stdout.write(out_buffer)
        sys.stdout.flush()
#        sys.stdout.close()

def function(input):
    return "You said \'" + input + "\'"

if __name__ == "__main__":
    main()
