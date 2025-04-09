if ./music.sh | grep -q "Playing Music"
then
good=True
else
good=False
fi
echo $good
