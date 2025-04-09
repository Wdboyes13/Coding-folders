if SwitchAudio -l | grep -q "External Headphones"
then
SwitchAudio -o "External Headphones"
osascript -e 'set volume output volume 50'
osascript -e 'tell application "Music" to play playlist "good music copy"'
echo Playing music
fi