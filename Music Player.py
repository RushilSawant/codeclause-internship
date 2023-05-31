import pygame
import os


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)


pygame.init()


win_width = 600
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Music Player")


font = pygame.font.Font(None, 40)


clock = pygame.time.Clock()


music_dir = "C:/Users/Rushil Sawant/Desktop/SKITS"


audio_files = [file for file in os.listdir(music_dir) if file.endswith((".mp3", ".wav"))]


current_song_index = 0


def load_song():
    pygame.mixer.music.load(os.path.join(music_dir, audio_files[current_song_index]))


def play_song():
    pygame.mixer.music.play()


def pause_song():
    pygame.mixer.music.pause()


def unpause_song():
    pygame.mixer.music.unpause()


def stop_song():
    pygame.mixer.music.stop()


def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(audio_files)
    load_song()
    play_song()


def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(audio_files)
    load_song()
    play_song()


def display_song_info():
    text = font.render(audio_files[current_song_index], True, BLACK)
    text_rect = text.get_rect(center=(win_width // 2, win_height // 2))
    win.blit(text, text_rect)



def adjust_volume(delta):
    current_volume = pygame.mixer.music.get_volume()
    new_volume = max(0, min(current_volume + delta, 1))
    pygame.mixer.music.set_volume(new_volume)


def run_music_player():
    running = True
    paused = False

    while running:
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if paused:
                        unpause_song()
                        paused = False
                    else:
                        pause_song()
                        paused = True
                elif event.key == pygame.K_s:
                    stop_song()
                elif event.key == pygame.K_RIGHT:
                    next_song()
                elif event.key == pygame.K_LEFT:
                    previous_song()
                elif event.key == pygame.K_UP:
                    adjust_volume(0.1)
                elif event.key == pygame.K_DOWN:
                    adjust_volume(-0.1)


        win.fill(WHITE)


        display_song_info()


        pygame.display.flip()


    pygame.quit()


load_song()
play_song()
run_music_player()
