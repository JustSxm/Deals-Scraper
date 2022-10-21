


def print_info(msg):
    color = '\033[94m'
    print(color + "[Scraper] " + msg + '\033[0m')


def print_scraper(name, msg):
    print_info( f"» {name} » " + msg)
