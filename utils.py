# Utility functionality

sep = 30 * "="
ssep = 30 * "-"

def print_(msg):
    print("* {}\n".format(msg.capitalize()))
def print_sec(msg):
    print("{0}\n{1}\n{0}\n\n".format(len(msg) * "=", msg.upper()))
def print_ssec(msg):
    print("{0}\n{1}\n{0}\n\n".format(len(msg) * "-", msg.capitalize()))
