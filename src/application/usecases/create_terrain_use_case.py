from src.enterprise.terrain_entity import TerrainEntity

class CreateTerrainUseCase:

    def __init__(self):
        pass

    def execute(largura: int, comprimento: int, pixel_por_metro: int) -> TerrainEntity:
        terrain_entity = TerrainEntity(largura, comprimento, pixel_por_metro)
        return terrain_entity