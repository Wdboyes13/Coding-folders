import nbt

# Load the player's NBT file
player_data = nbt.nbt.NBTFile('/Users/william/Library/Application\ Support/servers/mcserv/world/playerdata/8d7a626c-0d81-3a1e-b69a-fa46134dc12c.dat', 'rb')

# Read the player's last position (Pos tag)
pos = player_data['Pos'].value
print(f"Player's last position: X: {pos[0]}, Y: {pos[1]}, Z: {pos[2]}")

