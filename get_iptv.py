import requests
import os

def get_iptv_list():
    url = "https://gh.aptv.app/https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/iptv.m3u"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

import re

def parse_iptv_list(content):
    m3u_content = "#EXTM3U\n"
    target_channels = [
        r'#EXTINF:-1 tvg-id="CCTV1" tvg-name="CCTV1" group-title="央视IPV6",CCTV1\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV2" tvg-name="CCTV2" group-title="央视IPV6",CCTV2\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV3" tvg-name="CCTV3" group-title="央视IPV6",CCTV3\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV4" tvg-name="CCTV4" group-title="央视IPV6",CCTV4\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV5" tvg-name="CCTV5" group-title="央视IPV6",CCTV5\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV6" tvg-name="CCTV6" group-title="央视IPV6",CCTV6\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV7" tvg-name="CCTV7" group-title="央视IPV6",CCTV7\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV8" tvg-name="CCTV8" group-title="央视IPV6",CCTV8\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV9" tvg-name="CCTV9" group-title="央视IPV6",CCTV9\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV10" tvg-name="CCTV10" group-title="央视IPV6",CCTV10\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV11" tvg-name="CCTV11" group-title="央视IPV6",CCTV11\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV12" tvg-name="CCTV12" group-title="央视IPV6",CCTV12\n(.*?)\n',
        r'#EXTINF:-1 tvg-id="CCTV13" tvg-name="CCTV13" group-title="央视IPV6",CCTV13\n(.*?)\n',
    ]
    for channel_regex in target_channels:
        match = re.search(channel_regex, content)
        if match:
            m3u_content += match.group(0)
    return m3u_content

def get_current_content(filename="aptv.m3u"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def write_m3u_file(content, filename="aptv.m3u"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    filename = "aptv.m3u"
    old_content = get_current_content(filename)
    new_iptv_content = get_iptv_list()
    new_m3u_content = parse_iptv_list(new_iptv_content)
    
    if new_m3u_content != old_content:
        write_m3u_file(new_m3u_content, filename)
        return True
    return False

if __name__ == "__main__":
    has_updates = main()
    exit(0 if has_updates else 1)
