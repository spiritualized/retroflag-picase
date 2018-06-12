#Step 1) Download Python script-----------------------------
cd /storage/
mkdir scripts
cd /storage/scripts
script=retroflag-picase-libreelec-master

if [ -e $script ];
	then
		echo "Script SafeShutdown.py already exists. Reinstalling..."
		rm -R retroflag-picase-libreelec
	else
		wget "https://github.com/spiritualized/retroflag-picase-libreelec/archive/master.zip"
		unzip master.zip
		cd retroflag-picase-libreelec-master
		chmod +x libreelec-shutdown.sh
		chmod +x libreelec-restart.sh
fi
#-----------------------------------------------------------

#Step 2) Enable Python script to run on start up------------

cd /storage/.config/
File=autostart.sh
if grep -q "libreelec_SafeShutdown.py" "$File";
	then
		echo "Autostart already enabled. Doing nothing."
	else
		echo "python /storage/scripts/retroflag-picase-libreelec-master/libreelec_SafeShutdown.py &" >> $File
		chmod +x $File
		echo "Autostart enabled"
fi
#-----------------------------------------------------------

#Step 3) Reboot to apply changes----------------------------
echo "RetroFlag Pi Case installation done. Will now reboot after 3 seconds."
sleep 3
reboot
#-----------------------------------------------------------
