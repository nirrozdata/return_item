import dtlpy as dl
import os

class ServiceRunner(dl.BaseServiceRunner):

    def autoscaler_test_move(self, item, progress=None):
        name, ext = os.path.splitext(item.filename)
        new_name = name + "_moved" + ext
        item.move(new_name)
        print("Hello world")

        return item.id
