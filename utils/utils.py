def prep_filename( string: str ) -> str:
    
    string = string.lower()
    string = string.replace( ' ', '_' )
    string = string.replace( '-', '_' )
    string = string.replace( ':', '_' )
    string = string.replace( 'è', 'e' )
    
    return string    

def make_md_link( link: str, preview=None ) -> str:

    if preview == None:
        return '[{}]'.format(link)
    else:
        return '[{}]({})'.format(preview, link)

def int_with_leading_zeroes( x, zeroes: int ) -> str:
    return "0" * ( zeroes - len(str(x)) ) + str(x)
