import os
import unittest
import urllib.request

import gradio as gr

from apps.data_explorer.data_explorer import construct_app
from apps.data_explorer.loader import REPO_ROOT, load_datasets


class TestDataExplorer(unittest.TestCase):
    def test_ui(self):
        test_data_url = ("https://storage.googleapis.com/"
                         "camel-bucket/datasets/test/DATA.zip")
        data_dir = os.path.join(REPO_ROOT, "datasets_test")
        test_file_path = os.path.join(data_dir,
                                      os.path.split(test_data_url)[1])
        os.makedirs(data_dir, exist_ok=True)
        urllib.request.urlretrieve(test_data_url, test_file_path)

        datasets = load_datasets(data_dir)
        with gr.Blocks() as blocks:
            construct_app(blocks, datasets)


if __name__ == '__main__':
    unittest.main()
