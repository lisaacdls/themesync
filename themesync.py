import os
import shutil
import json
from pathlib import Path
import winreg

class ThemeSync:
    def __init__(self, themes_directory, config_file='themesync_config.json'):
        self.themes_directory = Path(themes_directory)
        self.config_file = Path(config_file)
        self.themes = self.load_themes()

    def load_themes(self):
        """Load available themes from the themes directory."""
        themes = [f for f in self.themes_directory.iterdir() if f.is_dir()]
        return themes

    def save_config(self, selected_theme):
        """Save the selected theme to the configuration file."""
        with open(self.config_file, 'w') as file:
            json.dump({'selected_theme': selected_theme.name}, file)

    def load_config(self):
        """Load the selected theme from the configuration file."""
        if self.config_file.exists():
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                return config.get('selected_theme')
        return None

    def apply_theme(self, theme_name):
        """Apply the selected theme."""
        theme_path = self.themes_directory / theme_name
        if theme_path.exists() and theme_path.is_dir():
            wallpaper = theme_path / 'wallpaper.jpg'
            if wallpaper.exists():
                self.set_wallpaper(str(wallpaper))
            self.save_config(theme_path)

    def set_wallpaper(self, wallpaper_path):
        """Set the desktop wallpaper."""
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Wallpaper", 0, winreg.REG_SZ, wallpaper_path)
        winreg.CloseKey(key)
        os.system('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')

    def sync_themes(self):
        """Synchronize themes across devices."""
        selected_theme = self.load_config()
        if selected_theme:
            self.apply_theme(selected_theme)
        else:
            print("No theme selected. Please apply a theme first.")

if __name__ == "__main__":
    themes_directory = "C:\\Users\\YourUsername\\Themes"
    theme_sync = ThemeSync(themes_directory)
    theme_sync.sync_themes()