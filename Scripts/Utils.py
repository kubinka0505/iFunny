def Trans_Paste(Background: Image, Foreground: Image) -> Image:
	"""Pasting transparent `Foreground` to `Background`."""
	FRGRND_TRNS = Image.new("RGBA", Background.size)
	#---#
	Background_Width, Background_Height = Background.size
	Foreground_Width, Foreground_Height = Foreground.size
	#---#
	FRGRND_TRNS.paste(Foreground, ((Background_Width - Foreground_Width) // 2, (Background_Height - Foreground_Height) // 2), mask = Foreground)
	#---#
	IMG_RET = Image.alpha_composite(Background, FRGRND_TRNS)
	return IMG_RET

def Get_Service(URL: str):
	'''"Converting" direct URL to direct Image.

	Supported Services:
	- Tenor
	- Giphy
	- Gfycat
	- ImgFlip
	- Pinterest
	'''
	if "tenor.com/view" in URL:
		return get(URL).text.split('contentUrl')[1].split("content")[0][2:].split('"')[1].replace("\\u002F", "/")
	if "giphy.com/gifs" in URL:
		return "https://media"+str(get(URL).text).split("https://media")[2].split('"')[0]
	if "//gfycat.com/" in URL:
		return get(URL).text.split("twitter:image")[1].split('"')[2].replace('size_restricted', 'small')
	if "//imgflip.com/gif/" in URL:
		return URL.replace("//", "//i.").replace("/gif", "")+".gif"
	if "//www.pinterest." in URL:
		return get(URL).text.split('"preload"')[1].split('href')[1].split('"')[1]
	else:
		return URL

def Margin(Picture: Image, Top: int, Color: ImageColor = "#FFF") -> Image:
	"""Adds margin to an `Picture`."""
	Width, Height = Picture.size
	Height = Height + Top + 0
	#---#
	Field = Image.new(Picture.mode, (Width, Height), Color)
	Field.paste(Picture, (0, Top))
	return Field

def Config():
	"""Loading values from JSON file."""
	__Path = "{0}\Config.json"
	#---#
	if system() != "Windows":
		__Path = __Path.replace("\\", "/")
	#---#
	return load(open(__Path.format(os.getcwd()), encoding = "utf-8"))

def Random_String(Length: int = 16):
	"""Random string creation used in saving files."""
	return "".join(choice(printable[0:62]) for String in range(Length))