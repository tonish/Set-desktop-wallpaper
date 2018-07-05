import win32console
import ctypes

def setWallpaperWithCtypes(path):
    # This code is based on the following two links
    # http://mail.python.org/pipermail/python-win32/2005-January/002893.html
    # http://code.activestate.com/recipes/435877-change-the-wallpaper-under-windows/
    cs = ctypes.c_buffer(path)
    ok = ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, cs, 1)

if __name__ == "__main__":
    path = 'C:\\Users\\Public\\Pictures\\Sample Pictures\\Jellyfish.jpg'
    setWallpaperWithCtypes(path)

