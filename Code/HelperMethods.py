#Helper Methods
def findBetween(s, first, last ):
	start_index = s.find(first)
	end_index = start_index + len(first)
	last_index = s.find(last)

	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
		return ""