from bs4 import BeautifulSoup
from flask_flatpages import Page
from werkzeug.utils import cached_property

from src.processors.processors import process_code_blocks


class MyPage(Page):
    @cached_property
    def unprocessed_html(self):
        return self.html_renderer(self)

    @cached_property
    def parsed_html(self):
        return process_code_blocks(BeautifulSoup(self.unprocessed_html, 'html.parser'))

    @cached_property
    def html(self):
        """The content of the page, rendered as HTML by the configured
        renderer.
        """
        return unicode(str(self.parsed_html), "utf8").replace("<br>", "<br/>")
