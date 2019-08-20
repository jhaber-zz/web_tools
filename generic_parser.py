def parsefile_by_tags(HTML_file):
    """Cleans HTML by removing inline tags, ripping out non-visible tags, replacing paragraph tags 
    with a random string, and finally using this to separate HTML into chunks."""

    random_string = "".join(map(chr, os.urandom(75))) # Create random string for tag delimiter
    soup = BeautifulSoup(open(HTML_file), "lxml")
    inline_tags = ["b", "big", "i", "small", "tt", "abbr", "acronym", "cite", "dfn", "em", "kbd", "strong", "samp", "var", "bdo", "map", "object", "q", "span", "sub", "sup"] # junk tags to eliminate

    [s.extract() for s in soup(['style', 'script', 'head', 'title', 'meta', '[document]'])] # Remove non-visible tags
    for it in inline_tags:
        [s.extract() for s in soup("</" + it + ">")] # Remove inline tags
    visible_text = soup.getText(random_string).replace("\n", "") # Replace "p" tags with random string, eliminate ‘\n’

    # Split text into list using random string, eliminate tabs, convert unicode to readable text:
    visible_text = list(normalize("NFKC",elem.replace("\t","")) for elem in visible_text.split(random_string))
    visible_text = list(filter(lambda vt: vt.split() != [], visible_text)) # Eliminate empty elements
    return(visible_text)
