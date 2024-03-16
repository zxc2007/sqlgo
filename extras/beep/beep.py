#!/usr/bin/env python
"""
# SQLGO License - Version 1.3

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
import time
import os
import sys
import simpleaudio as sa
import os
import sys
import platform
from pydub import AudioSegment
from pydub.playback import play



def find_beep_wav():
    module_directory = os.path.dirname(os.path.abspath(__file__))
    beep_wav_path = os.path.join(module_directory, 'beep.wav')
    return beep_wav_path if os.path.exists(beep_wav_path) else None


def beep():
    song = AudioSegment.from_wav(find_beep_wav())
    play(song)

if __name__ != '__main__':
    beep()