echo "Enter link: "
read LINK
output=$(spotdl $LINK | grep -o '".*"' | sed 's/"//g')
file="$output.mp3"
mv -n "$file" /Volumes/KOBOeReader