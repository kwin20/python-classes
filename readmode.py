from sys import argv

if len(argv) == 3:
    try:
        fp = open(argv[1], "r")
        fp1 = open(argv[2], "w+")
        for i in fp:
            fp1.write(i)
        print("File is copied successfully")
        fp1.seek(0, 0)
        content = fp1.read()
        print(content)
        fp.close()
        fp1.close()
    except Exception:
      print("Error")