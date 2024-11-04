                        import random

                        from code.Background import Background
                        from code.Const import WIN_WIDTH, WIN_HEIGHT
                        from code.Enemy import Enemy
                        from code.Player import Player

                        class EntityFactory:

                            @staticmethod
                            def get_entity(entity_name: str):
                                # Aqui eu crio diferentes tipos de entidades com base no nome que eu passo.
                                match entity_name:
                                    case 'Level1Bg':
                                        list_bg = []
                                        # Para o background do nível 1, eu decido criar 7 imagens.
                                        for i in range(7):  
                                            # Eu adiciono cada imagem na posição inicial (0, 0) e também na posição à direita da tela (WIN_WIDTH, 0).
                                            list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                                            list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                                        return list_bg

                                    case 'Level2Bg':
                                        list_bg = []
                                        # Para o background do nível 2, eu opto por criar 5 imagens.
                                        for i in range(5):  
                                            # Eu adiciono cada imagem nas mesmas duas posições que usei antes.
                                            list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                                            list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                                        return list_bg

                                    case 'Level3Bg':
                                        list_bg = []
                                        # Para o background do nível 3, eu também crio 5 imagens.
                                        for i in range(5):  
                                            # Eu coloco as imagens nas duas posições, assim como fiz nos níveis anteriores.
                                            list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                                            list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
                                        return list_bg

                                    case 'Player1':
                                        # Aqui eu crio o jogador 1 na posição inicial, um pouco à direita e no meio da tela.
                                        return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

                                    case 'Player2':
                                        # Agora eu crio o jogador 2, que fica logo abaixo do jogador 1.
                                        return Player('Player2', (10, WIN_HEIGHT / 2 + 30))

                                    case 'Enemy1':
                                        # Eu crio o inimigo 1 em uma posição aleatória, começando fora da tela, à direita.
                                        return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

                                    case 'Enemy2':
                                        # Eu crio o inimigo 2 da mesma forma, também em uma posição aleatória fora da tela, à direita.
                                        return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

                                    case 'Enemy3':
                                        # Finalmente, eu crio o inimigo 3, assim como os outros, com uma posição aleatória.
                                        return Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
