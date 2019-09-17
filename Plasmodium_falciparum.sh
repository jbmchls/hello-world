sed $'s/\r$//'
cd ~/
echo 'when prompted for username, enter anonymous'
echo 'use your email as the password'
mkdir Plasmodium_falciparum && cd $_
ftp ftp.ncbi.nlm.nih.gov
# enter 'anonymous' as un and your email as pw
passive && prompt
cd ftp.ncbi.nlm.nih.gov/genomes/archive/old_genbank/Plasmodium_falciparum/CHR1
mget AL844501.*
bye
