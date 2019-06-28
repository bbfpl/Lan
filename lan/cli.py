# -*- coding: UTF-8 -*-
import argparse
from lan.commands.it import it
from lan.commands.st import st
from lan.commands.sm import sm

def main():
    parser = argparse.ArgumentParser(prog='lan', description="Lan(懒)是一套Python测试套件")
    subparsers = parser.add_subparsers()

    parser_it = subparsers.add_parser('it', help='- 接口测试')
    parser_it.add_argument('name', help='- 请输入项目名称')
    parser_it.set_defaults(func=it)

    parser_st = subparsers.add_parser('st', help='- 压力测试')
    parser_st.add_argument('name', help='- 请输入项目名称')
    parser_st.set_defaults(func=st)

    parser_st = subparsers.add_parser('sm', help='- 服务器监控')
    parser_st.set_defaults(func=monitor)

    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help()


if __name__ == '__main__':
    main()
