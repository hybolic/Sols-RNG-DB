import os, sys
retry = 0 # used for import tester
virtual_dir = ".venv"
WORKING_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
virtual_dir_abs = "'"+(WORKING_DIR + "\\" + virtual_dir).replace("\\","\\\\")+"'"
requirements_path = "./requirements.txt"
### VIRTUAL ENVORIMENT ### Category:Auras
def active_venv():
    #check if we are in an venv if not we make and enter one. this keeps the main python install clean
    if not (sys.prefix != (getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix)) or not os.path.exists(virtual_dir + "/pyvenv.cfg"):
        print("FORCING VIRTUAL ENVIROMENT")
        from venv import EnvBuilder
        if not (os.path.exists(virtual_dir) and os.path.exists(virtual_dir + "/pyvenv.cfg")):
            virtual = EnvBuilder(with_pip=True)
            virtual.create(env_dir="./" + virtual_dir)
        activatorpy = "./" + virtual_dir + "/Scripts/activate_this.py"
        activator   = "./" + virtual_dir + "/Scripts/activate"
        from gzip import decompress
        from base64 import b64decode
        from re import match, sub
        from subprocess import run
        if not os.path.exists(activatorpy):
            with open(activatorpy, "w") as text_file:
                text_file.write(decompress(b64decode("H4sIAAAAAAAC/z1RwW7jIBC9+yt8G2gcpN4qIw45VNqVut2om+3FtSxsjx0SBxBDV83fF5xtT7wZ5vHmPabgLqWj0ly8C7H0Oh5LTaWv0P4zwdl"
                                                    "cmCq3CX0uSP4fJRMxN44VXSmDWS5qFnm0iOFaD8oL3VOuWddNZsGu4wV+DOhj+awv+BiCC5l4rp2C8G79FWTQhrDcEWGIxtl1hl1oVjCZj68tYe"
                                                    "M2IG+HSMRuFckSHPiUHZ0LneRHE2wSYgOXvdJNvV3QMvgzBOMjAd/et/KkYL87/ABpmlOrSJycsazR1Z0RM0Z2qgC4IL+YyIi3XFoFrz9fDn93T"
                                                    "93j82um2Vb1+dhAt3/5/Wt/gFYBJGde9JpwXaDnElUWv+XDiyndT6WxIMTbk+nfcphbr4eznpHgW7Aek4uAelkN+tt2upo4l0ehxzHTkkk2ihEH"
                                                    "NyKD9zhtH4CbCQCXlOTIi6WpW7U0WLebBLGV8/pk5wOmTPOXrUB+AdV/AqZng0UVAgAA")).decode())
                text_file.close()
        if not os.path.exists(activator):
            with open(activator, "w") as activate_file:
                activate_file.write(decompress("H4sIAAAAAAAA/52SUWuDMBDH3/0UN+1D++CKe+xwYKlgoVVpbGEbQ6RGDJS0aJSx0u8+1NTGpboxXyR3/+R+d/ePcbRnpIwYhvEEzgoAAEngHXQK"
                                            "6ugceqtFuFtugq21Cn0rcGb6RYUPeAaWYlqrq6/KmH3yVoU/T8eM1eI2VtAcM5Du1fmEDOO8Bo7nOt7a7oFq8zJa56oE2GYHMbuqhCg/aecWaual"
                                            "H3nkDTnhzt6gpefeZ06jPAU9g6cXmMa4nNLicPjTLJDRMwRkyN03YqltZAz2y9OcpFFck7a7u/E9VHgNjwkqPdIY5ywrKp/hO4jNS3oCcevFa6GL"
                                            "cotB9yFFKG1qmiYcNU1TeE8in2QyUx1VP1XhB0E8RfuMnFg+4wrRusIOhizYYxZTuiaMU/BUQnihr6qQgBYulsiar+zQ33hrP/itcLN/ceV1aPxY"
                                            "YlpOoJsSnNDW/4+V79o4Id8Ru3CgbQQAAA==").decode())
                activate_file.close()
            with open(activator, "r") as text_file:
                all_lines = text_file.readlines()
                text_file.close()
                for index, line in enumerate(all_lines):
                    if match("VIRTUAL_ENV=\#\#\#VIRTUAL_ENV\#\#\#",line):
                        all_lines[index] = sub("\#\#\#VIRTUAL_ENV\#\#\#", "'" + virtual_dir_abs + "'", line)
                        break
            with open(activator, "w") as text_file:
                text_file.writelines(all_lines)
                text_file.close()
        command1 = (activator)
        command2 = (
            "python -m pip install --upgrade pip" + " & "
            + "pip install --no-input -r " + requirements_path
        )
        try:
            print("running command: '" + command1 + "'")
            process = run(command1, capture_output=True, cwd=WORKING_DIR, shell=True, check=True, encoding="UTF-8")
            print("running command: '" + command2 + "'")
            print("this might take a while!")
            process = run(command2, capture_output=True, cwd=WORKING_DIR, shell=True, check=True, encoding="UTF-8")
            if not process.stdout == '':
                print(process.stdout)
        except Exception as exception:
            print(exception)
        del b64decode, decompress, run, EnvBuilder
        del match, sub
        with open(WORKING_DIR + "\\"+virtual_dir+"\\Scripts\\activate_this.py") as f:
            exec(compile(f.read(), activatorpy, 'exec'), dict(__file__=activatorpy))
        if not sys.prefix != (getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix):
            print("WE ARE NOT IN A VIRTUAL ENVIROMENT PLEASE CONTANCT THE DEVS!"),exit()
        else:
            print("WE ARE IN A VIRTUAL ENVIROMENT")
active_venv()

def ImportTester():
    global retry
    try:
        import requests
        pass
    except ImportError as e:
        import subprocess
        command = (
            ".\\" + virtual_dir + "\\Scripts\\activate" + " & "
            "pip install --no-input " + e.name
        )
        try:
            print("running command: '" + command + "'")
            print("this might take a while!")
            process = subprocess.run(command, capture_output=True, cwd=WORKING_DIR, shell=True, check=True, encoding="UTF-8")
            if not process.stdout == '':
                print(process.stdout)
            if not getattr(sys, 'gettrace', None) is None:
                print("DO NOT FORGET TO ADD '" + e.name + "' TO " + requirements_path, type="WARN")
        except Exception as exception:
            print(exception)
        if retry > 20: print("UNABLE TO IMPORT!?"); exit()
        retry += 1
        ImportTester()
        if subprocess:
            del subprocess
ImportTester()