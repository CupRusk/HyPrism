# Linux Installation Guide

HyPrism on Linux requires WebKitGTK 4.0 to run. Due to varying library versions across distributions, we recommend using Flatpak for the most reliable experience.

## Recommended: Flatpak Installation

Flatpak bundles all dependencies, avoiding library version conflicts.

### Prerequisites

Install Flatpak if not already installed:

```bash
# Ubuntu/Debian
sudo apt install flatpak

# Fedora
sudo dnf install flatpak

# Arch Linux
sudo pacman -S flatpak
```

### Install HyPrism

Download the latest `.flatpak` file from [releases](https://github.com/yyyumeniku/HyPrism/releases/latest) and install:

```bash
flatpak install HyPrism.flatpak
```

### Run HyPrism

```bash
flatpak run dev.hyprism.HyPrism
```

## Alternative: AppImage

### Prerequisites

Install WebKitGTK 4.0 (version 2.40+ recommended):

```bash
# Ubuntu 24.04+
sudo apt install libwebkit2gtk-4.0-37

# Ubuntu 22.04 or older
sudo apt install libwebkit2gtk-4.0-dev

# Fedora
sudo dnf install webkit2gtk4.0

# Arch Linux
sudo pacman -S webkit2gtk-4.1
```

### Run AppImage

1. Download `HyPrism-x86_64.AppImage` from [releases](https://github.com/yyyumeniku/HyPrism/releases/latest)
2. Make it executable: `chmod +x HyPrism-x86_64.AppImage`
3. Run: `./HyPrism-x86_64.AppImage`

## Troubleshooting

### AppImage won't launch (SteamOS/Steam Deck)

SteamOS has strict AppImage sandboxing. Use Flatpak instead:

```bash
flatpak install HyPrism.flatpak
flatpak run dev.hyprism.HyPrism
```

### "libwebkit2gtk-4.0.so.37: cannot open shared object file"

Your system is missing WebKitGTK. Install it using the commands above for your distribution, or switch to Flatpak.

### Game launches but crashes on world load

This may be a memory/heap corruption issue. Try:
1. Update to the latest HyPrism release
2. Ensure you have the latest graphics drivers
3. Use Flatpak, which isolates the runtime environment

### Update checker shows 404 error

Fixed in recent releases. Update to v1.0.8 or later, which includes `version.json` in releases.

## Building from Source

See [CONTRIBUTING.md](CONTRIBUTING.md) for build instructions.

## Known Issues

- AppImage may have dependency conflicts on some distributions
- Older Ubuntu versions may require backports for WebKitGTK 4.0
- Flatpak is the recommended solution for maximum compatibility

## Support

Report issues at [GitHub Issues](https://github.com/yyyumeniku/HyPrism/issues)
