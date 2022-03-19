import subprocess
import timeit

filename = "./pin_checker"

def run_bin(filename, input):
    echo_proc = subprocess.run(['echo', input], capture_output=True) #echo out this and pipe into the binary process
    bin_proc = subprocess.run([filename], input=echo_proc.stdout, capture_output=True)

    return(bin_proc.stdout)


#params
try_num = 10
pin_len = 8

#initial value
maxtime = [0,0]
cracked = ""

for i in range(pin_len):

    crack_len = len(cracked)
    p = list(cracked + ("0" * (pin_len - crack_len)))

    for i in range(10):
        p[crack_len] = str(i)
        pin = "".join(p)
        # print(pin)

        result = timeit.timeit(stmt="run_bin(filename, pin)", globals=globals(), number=try_num)
        # print(result)
        
        if(result > maxtime[0]):
            maxtime = [result, i]

    # print(maxtime)
    cracked += str(maxtime[1])
    print(cracked)
    

with open("pin.txt", "w") as f:
    f.write(cracked)