.DEFAULT_GOAL := default
proj = "plugin.video.tide"
version = "0.0.5"

default:
	git archive --prefix=$(proj)/ master -o $(proj)-$(version).zip

clean:
	rm *.zip *.pyc
