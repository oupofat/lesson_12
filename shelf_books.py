def shelf_books(books):

	tally = {}
	for title in books:
		if title not in tally:
			tally[title]=0
		tally[title]+=1
	
books= ("harry potter", "doctor who", "captain america","hulk","deadpool","captain britain")
shelf_books(books)