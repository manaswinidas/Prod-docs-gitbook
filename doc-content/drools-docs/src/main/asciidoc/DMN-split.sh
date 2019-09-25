#!/bin/bash
sudo chmod -R 777 ../asciidoc
mkdir DMN
csplit --quiet --prefix=DMN/ source/DMN-source.asciidoc "/\[id/" "{*}"
find DMN/ -size 0 -delete
cd DMN
for file in {01..24}
do
    # sed -n "s/^.*'\(.*\)_{context}'.$/\1/ p" $file <<< ${bigname}
    bigname=$(sed -n "s/^.*'\(.*\)_{context}'.$/\1/ p" $file)
    sudo mv -v "$file" "$bigname.asciidoc"
    # "s/^.*'\(.*\)'.*$/\1/ p"
done
for file in {25..28}
do 
    # sed -n "s/^.*'\(.*\)'.$/\1/ p" $file <<< ${name} 
    name=$(sed -n "s/^.*'\(.*\)'.$/\1/ p" $file)
    sudo mv -v "$file" "$name.asciidoc"
done
sudo chmod -R 777 ../DMN