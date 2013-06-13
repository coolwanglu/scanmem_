#!/usr/bin/env python3
import GameConqueror
from gi.repository import Gdk
from gi.repository import GObject

GObject.threads_init()
Gdk.threads_init()
GameConqueror.GameConqueror().main()
