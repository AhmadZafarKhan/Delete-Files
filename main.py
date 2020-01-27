import os


def main():

    txt = "labelled-files.txt"
    data_path = "sorted-dataset"

    with open(txt, 'r') as f:

        check = [line.split("/")[-1].split("\n")[0] for line in f]
        # print(check)
        # print(len(check))
        f.close()

    count = 0
    for  dirs, dirnames, files in os.walk(data_path):
        for file in files:
            for name in check:
                if name == file:
                    delete_path = os.path.abspath(dirs) + "/" + file
                    os.system("rm " + delete_path)
                    print("deleted " + delete_path + " number " + str(count))
                    count += 1


if __name__ ==  '__main__':
    main()
