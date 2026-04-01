import eyed3
import click
from eyed3.id3.frames import ImageFrame
from pathlib import Path

@click.command()
@click.option('--artist', '-a', help='Artist Name')
@click.option('--album', '-A', help='Album Name')
@click.option('--title', '-t', help='Song Title')
@click.option('--track', '-T', help='Track Number')
@click.option('--cover', '-c', help='Set "Cover image" to true. Only use this if you have a cover image called `Cover.jpg` in the same directory as your mp3 file.', is_flag=True)
@click.option('filename', '-f', help='Add filename(s). If no file names are provided, the script will assume the current directory contains mp3 files from the same album.', multiple=True)
def command(artist, album, title, track, cover, filename):
	print(artist)
	print(album)
	print(title)
	print(track)
	print(cover)
	print(filename)
	if len(filename) != 0:
		for f in filename:
			mp3file = eyed3.load(f)
			if (mp3file.tag == None):
				mp3file.initTag()
			if cover:
				mp3file.tag.images.set(ImageFrame.FRONT_COVER, open('cover.jpg','rb').read(), 'image/jpeg')
			if artist != None:
				mp3file.tag.artist = f"{artist}"
			if album != None:
				mp3file.tag.album = f"{album}"
			if title != None:
				mp3file.tag.title = f"{title}"
			if track != None:
				mp3file.tag.track_num = f"{track}"
			mp3file.tag.save()
	else:
		total = input(f"What is the total number of tracks for {album}: ")
		for f in Path('.').glob('*.mp3'):
			mp3file = eyed3.load(f)
			if (mp3file.tag == None):
				mp3file.initTag()
			if cover:
				mp3file.tag.images.set(ImageFrame.FRONT_COVER, open('cover.jpg','rb').read(), 'image/jpeg')
			if artist != None:
                                mp3file.tag.artist = f"{artist}"
			if album != None:
				mp3file.tag.album = f"{album}"
			title = input(f"What is the title of {f}: ")
			mp3file.tag.title = f"{title}"
			tracknum = input(f"What track number is {f}: ")
			mp3file.tag.track_num = (int(tracknum), int(total))
			mp3file.tag.save()
		
