import sys
import argparse


def main(args):
    parser = argparse.ArgumentParser(prog='lan', description="懒人测试框架")
    subparsers = parser.add_subparsers()

    parser_install = subparsers.add_parser('it', help='- 初始化接口测试')
    # parser_install.set_defaults(func=pip2.cli_wrapper.install)


if __name__ == '__main__':
    main()
