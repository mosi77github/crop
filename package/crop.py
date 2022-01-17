def crop(path_i: str, path_o: str, both: int) -> None:
    import numpy as np
    import cv2
    import os
    import crop

    # درقسمت زیر قسمتی را که میخواهیم نگه داریم جدا میکنیم
    import os

    relevant_path = path_i
    included_extensions = ["jpg", "jpeg", "bmp", "png", "gif"]
    file_names = [
        fn
        for fn in os.listdir(relevant_path)
        if any(fn.endswith(ext) for ext in included_extensions)
    ]

    dir_list = file_names
    x = []
    y = []
    w = []
    h = []
    for i in dir_list:
        im = cv2.imread(path_i + "/" + f"{i}")
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        lowerb = (0, 0, 70)
        upperb = (360, 255, 255)
        mask = cv2.inRange(hsv, lowerb, upperb)
        contours, _ = cv2.findContours(
            mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # بزرگ ترین کانتور که همان بخش مطلوب ماست را پیدا میکنیم
        wbcs = []
        for c in contours:
            A = cv2.contourArea(c)
            wbcs.append(A)
        # print(wbcs)
        x1 = np.where(wbcs == np.array(wbcs).max())
        x2 = int(x1[0])
        # یک مستطیل که به آن فیت میشود را پیدا کرده و عکس را از آن جا کراپ میکنیم
        xx, yy, ww, hh = cv2.boundingRect(contours[x2])
        x.append(xx)
        y.append(yy)
        w.append(ww)
        h.append(hh)

        crop = im[yy : yy + hh, xx : xx + ww]
        cv2.imwrite(path_o + "/" + f"{i}", crop)
        
    if both == 1:
        relevant_path = path_i
        included_extensions = ["txt"]
        file_names = [
            fn
            for fn in os.listdir(relevant_path)
            if any(fn.endswith(ext) for ext in included_extensions)
        ]

        dir_list = file_names
        d = 0
        shape = mask.shape
        for i in dir_list:
            with open(path_i + "/" + i) as f:
                content = f.read()
            spl = content.split()
            le = len(spl)
            rows, cols = (int(le / 5), 5)
            arr = [[0 for i in range(cols)] for j in range(rows)]
            for j in range(0, le):
                arr[int((j) / 5)][j % 5] = spl[j]
            for z in range(0, le):
                if z % 5 == 1:
                    arr[int((z) / 5)][z % 5] = shape[1] * float(
                        arr[int((z) / 5)][z % 5]
                    )
                    arr[int((z) / 5)][z % 5] = arr[int((z) / 5)][z % 5] - x[d]
                    arr[int((z) / 5)][z % 5] = arr[int((z) / 5)][z % 5] / w[d]
                    arr[int((z) / 5)][z % 5] = float(
                        "{:.6f}".format(arr[int((z) / 5)][z % 5])
                    )
                    arr[int((z) / 5)][z % 5] = format(arr[int((z) / 5)][z % 5], ".6f")
                if z % 5 == 2:
                    arr[int((z) / 5)][z % 5] = shape[0] * float(
                        arr[int((z) / 5)][z % 5]
                    )
                    arr[int((z) / 5)][z % 5] = arr[int((z) / 5)][z % 5] - y[d]
                    arr[int((z) / 5)][z % 5] = arr[int((z) / 5)][z % 5] / h[d]
                    arr[int((z) / 5)][z % 5] = float(
                        "{:.6f}".format(arr[int((z) / 5)][z % 5])
                    )
                    arr[int((z) / 5)][z % 5] = format(arr[int((z) / 5)][z % 5], ".6f")
                if z % 5 == 3:
                    arr[int((z) / 5)][z % 5] = shape[1] * float(
                        arr[int((z) / 5)][z % 5]
                    )
                    arr[int((z) / 5)][z % 5] = arr[int((z) / 5)][z % 5] / w[d]
                    arr[int((z) / 5)][z % 5] = float(
                        "{:.6f}".format(arr[int((z) / 5)][z % 5])
                    )
                    arr[int((z) / 5)][z % 5] = format(arr[int((z) / 5)][z % 5], ".6f")
                if z % 5 == 4:
                    arr[int((z) / 5)][z % 5] = shape[0] * float(
                        arr[int((z) / 5)][z % 5]
                    )
                    arr[int((z) / 5)][z % 5] = arr[int((z) / 5)][z % 5] / h[d]
                    arr[int((z) / 5)][z % 5] = float(
                        "{:.6f}".format(arr[int((z) / 5)][z % 5])
                    )
                    arr[int((z) / 5)][z % 5] = format(arr[int((z) / 5)][z % 5], ".6f")
            d = d + 1
            textfile = open(path_o + "/" + f"{i}.txt", "x")
            with open(path_o + "/" + f"{i}.txt", "w") as f:
                for j in range(0, le):
                    if j % 5 == 0 and j != 0:
                        f.write("\n")
                    f.write(str(arr[int((j) / 5)][j % 5]))
                    f.write(" ")
