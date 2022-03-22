import subprocess

filename = "./keygenme"

def run_bin(filename, input):
    echo_proc = subprocess.run(['echo', input], capture_output=True) #echo out this and pipe into the binary process
    bin_proc = subprocess.run([filename], input=echo_proc.stdout, capture_output=True)

    return(bin_proc.stdout)


potential_key = "picoCTF{br1ng_y0ur_0wn_k3y_?a450e14}"

for i in range(33, 127):
    input = potential_key.replace("?", chr(i))
    print(input)
    print(run_bin(filename, input))