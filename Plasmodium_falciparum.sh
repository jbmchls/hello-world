!/bin/bash
cd ~/
mkdir Plasmodium_falciparum && cd $_
ftp ftp.ncbi.nlm.nih.gov
# enter 'anonymous' as un and your email as pw
passive && prompt
cd ./genomes/archive/old_genbank/Plasmodium_falciparum/CHR1
mget AL844501.*
bye
