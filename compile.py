import subprocess
import os

# run py 1-12-2_1-16-5_ID_transformer.py --reverse
subprocess.run(["py", ".\\1-12-2_1-16-5_ID_transformer.py", "--reverse"])
# run gradlew buildForge1122
os.system("gradlew buildForge1122")
# run py 1-12-2_1-16-5_ID_transformer.py
subprocess.run(["py", ".\\1-12-2_1-16-5_ID_transformer.py"])
# run gradlew buildForge1165
os.system("gradlew buildForge1165")
# run py 1-12-2_1-16-5_ID_transformer.py --reverse
subprocess.run(["py", ".\\1-12-2_1-16-5_ID_transformer.py", "--reverse"])
