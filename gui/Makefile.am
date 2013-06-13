dist_bin_SCRIPTS = gameconqueror
dist_gameconqueror_DATA = GameConqueror.xml GameConqueror_128x128.png GameConqueror_72x72.png
dist_gameconqueror_DATA += backend*so consts*so misc*so hexview*so GameConqueror*so main.py
dist_icons_DATA = GameConqueror_128x128.png GameConqueror_72x72.png
dist_desktop_DATA = GameConqueror.desktop
dist_man_MANS = gameconqueror.1
dist_doc_DATA = README TODO COPYING
EXTRA_DIST = gameconqueror.in consts.pyx.in

gameconquerordir=$(datadir)/gameconqueror
iconsdir=$(datadir)/pixmaps
desktopdir=$(datadir)/applications

all: gui

gui:
	python3 setup.py build_ext --inplace
	if [ -d build ]; then rm -r build; fi
