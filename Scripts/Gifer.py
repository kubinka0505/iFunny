Caption = Image.open(Frame)
if Config()["Image"]["Crop"] == True: Caption = Caption.crop(Caption.getbbox())

Width = Pasted.size[0]
Percentage = (Width / float(Caption.size[0]))
Height_Size = int((float(Caption.size[1]) * float(Percentage)))
Caption = Caption.resize((Width, Height_Size), Image.LANCZOS)

Captionized = Margin(Caption, Pasted.size[1])
Captionized.paste(Pasted)