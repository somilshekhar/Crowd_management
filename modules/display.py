import pygame
import cv2

def init_window():
    pygame.init()
    screen = pygame.display.set_mode((416, 320))
    pygame.display.set_caption("People Counter")
    clock = pygame.time.Clock()
    return screen, clock

def draw_ui(screen, frame, enter_count, exit_count):
    # Draw vertical red line
    cv2.line(frame, (208, 0), (208, 320), (0, 0, 255), 2)

    # Draw text
    cv2.putText(frame, f"Entered: {enter_count}", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f"Exited: {exit_count}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Convert to RGB and show in pygame
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    surf = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))
    screen.blit(surf, (0, 0))
    pygame.display.flip()
