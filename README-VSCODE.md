# Catppuccin Blur for VS Code

A modern, blurred variant of the Catppuccin theme for Visual Studio Code, featuring Mocha and Espresso color schemes with beautiful transparency effects.

## 🎨 Themes

This extension includes two dark themes with static blur effects:

- **Catppuccin Mocha Blur** - A soft, muted dark theme with warm tones
- **Catppuccin Espresso Blur** - A deeper, darker theme with rich contrast

Both themes use the "Light" blur level (60% opacity) for a subtle transparency effect that works well with modern desktop environments.

## 📦 Installation

### From VS Code Marketplace
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X / Cmd+Shift+X)
3. Search for "Catppuccin Blur"
4. Click Install

### Manual Installation
1. Download the `.vsix` file from the [releases page](https://github.com/johngagefaulkner/catppuccin-blur-vscode/releases)
2. In VS Code, go to Extensions
3. Click the "..." menu and select "Install from VSIX..."
4. Select the downloaded file

## 🚀 Usage

After installation:
1. Open the Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
2. Type "Color Theme"
3. Select either:
   - `Catppuccin Mocha Blur`
   - `Catppuccin Espresso Blur`

## ⚙️ Blur Effect Notes

The blur effect works best when:
- Your desktop environment supports window transparency
- VS Code is configured with transparency enabled in your operating system
- You're using a modern compositor (Linux) or window manager

> **Note**: The blur effect is achieved through alpha channel transparency. The actual blur/frosted glass effect depends on your operating system and desktop environment's compositor capabilities.

## 🎨 Color Palettes

### Mocha
Based on the Catppuccin Mocha palette with carefully adjusted transparency values for optimal readability.

### Espresso
A darker variant with pure black backgrounds and the Catppuccin Macchiato color scheme for syntax highlighting.

## 🔧 Development

This theme was converted from the Zed editor Catppuccin Blur theme. The conversion process maps Zed's theme format to VS Code's color theme schema.

### Building from Source

```bash
# Clone the repository
git clone https://github.com/johngagefaulkner/catppuccin-blur-vscode.git
cd catppuccin-blur-vscode

# The themes are already generated, but you can regenerate them with:
python3 convert_to_vscode.py

# Package the extension (requires vsce)
npm install -g @vscode/vsce
vsce package
```

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

## 🙏 Credits

- Original Catppuccin theme: [Catppuccin](https://github.com/catppuccin/catppuccin)
- Zed Catppuccin Blur theme: [zed-catppuccin-blur](https://github.com/jenslys/zed-catppuccin-blur)

## 🐛 Issues

If you encounter any issues or have suggestions, please [open an issue](https://github.com/johngagefaulkner/catppuccin-blur-vscode/issues) on GitHub.
