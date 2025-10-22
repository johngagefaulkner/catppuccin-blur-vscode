#!/usr/bin/env python3
"""
Convert Zed Catppuccin Blur themes to VS Code format.
This script takes Mocha and Espresso [Light] themes from the Zed theme file
and converts them to VS Code color theme format.
"""

import json
import os
from pathlib import Path


def convert_zed_to_vscode(zed_theme_data):
    """
    Convert a Zed theme to VS Code theme format.
    
    Args:
        zed_theme_data: Dictionary containing Zed theme data
    
    Returns:
        Dictionary in VS Code theme format
    """
    style = zed_theme_data['style']
    
    # VS Code theme structure
    vscode_theme = {
        "$schema": "vscode://schemas/color-theme",
        "name": zed_theme_data['name'].replace(' (Blur)', ''),
        "type": zed_theme_data.get('appearance', 'dark'),
        "colors": {},
        "tokenColors": []
    }
    
    # Map Zed colors to VS Code colors
    # The mapping is based on semantic similarity between Zed and VS Code color keys
    
    # Background colors
    if 'background' in style:
        vscode_theme['colors']['editor.background'] = style['background']
        vscode_theme['colors']['window.background'] = style['background']
    
    if 'editor.background' in style and style['editor.background'] != '#00000000':
        vscode_theme['colors']['editor.background'] = style['editor.background']
    
    # Surface colors
    if 'surface.background' in style:
        vscode_theme['colors']['sideBar.background'] = style['surface.background']
        vscode_theme['colors']['activityBar.background'] = style['surface.background']
    
    if 'elevated_surface.background' in style:
        vscode_theme['colors']['editorGroupHeader.tabsBackground'] = style['elevated_surface.background']
        vscode_theme['colors']['panel.background'] = style['elevated_surface.background']
    
    # Status bar and title bar
    if 'status_bar.background' in style:
        vscode_theme['colors']['statusBar.background'] = style['status_bar.background']
        vscode_theme['colors']['statusBar.noFolderBackground'] = style['status_bar.background']
        vscode_theme['colors']['statusBar.debuggingBackground'] = style['status_bar.background']
    
    if 'title_bar.background' in style:
        vscode_theme['colors']['titleBar.activeBackground'] = style['title_bar.background']
    
    if 'title_bar.inactive_background' in style:
        vscode_theme['colors']['titleBar.inactiveBackground'] = style['title_bar.inactive_background']
    
    # Text colors
    if 'text' in style:
        vscode_theme['colors']['foreground'] = style['text']
        vscode_theme['colors']['editor.foreground'] = style['text']
        vscode_theme['colors']['sideBar.foreground'] = style['text']
        vscode_theme['colors']['activityBar.foreground'] = style['text']
    
    if 'text.muted' in style:
        vscode_theme['colors']['descriptionForeground'] = style['text.muted']
    
    if 'text.accent' in style:
        vscode_theme['colors']['textLink.foreground'] = style['text.accent']
    
    # Border colors
    if 'border' in style:
        vscode_theme['colors']['contrastBorder'] = style['border']
        vscode_theme['colors']['panel.border'] = style['border']
        vscode_theme['colors']['sideBar.border'] = style['border']
    
    if 'border.focused' in style:
        vscode_theme['colors']['focusBorder'] = style['border.focused']
    
    # Tabs
    if 'tab.active_background' in style:
        vscode_theme['colors']['tab.activeBackground'] = style['tab.active_background']
    
    if 'tab.inactive_background' in style:
        vscode_theme['colors']['tab.inactiveBackground'] = style['tab.inactive_background']
    
    if 'tab_bar.background' in style:
        vscode_theme['colors']['editorGroupHeader.tabsBackground'] = style['tab_bar.background']
    
    # Editor elements
    if 'editor.active_line.background' in style:
        vscode_theme['colors']['editor.lineHighlightBackground'] = style['editor.active_line.background']
    
    if 'editor.line_number' in style:
        vscode_theme['colors']['editorLineNumber.foreground'] = style['editor.line_number']
    
    if 'editor.active_line_number' in style:
        vscode_theme['colors']['editorLineNumber.activeForeground'] = style['editor.active_line_number']
    
    if 'editor.gutter.background' in style:
        vscode_theme['colors']['editorGutter.background'] = style['editor.gutter.background']
    
    # Selection and highlights
    if 'element.selected' in style:
        vscode_theme['colors']['editor.selectionBackground'] = style['element.selected']
        vscode_theme['colors']['list.activeSelectionBackground'] = style['element.selected']
    
    if 'element.hover' in style:
        vscode_theme['colors']['list.hoverBackground'] = style['element.hover']
    
    # Scrollbar
    if 'scrollbar.thumb.background' in style:
        vscode_theme['colors']['scrollbarSlider.background'] = style['scrollbar.thumb.background']
    
    if 'scrollbar.thumb.hover_background' in style:
        vscode_theme['colors']['scrollbarSlider.hoverBackground'] = style['scrollbar.thumb.hover_background']
    
    if 'scrollbar.track.background' in style:
        vscode_theme['colors']['scrollbar.shadow'] = style['scrollbar.track.background']
    
    # Terminal
    if 'terminal.background' in style and style['terminal.background'] != '#00000000':
        vscode_theme['colors']['terminal.background'] = style['terminal.background']
    
    if 'terminal.foreground' in style:
        vscode_theme['colors']['terminal.foreground'] = style['terminal.foreground']
    
    # Terminal ANSI colors
    ansi_mapping = {
        'terminal.ansi.black': 'terminal.ansiBlack',
        'terminal.ansi.red': 'terminal.ansiRed',
        'terminal.ansi.green': 'terminal.ansiGreen',
        'terminal.ansi.yellow': 'terminal.ansiYellow',
        'terminal.ansi.blue': 'terminal.ansiBlue',
        'terminal.ansi.magenta': 'terminal.ansiMagenta',
        'terminal.ansi.cyan': 'terminal.ansiCyan',
        'terminal.ansi.white': 'terminal.ansiWhite',
        'terminal.ansi.bright_black': 'terminal.ansiBrightBlack',
        'terminal.ansi.bright_red': 'terminal.ansiBrightRed',
        'terminal.ansi.bright_green': 'terminal.ansiBrightGreen',
        'terminal.ansi.bright_yellow': 'terminal.ansiBrightYellow',
        'terminal.ansi.bright_blue': 'terminal.ansiBrightBlue',
        'terminal.ansi.bright_magenta': 'terminal.ansiBrightMagenta',
        'terminal.ansi.bright_cyan': 'terminal.ansiBrightCyan',
        'terminal.ansi.bright_white': 'terminal.ansiBrightWhite',
    }
    
    for zed_key, vscode_key in ansi_mapping.items():
        if zed_key in style:
            vscode_theme['colors'][vscode_key] = style[zed_key]
    
    # Error, warning, info, success
    if 'error.background' in style:
        vscode_theme['colors']['editorError.background'] = style['error.background']
    
    if 'error' in style:
        vscode_theme['colors']['editorError.foreground'] = style['error']
    
    if 'warning.background' in style:
        vscode_theme['colors']['editorWarning.background'] = style['warning.background']
    
    if 'warning' in style:
        vscode_theme['colors']['editorWarning.foreground'] = style['warning']
    
    if 'info.background' in style:
        vscode_theme['colors']['editorInfo.background'] = style['info.background']
    
    if 'info' in style:
        vscode_theme['colors']['editorInfo.foreground'] = style['info']
    
    # Git decorations
    if 'version_control.added' in style:
        vscode_theme['colors']['gitDecoration.addedResourceForeground'] = style['version_control.added']
    
    if 'version_control.modified' in style:
        vscode_theme['colors']['gitDecoration.modifiedResourceForeground'] = style['version_control.modified']
    
    if 'version_control.deleted' in style:
        vscode_theme['colors']['gitDecoration.deletedResourceForeground'] = style['version_control.deleted']
    
    if 'version_control.ignored' in style:
        vscode_theme['colors']['gitDecoration.ignoredResourceForeground'] = style['version_control.ignored']
    
    if 'version_control.conflict' in style:
        vscode_theme['colors']['gitDecoration.conflictingResourceForeground'] = style['version_control.conflict']
    
    # Add token colors for syntax highlighting
    if 'syntax' in style and isinstance(style['syntax'], dict):
        syntax = style['syntax']
        token_colors = []
        
        # Map common syntax tokens
        syntax_map = {
            'comment': {'scope': ['comment'], 'settings': {}},
            'string': {'scope': ['string'], 'settings': {}},
            'number': {'scope': ['constant.numeric'], 'settings': {}},
            'keyword': {'scope': ['keyword'], 'settings': {}},
            'function': {'scope': ['entity.name.function'], 'settings': {}},
            'type': {'scope': ['entity.name.type', 'support.type'], 'settings': {}},
            'variable': {'scope': ['variable'], 'settings': {}},
            'operator': {'scope': ['keyword.operator'], 'settings': {}},
        }
        
        for token_name, token_def in syntax_map.items():
            if token_name in syntax:
                color_data = syntax[token_name]
                if isinstance(color_data, dict):
                    if 'color' in color_data:
                        token_def['settings']['foreground'] = color_data['color']
                    if 'font_weight' in color_data and color_data['font_weight'] is not None:
                        token_def['settings']['fontStyle'] = 'bold' if color_data['font_weight'] > 400 else 'normal'
                elif isinstance(color_data, str):
                    token_def['settings']['foreground'] = color_data
                
                if token_def['settings']:
                    token_colors.append(token_def)
        
        vscode_theme['tokenColors'] = token_colors
    
    return vscode_theme


