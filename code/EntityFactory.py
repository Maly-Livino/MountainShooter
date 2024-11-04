                import random

                from code.Background import Background
                from code.Const import WIND_WIDTH, WIND_HEIGHT
                from code.Enemy import Enemy
                from code.Player import Player


                class EntityFactory:

                    @staticmethod
                    def get_entity(entity_name: str):
                        match entity_name:
                            case 'Level1Bg':
                                list_bg = []
                                for i in range(7):  # level1bg images number
                                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                                    list_bg.append(Background(f'Level1Bg{i}', (WIND_WIDTH, 0)))
                                return list_bg
                            case 'Level2Bg':
                                list_bg = []
                                for i in range(5):  # level2bg images number
                                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                                    list_bg.append(Background(f'Level2Bg{i}', (WIND_WIDTH, 0)))
                                return list_bg
                            case 'Level3Bg':
                                list_bg = []
                                for i in range(5):  # level3bg images number
                                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                                    list_bg.append(Background(f'Level3Bg{i}', (WIND_WIDTH, 0)))
                                return list_bg
                            case 'Player1':
                                return Player('Player1', (10, WIND_HEIGHT / 2 - 30))
                            case 'Player2':
                                return Player('Player2', (10, WIND_HEIGHT / 2 + 30))
                            case 'Enemy1':
                                return Enemy('Enemy1', (WIND_WIDTH + 10, random.randint(40, WIND_HEIGHT - 40)))
                            case 'Enemy2':
                                return Enemy('Enemy2', (WIND_WIDTH + 10, random.randint(40, WIND_HEIGHT - 40)))
                            case 'Enemy3':
                                return Enemy('Enemy3', (WIND_WIDTH + 10, random.randint(40, WIND_HEIGHT - 40)))