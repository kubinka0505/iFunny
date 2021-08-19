__Gifsicle = "Gifsicle"
__Gifsicle_Error_1 = "\n{0}Gifsicle{1} not found!".format(Styles.Yellow, Styles.Reset)
__Gifsicle_Error_2 = "\n{0}Image will not be processed.{1}{2}".format(Styles.Red, Styles.Reset, __BEL)

if not Config["Settings"]["Packages"]["Location"][__Gifsicle]:
	for File in next(os.walk("."))[2]:
		if os.path.basename(File)[:6] == __Gifsicle.lower():
			try:
				__Gifsicle = os.path.abspath(File)
			except:
				pass
	else:
		__Gifsicle = Variable_Search(Content = __Gifsicle.lower())
		if __Gifsicle:
			if os.path.isfile(__Gifsicle):
				pass
			else:
				raise SystemExit(__Gifsicle_Error_1 + ' {1}("{0}"){2}'.format(__Gifsicle, Styles.DarkGray, Styles.Reset) + __Gifsicle_Error_2)
else:
	__Gifsicle = os.path.abspath(Config["Settings"]["Packages"]["Location"][__Gifsicle])
	if os.path.isfile(__Gifsicle):
		pass
	else:
		raise SystemExit(__Gifsicle_Error + "({0})".format(__Gifsicle))