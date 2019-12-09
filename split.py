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
dest1=os.getcwd()+"/doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS"
try:
    os.mkdir(dest1)
except OSError:
    print("Creation of the directory %s failed" % dest1)
else:
    print("Successfully created the directory %s " % dest1)

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
            shutil.move(file, dest1)
for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/*'].asciidoc"):
    os.rename(file,file.replace("']",""))
# lifiles=[]
# for file in os.listdir(dest1):
#     lifiles.append(file)
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
    for i in range(levels + 2):
        common = os.path.dirname(common)
    return os.path.relpath(filepath, common)

for line in lines:
    if line.startswith("// Mod"):
        output_lines.append("// Modules - concepts, procedures, refs, etc.\n")               
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-con.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+1]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-conf*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-dr*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-fe*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-na*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+3]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-data-types-r*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+3]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-box*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    i=2
    for file in sorted(glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-decision-tables-*.asciidoc")):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+"+str(1+i)+"]\n")
        i=3
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-lit*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+3]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-cont*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+3]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-rel*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+3]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-func*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+3]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-invo*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+3]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-model-e*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-sup*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+1]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-prop*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-model-c*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+1]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-logic*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-data-types-d*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-inc*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    for file in glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-des*.asciidoc"):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+2]\n")
    i=0
    for file in sorted(glob.glob("doc-content/drools-docs/src/main/asciidoc/DMN/DMNDS/ds-dmn-exe*.asciidoc")):
        if("// Modules - concepts, procedures, refs, etc." in line):
            output_lines.append("include::{drools-dir}/"+get_file_with_parents(file, 1)+"[leveloffset=+"+str(1+i)+"]\n")
            i=1       
f = open(filename, "w")
final=linesbegin+output_lines+linesend
f.write("\n".join(final))
f.close()