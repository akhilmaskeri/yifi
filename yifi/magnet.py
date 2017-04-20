import urllib

trackers = [
    'udp://open.demonii.com:1337/announcejj',
    'udp://tracker.istole.it:80',
    'http://tracker.yify-torrents.com/announce',
    'udp://tracker.publicbt.com:80',
    'udp://tracker.openbittorrent.com:80',
    'udp://tracker.coppersurfer.tk:6969',
    'udp://glotorrents.pw:6969/announce',
    'udp://tracker.opentrackr.org:1337/announce',
    'udp://torrent.gresille.org:80/announce',
    'udp://p4p.arenabg.com:1337',
    'udp://tracker.leechers-paradise.org:6969',
    'http://exodus.desync.com:6969/announce'
]

def getMagnet(torrent,quality):

    base = "magnet:?xt=urn:btih:"+torrent["torrents"][quality]["hash"]+"&dn"+urllib.quote(torrent["title"])
    for t in trackers:
        base+= '&tr='+t

    return base
