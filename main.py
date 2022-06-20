from os import listdir
from os.path import isfile, join
from PIL import Image
import importlib.util
import numpy as np
import cv2

class main():
    def __init__(self) -> None:
        self.plugins_location = "plugins"
        self.annotation_plugins = self.load_plugins(self.scan_for_plugin_files())
        

    def load_plugins(self, files):
        modules = []
        for f in files:
            spec = importlib.util.spec_from_file_location(f, join(self.plugins_location, f))
            foo = importlib.util.module_from_spec(spec)
            modules.append(foo)
            spec.loader.exec_module(foo)
        return modules

    def scan_for_plugin_files(self):
        onlyfiles = [f for f in listdir(self.plugins_location) if isfile(join(self.plugins_location, f))]
        return onlyfiles


    def execute_plugins(self, modules ,images):
        for module in modules:
            for im in images:
                print(module.execute(im))

    def execute_annotation_plugins(self, images):
        self.execute_plugins(self.annotation_plugins, images)

def run():
    app = main()
    images=[]
    images.append(np.asarray(Image.open("C:\\Users\\justa\\OneDrive\\Pictures\\jobsselection.png"))) 
    print(len(images))
    cv2.imshow('t', images[0])
    cv2.waitKey()
    app.execute_annotation_plugins(images)
    
run()