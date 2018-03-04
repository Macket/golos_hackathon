from backend import login, User


def main():
    user = login('poster', 'qwerty12345')
    video = user.get_video('videopotest', '/Users/alexander/potest.mp4')

    user.add_video('jordan2', '/home/aleksei/jordan.txt', 'My favorite actress without any video')


if __name__ == '__main__':
    main()
