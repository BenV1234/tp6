import random
import arcade

from game_state import GameState
from attack_animation import AttackAnimation, AttackType

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600  

CHOICE_IMAGES = {
   AttackType.ROCK: "assets/srock.png",
   AttackType.PAPER: "assets/spaper.png",
   AttackType.SCISSORS: "assets/scissors.png"
}
IMAGES_X = {
   AttackType.ROCK: SCREEN_WIDTH // 4 - 100,
   AttackType.PAPER: SCREEN_WIDTH // 4,
   AttackType.SCISSORS: SCREEN_WIDTH // 4 + 100
}
IMAGES_X_PC = SCREEN_WIDTH * 3 // 4
IMAGES_Y = SCREEN_HEIGHT // 2 - 150
IMAGES_WH = 60

TEXT_TITLE = "Roche, Papier, Ciseaux"
TEXT_TAP_IMAGE = "Appuyer sur une image pour faire une attaque!"
TEXT_START_NEW_GAME = "Appuier sur 'ESPACE' pour débuter une nouvelle partie!"
TEXT_START_NEW_ROUND = "Appuie sur 'ESPACE' pour commencer une nouvelle ronde!"
TEXT_START_GAME = "Appuyer sur une image pour faire une attaque"

TEXT_EQUALITY = "Égalité!"
TEXT_YOU_WIN_ROUND = "Vous avez gangé la ronde!"
TEXT_COMPUTER_WIN_ROUND = "L’ordinateur à gagne la ronde!"
TEXT_YOU_WIN_GAME = "Vous avez gangé la partie!"
TEXT_COMPUTER_WIN_GAME = "L’ordinateur à gagné la partie!"
TEXT_PLAYER_SCORE = "Le pontage du joueur est"
TEXT_COMPUTER_SCORE = "Le pontage de ordinateur est"
TEXT_GAME_OVER = "La partie est terminée."

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        # Create the SpriteList
        self.image_sprites = arcade.SpriteList()

        #Create choice variable
        self.player_choice = False

        # Create Sprite instance to the SpriteList
        self.player_sprite = arcade.Sprite("assets/faceBeard.png",0.2, SCREEN_WIDTH // 4,SCREEN_HEIGHT // 2 - 30)
        self.computer_sprite = arcade.Sprite("assets/compy.png", 1, 3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 30)

        # Append the instance to the SpriteList
        self.image_sprites.append(self.player_sprite)
        self.image_sprites.append(self.computer_sprite)

        # Create rectangles
        self.rect_rock = arcade.shape_list.create_rectangle(IMAGES_X[AttackType.ROCK], IMAGES_Y, IMAGES_WH, IMAGES_WH, arcade.color.RED, 1, 00, False )
        self.rect_paper = arcade.shape_list.create_rectangle(IMAGES_X[AttackType.PAPER], IMAGES_Y, IMAGES_WH, IMAGES_WH, arcade.color.RED, 1, 00, False )
        self.rect_scissors = arcade.shape_list.create_rectangle(IMAGES_X[AttackType.SCISSORS], IMAGES_Y, IMAGES_WH, IMAGES_WH, arcade.color.RED, 1, 00, False )
        self.rect_computer = arcade.shape_list.create_rectangle(3 * SCREEN_WIDTH // 4, IMAGES_Y, IMAGES_WH, IMAGES_WH, arcade.color.RED, 1, 00, False )

        # Create Sprite instance to the SpriteList
        self.rock = AttackAnimation(AttackType.ROCK)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.scissors = AttackAnimation(AttackType.SCISSORS)

        # Create Text for title
        self.title_text = arcade.Text(TEXT_TITLE, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 70, arcade.color.YELLOW, 48, anchor_x="center")

        # Create Text for message
        self.message = arcade.Text(
            "",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 150,
            arcade.color.WHITE,
            24,
            width=SCREEN_WIDTH,
            multiline=True,
            align="center",
            anchor_x="center"
        )
        self.second_message = arcade.Text(
            "",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 150,
            arcade.color.WHITE,
            24,
            width=SCREEN_WIDTH,
            multiline=True,
            align="center",
            anchor_x="center"
        )
        # Create Text for status
        self.status = arcade.Text(
            "",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 230,
            arcade.color.WHITE,
            24,
            width=SCREEN_WIDTH,
            multiline=True,
            align="center",
            anchor_x="center"
        )
        # self.game_state_text = arcade.Text("", SCREEN_WIDTH // 2, 10, arcade.color.WHITE, 16, anchor_x="center")

        # Create Text for scores
        self.player_score_text = arcade.Text("", SCREEN_WIDTH // 4,50, arcade.color.WHITE, 16, anchor_x="center")
        self.computer_score_text = arcade.Text("", 3 * SCREEN_WIDTH // 4, 50, arcade.color.WHITE, 16, anchor_x="center")

        # Create variables
        self.game_state = GameState.NOT_STARTED
        self.player_score = 0
        self.computer_score = 0
        self.player_attack_type = None
        self.computer_attack_type = None
        self.attack_sprites = arcade.SpriteList()

        self.setup()

        

    def setup(self):
        """Initialise les variables du jeu."""
        self.game_state = GameState.NOT_STARTED
        self.player_score = 0
        self.computer_score = 0

        self.attack_sprites = arcade.SpriteList()
        self.player_attack_type = None
        self.computer_attack_type = None

        self.message.color = arcade.color.WHITE
        self.message.font_size = 24
        self.message.text = TEXT_START_NEW_GAME
        self.second_message.text = TEXT_START_GAME
        

        
        self.player_score_text.text = f"{TEXT_PLAYER_SCORE} {self.player_score}"
       
        self.computer_score_text.text = f"{TEXT_COMPUTER_SCORE} {self.computer_score}"

    def on_draw(self):

        # Clear the screen
        self.clear()

        self.rock.center_x = 100
        self.rock.center_y = 150
        self.paper.center_x = 200
        self.paper.center_y = 150
        self.scissors.center_x = 300
        self.scissors.center_y = 150

        # Draw texts
        self.title_text.draw()

        self.status.draw()
        

        # Draw scores
        self.player_score_text.text = f"{TEXT_PLAYER_SCORE} {self.player_score}"
        self.computer_score_text.text = f"{TEXT_COMPUTER_SCORE} {self.computer_score}"
        self.player_score_text.draw()
        self.computer_score_text.draw()

        # Draw sprites
        self.image_sprites.draw()
        self.attack_sprites.draw()

        # Draw rectangles
        self.rect_rock.draw()
        self.rect_paper.draw()
        self.rect_scissors.draw()
        self.rect_computer.draw()

        if self.game_state == GameState.NOT_STARTED:
            self.message.draw()
        elif self.game_state == GameState.ROUND_ACTIVE:
            self.message.draw()



    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:
            

            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.ROUND_DONE:
                self.player_attack_type = None
                self.computer_attack_type = None
                self.player_choice = False
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.GAME_OVER:
                self.setup()
                self.game_state = GameState.ROUND_ACTIVE


            """Append the instance to the SpriteList to draw attack_sprites"""
            self.attack_sprites.clear()
            self.attack_sprites.append(self.rock)
            self.attack_sprites.append(self.paper)
            self.attack_sprites.append(self.scissors)

            self.status.text = ""
            

    def on_mouse_press(self, x, y, button, modifiers):
        """Manages mouse clicks to choose an attack."""
       
        if self.game_state == GameState.ROUND_ACTIVE:

            if self.rock.collides_with_point((x, y)):
                self.player_attack_type = AttackType.ROCK
                self.player_choice = True
            elif self.paper.collides_with_point((x, y)):
                self.player_attack_type = AttackType.PAPER
                self.player_choice = True
            elif self.scissors.collides_with_point((x, y)):
                self.player_attack_type = AttackType.SCISSORS
                self.player_choice = True



    def on_update(self, delta_time):
        """Updates game logic."""
        if self.game_state == GameState.ROUND_ACTIVE and self.player_choice:
            pc_attack = random.randint(0, 2)
            if pc_attack == 0:
                self.computer_attack_type = AttackType.ROCK
            elif pc_attack == 1:
                self.computer_attack_type = AttackType.PAPER
            else:
                self.computer_attack_type = AttackType.SCISSORS

            self.rock.on_update()
            self.paper.on_update()
            self.scissors.on_update()

            if self.computer_attack_type == AttackType.ROCK:
                if self.player_attack_type == AttackType.ROCK:
                    pass
                if self.player_attack_type == AttackType.PAPER:

                    self.player_score += 1
                if self.player_attack_type == AttackType.SCISSORS:

                    self.computer_score += 1
            if self.computer_attack_type == AttackType.PAPER:
                if self.player_attack_type == AttackType.ROCK:

                    self.computer_score += 1
                if self.player_attack_type == AttackType.PAPER:
                    pass
                if self.player_attack_type == AttackType.SCISSORS:

                    self.player_score += 1
            if self.computer_attack_type == AttackType.SCISSORS:
                if self.player_attack_type == AttackType.ROCK:

                    self.player_score += 1
                if self.player_attack_type == AttackType.PAPER:

                    self.computer_score += 1
                if self.player_attack_type == AttackType.SCISSORS:
                    pass
            self.game_state = GameState.ROUND_DONE

            if self.player_score >= 3 or self.computer_score >= 3:
                self.game_state = GameState.GAME_OVER






def main():

    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
