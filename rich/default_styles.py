from typing import Dict

from .style import Style

DEFAULT_STYLES: Dict[str, Style] = {
    "none": Style(),
    "reset": Style(
        color="default",
        bgcolor="default",
        dim=False,
        bold=False,
        italic=False,
        underline=False,
        blink=False,
        blink2=False,
        reverse=False,
        conceal=False,
        strike=False,
    ),
    "dim": Style(dim=True),
    "bright": Style(dim=False),
    "bold": Style(bold=True),
    "strong": Style(bold=True),
    "code": Style(reverse=True, bold=True),
    "italic": Style(italic=True),
    "emphasize": Style(italic=True),
    "underline": Style(underline=True),
    "blink": Style(blink=True),
    "blink2": Style(blink2=True),
    "reverse": Style(reverse=True),
    "strike": Style(strike=True),
    "black": Style(color="black"),
    "red": Style(color="red"),
    "green": Style(color="green"),
    "yellow": Style(color="yellow"),
    "magenta": Style(color="magenta"),
    "cyan": Style(color="cyan"),
    "white": Style(color="white"),
    "logging.keyword": Style(bold=True, color="yellow"),
    "logging.level.notset": Style(dim=True),
    "logging.level.debug": Style(color="green"),
    "logging.level.info": Style(color="blue"),
    "logging.level.warning": Style(color="red"),
    "logging.level.error": Style(color="red", bold=True),
    "logging.level.critical": Style(color="red", bold=True, reverse=True),
    "log.level": Style(),
    "log.time": Style(color="cyan", dim=True),
    "log.message": Style(),
    "log.path": Style(dim=True),
    "repr.str": Style(color="green", italic=False, bold=False),
    "repr.brace": Style(bold=True),
    "repr.tag_start": Style(bold=True),
    "repr.tag_name": Style(color="bright_magenta", bold=True),
    "repr.tag_contents": Style(color="default"),
    "repr.tag_end": Style(bold=True),
    "repr.attrib_name": Style(color="yellow", italic=True),
    "repr.attrib_equal": Style(bold=True),
    "repr.attrib_value": Style(color="magenta", italic=False),
    "repr.number": Style(color="blue", bold=True, italic=False),
    "repr.bool_true": Style(color="bright_green", italic=True),
    "repr.bool_false": Style(color="bright_red", italic=True),
    "repr.none": Style(color="magenta", italic=True),
    "repr.url": Style(underline=True, color="bright_blue", italic=False, bold=False),
    "repr.uuid": Style(color="bright_yellow", bold=False),
    "rule.line": Style(color="bright_green"),
    "rule.text": Style(),
    "prompt.choices": Style(color="magenta", bold=True),
    "prompt.default": Style(color="cyan", bold=True),
    "prompt.invalid": Style(color="red"),
    "prompt.invalid.choice": Style(color="red"),
    "scope.border": Style(color="blue"),
    "scope.key": Style(color="yellow", italic=True),
    "scope.key.special": Style(color="yellow", italic=True, dim=True),
    "scope.equals": Style(color="red"),
    "repr.path": Style(color="magenta"),
    "repr.filename": Style(color="bright_magenta"),
    "table.header": Style(bold=True),
    "table.footer": Style(bold=True),
    "table.cell": Style(),
    "table.title": Style(italic=True),
    "table.caption": Style(italic=True, dim=True),
    "traceback.text": Style(),
    "traceback.filename": Style(color="green"),
    "traceback.lineno": Style(bold=True, color="cyan"),
    "traceback.name": Style(color="yellow"),
    "traceback.exc_type": Style(color="bright_red", bold=True),
    "traceback.exc_value": Style(),
    "traceback.offset": Style(color="bright_red", bold=True),
    "bar.back": Style(color="grey23"),
    "bar.complete": Style(color="rgb(249,38,114)"),
    "bar.finished": Style(color="rgb(114,156,31)"),
    "bar.pulse": Style(color="rgb(249,38,114)"),
    "progress.description": Style(),
    "progress.filesize": Style(color="green"),
    "progress.filesize.total": Style(color="green"),
    "progress.download": Style(color="green"),
    "progress.percentage": Style(color="magenta"),
    "progress.remaining": Style(color="cyan"),
    "progress.data.speed": Style(color="red"),
}

MARKDOWN_STYLES = {
    "markdown.paragraph": Style(),
    "markdown.text": Style(),
    "markdown.emph": Style(italic=True),
    "markdown.strong": Style(bold=True),
    "markdown.code": Style(bgcolor="black", color="bright_white"),
    "markdown.code_block": Style(dim=True, color="cyan", bgcolor="black"),
    "markdown.block_quote": Style(color="magenta"),
    "markdown.list": Style(color="cyan"),
    "markdown.item": Style(),
    "markdown.item.bullet": Style(color="yellow", bold=True),
    "markdown.item.number": Style(color="yellow", bold=True),
    "markdown.hr": Style(color="yellow"),
    "markdown.h1.border": Style(),
    "markdown.h1": Style(bold=True),
    "markdown.h2": Style(bold=True, underline=True),
    "markdown.h3": Style(bold=True),
    "markdown.h4": Style(bold=True, dim=True),
    "markdown.h5": Style(underline=True),
    "markdown.h6": Style(italic=True),
    "markdown.h7": Style(italic=True, dim=True),
    "markdown.link": Style(color="bright_blue"),
    "markdown.link_url": Style(color="blue"),
}


DEFAULT_STYLES.update(MARKDOWN_STYLES)
