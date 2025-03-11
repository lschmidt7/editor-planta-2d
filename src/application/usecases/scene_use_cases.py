from src.application.repositories import IPillarRepository, IWallRepository
from src.application.renders import IPillarRender, IWallRender

class RenderSceneUseCase:

    def __init__(self, pillar_repository: IPillarRepository, wall_repository: IWallRepository, pillar_render: IPillarRender, wall_render: IWallRender):
        self.pillar_repository = pillar_repository
        self.wall_repository = wall_repository
        self.pillar_render = pillar_render
        self.wall_render = wall_render
    
    def execute(self):
        pillars = self.pillar_repository.all()
        for pillar in pillars:
            self.pillar_render.render(pillar)
        walls = self.wall_repository.all()
        for wall in walls:
            self.wall_render.render(wall)