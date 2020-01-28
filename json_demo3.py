def main():
    f = open("new_file.txt", "w+")

    for i in range(10):
        f.write("this is line %d\r\n" % (i+1))

    f.close()


if __name__ =="__main__":
    main()