import requests

def get_iptv_list():
    url = "https://m3u.ibert.me/txt/fmml_ipv6.txt"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_iptv_list(content):
    target_channels = [
        "CCTV-1_综合",
        "CCTV-2_财经",
        "CCTV-3_综艺",
        "CCTV-4_中文国际",
        "CCTV-5_体育",
        "CCTV-6_电影",
        "CCTV-7_国防军事",
        "CCTV-8_电视剧",
        "CCTV-9_纪录",
        "CCTV-10_科教",
        "CCTV-11_戏曲",
        "CCTV-12_社会与法",
        "CCTV-13_新闻",
    ]
    
    m3u_content = "#EXTM3U\n"
    for line in content.splitlines():
        for channel in target_channels:
            if line.startswith(channel):
                parts = line.split(",")
                if len(parts) == 2:
                    channel_name = parts[0]
                    channel_url = parts[1]
                    m3u_content += f'#EXTINF:-1 tvg-id="{channel_name.replace("-", "").replace("_", "")}" tvg-name="{channel_name.replace("_", "")}" group-title="央视IPV6",{channel_name.replace("_", "")}\n'
                    m3u_content += f'{channel_url}\n'
    return m3u_content

def write_m3u_file(content, filename="aptv.m3u"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    iptv_content = get_iptv_list()
    m3u_content = parse_iptv_list(iptv_content)
    write_m3u_file(m3u_content, "aptv.m3u")
