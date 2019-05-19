import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--db', help='Sqlite database location',
        type=str, required=True)
    args = parser.parse_args()

if __name__ == "__main__":
    main()