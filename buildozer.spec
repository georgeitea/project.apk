[app]

# Το όνομα του φακέλου / πακέτου της εφαρμογής
title = GDREMOTEHUB
package.name = mykivyapp
package.domain = org.test

# Το βασικό αρχείο Python (βάλε το όνομα του .py που έχεις)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
main.py = main.py

# Έκδοση (βάλε ό,τι θέλεις)
version = 0.1

# Απαιτούμενα πακέτα (Kivy + Python3 + socket είναι built-in)
requirements = python3,kivy

# Bootstrap system
bootstrap = sdl2

# Υποστηριζόμενες αρχιτεκτονικές (ARM για Android)
arch = armeabi-v7a, arm64-v8a

# Ελάχιστη και μέγιστη API έκδοση Android
android.minapi = 23
android.api = 31

# Εικονίδια (αν δεν έχεις, αγνόησέ το)
# icon.filename = %(source.dir)s/data/icon.png

# Κατάλογος για build
build_dir = .buildozer

# Fullscreen
fullscreen = 1


[buildozer]

log_level = 2
warn_on_root = 1
