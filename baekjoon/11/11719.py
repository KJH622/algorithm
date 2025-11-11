# 그대로 출력하기 2

import sys

def main():
    data = sys.stdin.read() # EOF까지 전부 읽기
    sys.stdout.write(data) # 가공 없이 그대로 출력

if __name__ == "__main__":
    main()