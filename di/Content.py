from web.module import App
from web.route import Route_web
from web.mapper import Mapper_web
from web.model import Model_web


class Content:
    def __init__(self):
        self.web_mapper = Mapper_web()
        self.web_bp = Route_web(self.web_mapper)
        self.server = App(self.web_bp.get_bp())
