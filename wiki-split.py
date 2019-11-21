import os
import shutil
import glob
import fileinput
import itertools

source = os.getcwd()+"/doc-content/drools-docs/src/main/asciidoc/DMN-subtree/Authorising-Rules/Designing-a-decision-service-using-DMN-models/Decision-Model-and-Notation-DMN"
dest = os.getcwd()+"/doc-content/drools-docs/src/main/asciidoc/DMN"
shutil.rmtree(dest)
try:
    os.mkdir(dest)
except OSError:
    print("Creation of the directory %s failed" % dest)
else:
    print("Successfully created the directory %s " % dest)

files = [f for f in glob.glob(source+"/*.asciidoc", recursive=True)]

for f in files:
    with open(f, "r") as g:
        stri = g.read()
        for i, part in enumerate(stri.split("[id")):
            if not part.strip():
                continue  # make sure its not empty
            with open("file%d.asciidoc" % i, "w") as f:  # open a file to write to
                f.write("[id"+part)
    for file in os.listdir(os.getcwd()):
        if file.endswith(".asciidoc"):
            shutil.move(file, dest)
    with os.scandir(dest) as entries:
        for entry in entries:
            if entry.is_file():
                with open(entry, "r") as fi:
                    fline = fi.readline()
                    m=fline[fline.find("[id='")+5:fline.find("_{context}']")]
                    os.rename(entry,m+".asciidoc")
for file in os.listdir(os.getcwd()):
        if file.endswith(".asciidoc"):
            shutil.move(file, dest)
for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/*'].asciidoc"):
    os.rename(file,file.replace("']",""))

source = os.getcwd()+"/doc-content/drools-docs/src/main/asciidoc/DMN-subtree/Getting-Started/Getting-started-with-decision-services"
# dest = os.getcwd()+"/doc-content/drools-docs/src/main/asciidoc/DMN"

files = [f for f in glob.glob(source+"/*.asciidoc", recursive=True)]

for f in files:
    with open(f, "r") as g:
        stri = g.read()
        for i, part in enumerate(stri.split("[id")):
            if not part.strip():
                continue  # make sure its not empty
            with open("file%d.asciidoc" % i, "w") as f:  # open a file to write to
                f.write("[id"+part)
    for file in os.listdir(os.getcwd()):
        if file.endswith(".asciidoc"):
            shutil.move(file, dest)
    with os.scandir(dest) as entries:
        for entry in entries:
            if entry.is_file():
                with open(entry, "r") as fi:
                    fline = fi.readline()
                    m=fline[fline.find("[id='")+5:fline.find("_{context}']")]
                    os.rename(entry,m+".asciidoc")
for file in os.listdir(os.getcwd()):
        if file.endswith(".asciidoc"):
            shutil.move(file, dest)
for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/*'].asciidoc"):
    os.rename(file,file.replace("']",""))

output_lines = []

filename=os.getcwd()+'/assemblies/assembly_dmn-models/main.adoc' 
with open(filename) as fp:
    linesbegin = list(itertools.takewhile(lambda x: '// Modules -' not in x, 
        itertools.dropwhile(lambda x: "[id='assembly_dmn-models']" not in x, fp)))
with open(filename) as fp:
    lines = list(itertools.takewhile(lambda x: '== Additional resources' not in x, 
        itertools.dropwhile(lambda x: '// Modules -' not in x, fp)))
with open(filename) as fp:
    linesend =list(itertools.takewhile(lambda x: '// End of main.adoc' not in x, 
        itertools.dropwhile(lambda x: '== Additional resources' not in x, fp)))

def get_file_with_parents(filepath, levels=1):
    common = filepath
    for i in range(levels + 1):
        common = os.path.dirname(common)
    return os.path.relpath(filepath, common)

res = [sub.replace("= Designing a decision service using DMN models", "= Getting started with decision services") for sub in linesbegin] 
for line in lines:
    if ("dmn-con.asciidoc" in line or "dmn-execution-con.asciidoc" in line or "dmn-execution-rest-proc.asciidoc" in line):
        output_lines.append(line)
    else:
        if line.startswith !="//":
            output_lines.append("//" + line)
    i=0                   
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/decision*.asciidoc"):
            if("// Modules - concepts, procedures, refs, etc." in line):
                output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+"+str(1+i)+"]\n")
                i=1
                print(i)
                continue
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/dmn-gs-new*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+1]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/dmn-gs-creating-drd*.asciidoc"):
        if("dmn-con.asciidoc" in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/dmn-gs-creating-c*.asciidoc"):
        if("dmn-con.asciidoc" in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/dmn-gs-assigning-c*.asciidoc"):
        if("dmn-con.asciidoc" in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n") 
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/dmn-gs-defining*.asciidoc"):
        if("dmn-con.asciidoc" in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/test*.asciidoc"):
        if("dmn-con.asciidoc" in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+1]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/dmn-gs-test*.asciidoc"):
        if("dmn-con.asciidoc" in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
f = open(filename, "w")
final=res+output_lines+linesend
f.write("\n".join(final))
f.close()

