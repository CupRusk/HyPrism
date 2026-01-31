<p align="left">
  <img src="assets/Hyprism.png" alt="HyPrism Logo" width="64" height="64" />
</p>

# HyPrism

[![Downloads](https://img.shields.io/github/downloads/yyyumeniku/HyPrism/total?style=for-the-badge&logo=github&label=Downloads&color=207e5c)](https://github.com/yyyumeniku/HyPrism/releases)
[![Website](https://img.shields.io/badge/Website-hyprism-207e5c?style=for-the-badge&logo=website)](https://yyyumeniku.github.io/hyprism-site/)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/yyyumeniku)
[![Discord](https://img.shields.io/badge/Website-discord-207e5c?style=for-the-badge&logo=discord)](https://discord.gg/ekZqTtynjp)


A multiplatform Hytale launcher with mod manager and more!

<img width="3016" height="2056" alt="Screenshot 2026-01-31 at 07 36 56@2x" src="https://github.com/user-attachments/assets/edfccc21-b08b-4ae5-95b9-cfebd0c30358" />


## Installation
Downloads are available in [releases](https://github.com/yyyumeniku/HyPrism/releases)

### Available builds
HyPrism is availalbe for:
- **Windows x86_64**
- **macOS arm**
- **Linux x86_64**: 4 options (AppImage, DEB, RPM, Flatpak)

For older Linux OSes the Flatpak will be the only feasable solution.

### Flatpak Remote (Experimental)
You can try the experimental Flatpak remote hosted on GitHub Pages. Updates may be unstable.

1) Add the remote:
  - `flatpak remote-add --if-not-exists hyprism https://yyyumeniku.github.io/HyPrism/flatpak-repo`
2) Install:
  - `flatpak install hyprism dev.hyprism.HyPrism`
3) Update later:
  - `flatpak update dev.hyprism.HyPrism`

## Build instructions
**Backend**: 
- Default/Modern build: `dotnet build`
- Legacy build: `dotnet build /p:PhotinoVersion=legacy`
- Run: `dotnet run`

**Frontend**: 
- Build: `npm run build` (in the `frontend` directory)

## Credits
Sanasol for maintaining and creating the auth server (https://github.com/sanasol/hytale-auth-server)
