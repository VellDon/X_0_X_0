from web.module import App
from web.route import Route_web
from web.mapper import Mapper_web
from domain.service import Service
from datasource.repository import Repository
from datasource.mapper import Mapper_rep

class Content:
    def __init__(self):
        self.mapper_rep = Mapper_rep()
        self.repository = Repository()
        self.service = Service(self.repository, self.mapper_rep)
        self.web_mapper = Mapper_web()
        self.web_bp = Route_web(self.web_mapper, self.service)
        self.server = App(self.web_bp.get_bp())
