"""Module loading QPalette."""
from qdarktheme.qtpy.QtGui import QColor, QPalette

_palette = QPalette()

# base
_palette.setColor(QPalette.ColorRole.WindowText, QColor("#e4e4e4"))
_palette.setColor(QPalette.ColorRole.Button, QColor("#202020"))
_palette.setColor(QPalette.ColorRole.Text, QColor("#efefef"))
_palette.setColor(QPalette.ColorRole.ButtonText, QColor("#d2aa02"))
_palette.setColor(QPalette.ColorRole.Base, QColor("#202020"))
_palette.setColor(QPalette.ColorRole.Window, QColor("#202020"))
_palette.setColor(QPalette.ColorRole.Highlight, QColor("#d2aa02"))
_palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#202020"))
_palette.setColor(QPalette.ColorRole.Link, QColor("#202020"))
_palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#303030"))
_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#292929"))
_palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#e4e4e4"))
_palette.setColor(QPalette.ColorRole.LinkVisited, QColor("#c58af8"))
_palette.setColor(QPalette.ColorRole.ToolTipText, QColor("#292929"))
_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor("#e4e4e4"))
if hasattr(QPalette.ColorRole, "Foreground"):
    _palette.setColor(QPalette.ColorRole.Foreground, QColor("#e4e4e4"))  # type: ignore
if hasattr(QPalette.ColorRole, "PlaceholderText"):
    _palette.setColor(QPalette.ColorRole.PlaceholderText, QColor("#8a8a8a"))

_palette.setColor(QPalette.ColorRole.Light, QColor("#404040"))
_palette.setColor(QPalette.ColorRole.Midlight, QColor("#404040"))
_palette.setColor(QPalette.ColorRole.Dark, QColor("#e4e4e4"))
_palette.setColor(QPalette.ColorRole.Mid, QColor("#404040"))
_palette.setColor(QPalette.ColorRole.Shadow, QColor("#404040"))

# disabled
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor("#696969"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor("#696969"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor("#404040"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor("#535353"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor("#696969"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Link, QColor("#696969"))
_palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.LinkVisited, QColor("#696969"))

# inactive
_palette.setColor(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, QColor("#393939"))

PALETTE = _palette
