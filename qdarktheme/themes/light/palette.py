"""Module loading QPalette."""
from qdarktheme.qtpy.QtGui import QColor, QPalette

_palette = QPalette()

# base
_palette.setColor(QPalette.ColorRole.WindowText, QColor("#4d4d4d"))
_palette.setColor(QPalette.ColorRole.Button, QColor("#f6f6f6"))
_palette.setColor(QPalette.ColorRole.Text, QColor("#888888"))
_palette.setColor(QPalette.ColorRole.ButtonText, QColor("#127def"))
_palette.setColor(QPalette.ColorRole.Base, QColor("#f6f6f6"))
_palette.setColor(QPalette.ColorRole.Window, QColor("#f6f6f6"))
_palette.setColor(QPalette.ColorRole.Highlight, QColor("#127def"))
_palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#f6f6f6"))
_palette.setColor(QPalette.ColorRole.Link, QColor("#f6f6f6"))
_palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#e9e9e9"))
_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#ffffff"))
_palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#4d4d4d"))
_palette.setColor(QPalette.ColorRole.LinkVisited, QColor("#660098"))
_palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#ffffff"))
_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#4d4d4d"))
if hasattr(QPalette.ColorRole, "Foreground"):
    _palette.setColor(QPalette.ColorRole.Foreground, QColor("#4d4d4d"))  # type: ignore
if hasattr(QPalette.ColorRole, "PlaceholderText"):
    _palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("#696969"))

_palette.setColor(QPalette.ColorRole.Light, QColor("#dadada"))
_palette.setColor(QPalette.ColorRole.Midlight, QColor("#dadada"))
_palette.setColor(QPalette.ColorRole.Dark, QColor("#4d4d4d"))
_palette.setColor(QPalette.ColorRole.Mid, QColor("#dadada"))
_palette.setColor(QPalette.ColorRole.Shadow, QColor("#dadada"))

# disabled
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor("#bababa"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor("#bababa"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor("#dadada"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor("#dadada"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor("#bababa"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Link, QColor("#bababa"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.LinkVisited, QColor("#bababa"))

# inactive
_palette.setColor(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, QColor("#e4e4e4"))

PALETTE = _palette
