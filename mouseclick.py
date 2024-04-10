import pyautogui
import time

def main():
    try:
        while True:

            pyautogui.click()

            print("Tıklama yapıldı!")


            time.sleep(2)
    except KeyboardInterrupt:
        print("\nProgramdan çıkılıyor...")

if __name__ == "__main__":
    main()