def main():
    """Main conversion function."""
    # Paths
    repo_root = Path(__file__).parent
    zed_theme_path = repo_root / 'themes' / 'catppuccin-blur.json'
    vscode_themes_dir = repo_root / 'themes'
    
    # Ensure themes directory exists
    vscode_themes_dir.mkdir(exist_ok=True)
    
    # Load Zed themes
    print(f"Loading Zed themes from {zed_theme_path}")
    with open(zed_theme_path, 'r') as f:
        zed_data = json.load(f)
    
    # Find and convert Mocha and Espresso [Light] themes
    themes_to_convert = [
        ('Mocha', 'mocha-light'),
        ('Espresso', 'espresso-light')
    ]
    
    for theme_search, output_name in themes_to_convert:
        print(f"\nLooking for {theme_search} [Light] theme...")
        
        for theme in zed_data['themes']:
            if theme_search in theme['name'] and '[Light]' in theme['name']:
                print(f"  Found: {theme['name']}")
                
                # Convert to VS Code format
                vscode_theme = convert_zed_to_vscode(theme)
                
                # Save to file
                output_path = vscode_themes_dir / f'catppuccin-blur-{output_name}.json'
                with open(output_path, 'w') as f:
                    json.dump(vscode_theme, f, indent=2)
                
                print(f"  Saved to: {output_path}")
                break
        else:
            print(f"  WARNING: {theme_search} [Light] theme not found!")
    
    print("\nConversion complete!")


if __name__ == '__main__':
    main()
