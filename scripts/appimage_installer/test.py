from PyInstaller.utils.hooks import collect_all, collect_submodules

datas, binaries, hiddenimports = collect_all('requests')

# Также добавляем все подмодули requests
hiddenimports += collect_submodules('requests')