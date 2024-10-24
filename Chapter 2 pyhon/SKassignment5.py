import subprocess

 
    subprocess.check_output(["java", "--version"])

    print("Java is installed on your computer.")

except FileNotFoundError:
    print("Java is not installed on your computer.")
