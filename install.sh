

# Paths
DESKTOP_FILE=~/.local/share/applications/DelftBlue.desktop
EXEC_PATH=$(pwd)/dist/main
ICON_PATH=$(pwd)/dist/backends/img.png
WORKING_DIR=$(pwd)/dist

# Create the .desktop file
cat > "$DESKTOP_FILE" <<EOL
[Desktop Entry]
Type=Application
Name=DelftBLue
Exec=$EXEC_PATH
Icon=$ICON_PATH
Path=$WORKING_DIR
Terminal=false
Categories=Utility;
EOL

#copy to desktop and make exec
chmod +x "$DESKTOP_FILE"
cp  ~/.local/share/applications/DelftBlue.desktop ~/Desktop/


