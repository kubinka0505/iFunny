__Name = os.path.abspath("./{0}/{1}".format(
	__Out_Dir,
	"{0}_{1}.{2}".format(
		normalize(
			re.sub(
				"[^\w\-_\. ]", "_",
				Config["Text"]["Content"][:25]
			)
		).replace(".", ""),
		Random_String(8),
		"png" if len(Frames) == 1 else "gif"
		).replace(" ", "_")
	)
)

__Name = __Out_Dir + os.sep + __Name.split(os.sep)[-1]