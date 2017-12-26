#!/usr/bin/env python3

import time
import pygame.mixer as mixer

def play(filepath):
  mixer.init()
  mixer.music.load(filepath)
  mixer.music.play(0)
