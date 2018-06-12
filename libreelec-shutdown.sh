
if pgrep "game.emulationstation.RPi" > /dev/null;
then 
	killall game.emulationstation-RPi
	sleep 5s
	shutdown -h now 
else
	kodi-send --action="shutdown" 
fi

