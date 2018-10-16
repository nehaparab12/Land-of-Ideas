blog = """<ul style="position:absolute; right:-1em; top:50%; margin-top:-2.4em; width:38%; min-width:25em; font-size:95%;">
<li style="position:absolute; left:0; top:0;"><a href="/wiki/Portal:Arts" title="Portal:Arts">Arts</a></li>
<li style="position:absolute; left:0; top:1.6em;"><a href="/wiki/Portal:Biography" title="Portal:Biography">Biography</a></li>
<li style="position:absolute; left:0; top:3.2em;"><a href="/wiki/Portal:Geography" title="Portal:Geography">Geography</a></li>
<li style="position:absolute; left:33%; top:0;"><a href="/wiki/Portal:History" title="Portal:History">History</a></li>
<li style="position:absolute; left:33%; top:1.6em;"><a href="/wiki/Portal:Mathematics" title="Portal:Mathematics">Mathematics</a></li>
<li style="position:absolute; left:33%; top:3.2em;"><a href="/wiki/Portal:Science" title="Portal:Science">Science</a></li>
<li style="position:absolute; left:66%; top:0;"><a href="/wiki/Portal:Society" title="Portal:Society">Society</a></li>
<li style="position:absolute; left:66%; top:1.6em;"><a href="/wiki/Portal:Technology" title="Portal:Technology">Technology</a></li>
<li style="position:absolute; left:66%; top:3.2em;"><strong><a href="/wiki/Portal:Contents/Portals" title="Portal:Contents/Portals">All portals</a></strong></li>
</ul>"""

d = blog
a = d.find('<a href="') + 9
b = d.find('">', a)
c = b + 2
cnt = blog.count('<a href="')

for i in range (0,cnt):
    print(d[a:b])
    d=d[c:]
    a = d.find('<a href="') + 9
    b = d.find('">', a)
    c = b + 2




