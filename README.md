# ThemeSync

ThemeSync is a Python-based tool designed to synchronize desktop themes across multiple Windows devices, ensuring a consistent look and feel on all your machines. It allows you to keep your desktop environment uniform and personalized, no matter where you are.

## Features

- **Load and manage themes**: Easily load themes stored in a designated directory.
- **Apply selected theme**: Choose and apply a theme from your collection.
- **Sync themes**: Automatically synchronize your selected theme across devices.
- **Set desktop wallpaper**: Update your desktop wallpaper to match the theme.

## Requirements

- Windows OS
- Python 3.x
- Administrative privileges (for registry modifications)
- Themes should be stored in a directory with each theme in a separate subdirectory containing at least a `wallpaper.jpg`.

## Installation

1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed.
3. Install any necessary Python packages (none required for this basic setup).

## Usage

1. Place your themes in the directory specified in `themes_directory` in the script. Each theme should be in its own subdirectory with a `wallpaper.jpg` file.
2. Run the script using Python:
   ```bash
   python themesync.py
   ```
3. The script will load the previously selected theme and apply it. If no theme is selected, it will prompt you to apply a theme first.

## Configuration

- The script uses a JSON configuration file (`themesync_config.json`) to store the currently selected theme.

## Limitations

- Currently, supports only wallpaper synchronization.
- Works on Windows OS only due to the reliance on the Windows registry for wallpaper settings.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.