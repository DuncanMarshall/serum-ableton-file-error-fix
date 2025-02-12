'''Runs a Windows batch command to free file handles associated with Ableton 11 timeline'''

import subprocess


print("Freeing file handles...")

def run_command(command):
    # Run the command and capture its output
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Return the output as a string
        return result.stdout.strip()
    else:
        # If there was an error, raise an exception or handle it as needed
        raise RuntimeError(f"Command '{command}' failed with exit code {result.returncode}")


#run the handle command to list all open file handles on the system
command = ["handle", "-a"]
output = run_command(command)

#find the section associated with Ableton Live 11 Suite
substr = output[output.find("Ableton Live 11 Suite.exe pid"):]
substr = substr[:substr.find("--------")]


#split in to lines
lines = substr.splitlines()

#get the pid of Ableton 11
pid = lines[0][lines[0].find("pid: ") + 5:]
pid = pid[:pid.find(" ")]


#iterate over lines
for line in lines:
    #if it's a .wav, we're interested
    if line.endswith(".wav"):
        #this is to exclude things like the .wav associated with Ableton's built in metronome
        if line.find('C:\\ProgramData\\Ableton\\Live 11 Suite\\Resources\\') == -1:
            #get the fid (file id)
            fid = line[:line.find(": ")]
            
            #kill it
            command = f'handle64 -c {fid} -p {pid} -y'
            print("doing command: " + command)
            print("based on line:" + line)
            run_command(command)


