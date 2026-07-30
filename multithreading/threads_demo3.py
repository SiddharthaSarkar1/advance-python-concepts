from threading import Thread
import time


def download(file_name):
    print(f"Downloading file ... {file_name}")
    time.sleep(0.5)
    print("Downloading complete.")


if __name__ == "__main__":

    files = ['video.mp4', 'image.png', 'audio.mp3', 'data.csv']
    threads = []

    start = time.perf_counter()

    for file in files:
        t = Thread(target=download, args=(file,))
        threads.append(t)

    for t in threads:
        t.start()
        
    for t in threads:
        t.join()

    end = time.perf_counter()   
    print(f"Time taken: {end - start:,.2f}")

    print("Bye!")




