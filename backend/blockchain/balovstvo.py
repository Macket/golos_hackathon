from backend import login, User


def main():
    user = login('liker', 'qwerty12345')
    #video = user.get_video('hackathon-mipt', '/home/aleksei/pizda')

    # user.add_video('blockchaining', '/home/aleksei/jordan.txt', 'Ooops, there is no any video')

    videos_list = User.get_videos_list('empty-test')
    print(videos_list)

if __name__ == '__main__':
    main()
