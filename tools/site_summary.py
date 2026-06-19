import json
from datetime import datetime

def load_site_data():
    return {
        "site_name": "爱游戏门户",
        "url": "https://home-portal-i-game.com.cn",
        "tags": ["游戏", "门户", "资讯", "社区"],
        "keywords": ["爱游戏", "游戏门户", "游戏资讯"],
        "description": "一个专注于提供游戏资讯、社区互动和资源分享的综合游戏门户平台。",
        "creation_date": "2024-01-15",
        "category": "游戏娱乐",
        "features": [
            "最新游戏资讯",
            "玩家社区论坛",
            "游戏资源下载",
            "游戏评测与攻略"
        ]
    }

def format_summary(site_info):
    lines = []
    lines.append("=" * 50)
    lines.append("站点摘要报告")
    lines.append("=" * 50)
    lines.append(f"站点名称: {site_info['site_name']}")
    lines.append(f"访问地址: {site_info['url']}")
    lines.append(f"站点类别: {site_info['category']}")
    lines.append(f"创建日期: {site_info['creation_date']}")
    lines.append("")
    lines.append("核心关键词:")
    for keyword in site_info['keywords']:
        lines.append(f"  - {keyword}")
    lines.append("")
    lines.append("标签列表:")
    for tag in site_info['tags']:
        lines.append(f"  #{tag}")
    lines.append("")
    lines.append("站点描述:")
    lines.append(f"  {site_info['description']}")
    lines.append("")
    lines.append("主要功能:")
    for idx, feature in enumerate(site_info['features'], 1):
        lines.append(f"  {idx}. {feature}")
    lines.append("=" * 50)
    return "\n".join(lines)

def generate_json_output(site_info):
    output = {
        "metadata": {
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "report_type": "site_summary"
        },
        "site_data": site_info
    }
    return json.dumps(output, ensure_ascii=False, indent=2)

def show_compact_summary(site_info):
    parts = []
    parts.append(f"【{site_info['site_name']}】")
    parts.append(f"URL: {site_info['url']}")
    parts.append(f"关键词: {'、'.join(site_info['keywords'])}")
    parts.append(f"标签: {' '.join('#' + t for t in site_info['tags'])}")
    parts.append(f"简介: {site_info['description'][:30]}...")
    return " | ".join(parts)

def main():
    site_data = load_site_data()
    print("正在生成站点摘要...\n")
    print(format_summary(site_data))
    print("\nJSON 格式输出:\n")
    print(generate_json_output(site_data))
    print("\n紧凑摘要:\n")
    print(show_compact_summary(site_data))
    print("\n摘要生成完毕。")

if __name__ == "__main__":
    main()