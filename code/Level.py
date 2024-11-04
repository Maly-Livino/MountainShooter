                import random
                import sys

                import pygame
                from pygame import Surface, Rect
                from pygame.font import Font

                # Aqui, eu importo constantes e classes que vou usar no jogo.
                from code.Const import C_WHITE, WIND_HEIGHT, MENU_OPTION, EVENT_ENEMY, EVENT_TIMEOUT, TIMEOUT_STEP, SPAWN_TIME, \
                    TIMEOUT_LEVEL, C_GREEN, C_CYAN
                from code.Enemy import Enemy
                from code.Entity import Entity
                from code.EntityFactory import EntityFactory
                from code.EntityMediator import EntityMediator
                from code.Player import Player


                class Level:
                    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
                        # No início, eu defino a duração do nível. Para o Level 3, é o dobro do normal.
                        if name == 'Level3':
                            self.timeout = TIMEOUT_LEVEL * 2  # Duração em dobro para o Level 3
                        else:
                            self.timeout = TIMEOUT_LEVEL  # Para os outros níveis, uso o tempo padrão.

                        # Eu guardo a janela do jogo e outras informações.
                        self.window = window
                        self.name = name
                        self.game_mode = game_mode
                        self.entity_list: list[Entity] = []  # Aqui eu crio uma lista para armazenar as entidades do nível.

                        # Eu adiciono o background do nível na lista de entidades.
                        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))

                        # Eu crio o jogador 1 e atribuo a pontuação a ele.
                        player = EntityFactory.get_entity('Player1')
                        player.score = player_score[0]
                        self.entity_list.append(player)  # Eu adiciono o jogador 1 na lista de entidades.

                        # Se o modo de jogo permitir, eu também adiciono o jogador 2.
                        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
                            player = EntityFactory.get_entity('Player2')
                            player.score = player_score[1]
                            self.entity_list.append(player)  # Eu adiciono o jogador 2 na lista.

                        # Eu configuro um timer para os eventos de inimigos e tempo.
                        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
                        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # Timer a cada 100ms

                    def run(self, player_score: list[int]):
                        # Aqui eu carrego a música do nível e começo a tocá-la.
                        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
                        pygame.mixer_music.set_volume(0.3)
                        pygame.mixer_music.play(-1)  # A música toca em loop.

                        clock = pygame.time.Clock()  # Eu crio um relógio para controlar a taxa de quadros.
                        while True:
                            clock.tick(60)  # O jogo roda a 60 quadros por segundo.

                            # Aqui eu desenho cada entidade na tela e faço elas se moverem.
                            for ent in self.entity_list:
                                self.window.blit(source=ent.surf, dest=ent.rect)  # Eu desenhei a entidade na janela.
                                ent.move()  # Eu faço a entidade se mover.

                                # Se a entidade for um jogador ou um inimigo, eu verifico se ela atira.
                                if isinstance(ent, (Player, Enemy)):
                                    shoot = ent.shoot()  # A entidade tenta atirar.
                                    if shoot is not None:  # Se há um tiro, eu adiciono à lista de entidades.
                                        self.entity_list.append(shoot)

                                # Eu mostro informações sobre o jogador 1 na tela.
                                if ent.name == 'Player1':
                                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))
                                # Eu mostro informações sobre o jogador 2, se existir.
                                if ent.name == 'Player2':
                                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (10, 45))

                            # Aqui eu verifico os eventos que ocorrem na janela do jogo.
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:  # Se o usuário fechar a janela, eu encerro o jogo.
                                    pygame.quit()
                                    sys.exit()

                                # Aqui eu crio inimigos de acordo com o nível.
                                if event.type == EVENT_ENEMY:
                                    if self.name == 'Level3':
                                        # No Level 3, só crio inimigos do tipo 'Enemy3'.
                                        self.entity_list.append(EntityFactory.get_entity('Enemy3'))
                                    else:
                                        # Nos outros níveis, eu escolho aleatoriamente entre 'Enemy1' e 'Enemy2'.
                                        choice = random.choice(('Enemy1', 'Enemy2'))
                                        self.entity_list.append(EntityFactory.get_entity(choice))

                                # Aqui eu verifico o tempo e atualizo a pontuação dos jogadores quando o tempo acaba.
                                if event.type == EVENT_TIMEOUT:
                                    self.timeout -= TIMEOUT_STEP  # Eu reduzo o tempo restante.
                                    if self.timeout == 0:  # Se o tempo acabar:
                                        for ent in self.entity_list:
                                            if isinstance(ent, Player) and ent.name == 'Player1':
                                                player_score[0] = ent.score  # Eu atualizo a pontuação do jogador 1.
                                            if isinstance(ent, Player) and ent.name == 'Player2':
                                                player_score[1] = ent.score  # Eu atualizo a pontuação do jogador 2.
                                        return True  # O nível terminou.

                                # Aqui eu verifico se ainda há jogadores vivos.
                                found_player = False
                                for ent in self.entity_list:
                                    if isinstance(ent, Player):
                                        found_player = True  # Eu encontrei um jogador.

                                if not found_player:
                                    return False  # Se não houver jogadores, o jogo termina.

                            # Aqui eu mostro algumas informações na tela, como o tempo restante e a quantidade de entidades.
                            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
                            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIND_HEIGHT - 35))
                            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIND_HEIGHT - 20))
                            pygame.display.flip()  # Eu atualizo a tela.

                            # Aqui eu verifico colisões entre as entidades e a saúde delas.
                            EntityMediator.verify_collision(entity_list=self.entity_list)
                            EntityMediator.verify_health(entity_list=self.entity_list)

                    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
                        # Aqui eu crio uma função para desenhar texto na tela.
                        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
                        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
                        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
                        self.window.blit(source=text_surf, dest=text_rect)  # Eu desenho o texto na janela.
