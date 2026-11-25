#!/data/data/com.termux/files/usr/bin/bash
apt update -y && apt install python git -y
chmod +x ~/tiktok-pk/pk_sim.py
ln -sf ~/tiktok-pk/pk_sim.py $PREFIX/bin/pk-sim
echo "[+] ተጭኗል! አሁን 'pk-sim' ብለህ ስትጽፍ ይከፍታል።"
