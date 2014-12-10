#!/usr/bin/env python
# coding = utf-8
# Author: Archer Reilly
# Date: 09/Dec/2014
# File: NonPlainFileFilter.py
# Desc: filter out the non plain files that can not be parsed by
# BeautifulSoup
#
# Produced By CSRGXTU

class NonPlainFileFilter(object):
  plainFileExtensions = ['.asp', '.aspx', '.cer', '.cfm', '.csr',
                        '.css', '.htm', '.html', '.js', '.jsp',
                        '.php', '.rss', '.xhtml', '.xml']
  nonPlainFileExtensions = ['.doc', '.docx', '.log', '.msg', '.odt',
                        '.pages', '.rtf', '.tex', '.txt', '.wpd',
                        '.wps', '.csv', '.dat', '.gbr', '.ged',
                        '.key', '.keychain', '.pps', '.ppt', '.pptx',
                        '.sdf', '.tar', '.tax2012', '.tax2014',
                        '.vcf', '.aif', '.iff', '.m3u', '.m4a',
                        '.mid', '.mp3', '.mpa', '.ra', '.wav',
                        '.wma', '.3g2', '.3gp', '.asf', '.asx',
                        '.avi', '.flv', '.m4v', '.mov', '.mp4',
                        '.mpg', '.rm', '.srt', '.swf', '.vob',
                        '.wmv', '.3dm', '.3ds', '.max', '.obj',
                        '.bmp', '.dds', '.gif', '.jpg', '.png',
                        '.psd', '.pspimage', '.tga', '.thm', '.tif',
                        '.tiff', '.yuv', '.ai', '.eps', '.ps', '.svg',
                        '.indd', '.pct', '.pdf', '.xlr', '.xls',
                        '.xlsx', '.accdb', '.db', '.dbf', '.mdb',
                        '.pdb', '.sql', '.apk', '.app', '.bat',
                        '.cgi', '.com', '.exe', '.gadget', '.jar',
                        '.pif', '.vb', '.wsf', '.dem', '.gam',
                        '.nes', '.rom', '.sav', '.dwg', '.dxf',
                        '.gpx', '.kml', '.kmz', '.crx', '.plugin',
                        '.fnt', '.fon', '.otf', '.ttf', '.cab',
                        '.cpl', '.cur', '.deskthemepack', '.dll',
                        '.dmp', '.drv', '.icns', '.ico', '.Ink',
                        '.sys', '.cfg', '.ini', '.prf', '.hqx',
                        '.mim', '.uue', '.7z', '.cbr', '.deb',
                        '.gz', '.pkg', '.rar', '.rmp', '.sitx',
                        '.tar.gz', '.zip', '.zipx', '.biz2',
                        '.bin', '.cue', '.dmg', '.iso', '.mdf',
                        '.toast', '.vcd', '.c', '.class', '.cpp',
                        '.cs', '.dtd', '.fla', '.h', '.java',
                        '.lua', '.m', '.sh', '.sln',
                        '.swift', '.vcxproj', '.xcodeproj', '.bak',
                        '.tmp', '.crdownload', '.ics', '.msi', '.part',
                        '.torrent', '.rmvb']
  # getFilteredUrls
  # get the filtered urls
  #
  # @param urls list(string)
  # @return res list(string) or False
  def getFilteredUrls(self, urls):
    res = []

    for url in urls:
      if self.isPlainText(url):
        res.append(url)

    if len(res) == 0:
      return False
    else:
      return res
    #pass
  
  # isPlainText
  # check if an url is plain text by url extension, not work
  # exactly correct, but most time works
  #
  # @param url
  # @return boolean
  def isPlainText(self, url):
    url = url.lower()

    for item in self.plainFileExtensions:
      if url.endswith(item):
        return True

    for item in self.nonPlainFileExtensions:
      if url.endswith(item):
        return False

    return True
