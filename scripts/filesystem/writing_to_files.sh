str="Ragnaros, the Firelord"
if [[ $(< /home/ubuntu/file.txt) != "$str" ]]; then
    exit -1
fi